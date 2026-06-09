from flask import Flask, request, jsonify, render_template
from database import get_db_connection, create_tables
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)
CORS(app)

create_tables()


def send_telegram_alert(message):
    try:
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            print("[ALERT SKIPPED] Telegram env not configured")
            return

        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }

        requests.post(telegram_url, json=payload, timeout=5)
        print("[ALERT SENT] Telegram notification sent")

    except Exception as e:
        print("[ALERT ERROR]", str(e))


def check_single_site(site_id, url):
    status_code = None
    response_time = None
    status = "DOWN"

    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)
        status_code = response.status_code

        if 200 <= status_code < 400:
            status = "SLOW" if response_time > 1000 else "UP"
        else:
            status = "DOWN"

    except requests.exceptions.RequestException:
        status = "DOWN"

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO uptime_logs (site_id, status, status_code, response_time)
        VALUES (%s, %s, %s, %s)
        """,
        (site_id, status, status_code, response_time)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"[AUTO CHECK] {url} => {status}")

    if status == "DOWN":
        alert_message = f"""
🚨 Site Down Alert

URL: {url}
Status: {status}
Status Code: {status_code}
Response Time: {response_time} ms
"""
        send_telegram_alert(alert_message)

    return {
        "url": url,
        "status": status,
        "status_code": status_code,
        "response_time_ms": response_time
    }


def monitor_all_sites():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sites")
    sites = cursor.fetchall()

    cursor.close()
    conn.close()

    for site in sites:
        check_single_site(site["id"], site["url"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/db-test")
def db_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "connected",
            "database": version["version"]
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/api/add-site", methods=["POST"])
def add_site():
    data = request.get_json()

    if not data or "name" not in data or "url" not in data:
        return jsonify({"error": "name and url are required"}), 400

    name = data["name"]
    url = data["url"]

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sites (name, url)
        VALUES (%s, %s)
        RETURNING id
        """,
        (name, url)
    )

    site = cursor.fetchone()
    site_id = site["id"]

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "Site added successfully",
        "site_id": site_id,
        "name": name,
        "url": url
    })


@app.route("/api/sites", methods=["GET"])
def get_sites():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sites ORDER BY id DESC")
    sites = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(sites)


@app.route("/api/check-site", methods=["POST"])
def check_site():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data["url"]

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM sites WHERE url = %s LIMIT 1", (url,))
    site = cursor.fetchone()

    if site:
        site_id = site["id"]
    else:
        cursor.execute(
            """
            INSERT INTO sites (name, url)
            VALUES (%s, %s)
            RETURNING id
            """,
            (url, url)
        )
        new_site = cursor.fetchone()
        site_id = new_site["id"]
        conn.commit()

    cursor.close()
    conn.close()

    result = check_single_site(site_id, url)
    return jsonify(result)


@app.route("/api/check-all", methods=["GET"])
def check_all_now():
    monitor_all_sites()

    return jsonify({
        "message": "All sites checked successfully"
    })


@app.route("/api/logs", methods=["GET"])
def get_logs():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            uptime_logs.id,
            sites.name,
            sites.url,
            uptime_logs.status,
            uptime_logs.status_code,
            uptime_logs.response_time,
            uptime_logs.checked_at
        FROM uptime_logs
        JOIN sites ON uptime_logs.site_id = sites.id
        ORDER BY uptime_logs.id DESC
        LIMIT 50
    """)

    logs = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(logs)


@app.route("/api/delete-site/<int:site_id>", methods=["DELETE"])
def delete_site(site_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM uptime_logs WHERE site_id = %s", (site_id,))
    cursor.execute("DELETE FROM sites WHERE id = %s", (site_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "Site deleted successfully",
        "site_id": site_id
    })


@app.route("/api/site-stats", methods=["GET"])
def site_stats():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            sites.id,
            sites.name,
            sites.url,
            COUNT(uptime_logs.id) AS total_checks,
            COALESCE(SUM(CASE WHEN uptime_logs.status = 'UP' THEN 1 ELSE 0 END), 0) AS up_checks,
            COALESCE(
                ROUND(
                    (SUM(CASE WHEN uptime_logs.status = 'UP' THEN 1 ELSE 0 END) * 100.0) / 
                    NULLIF(COUNT(uptime_logs.id), 0),
                    2
                ),
                0
            ) AS uptime_percentage
        FROM sites
        LEFT JOIN uptime_logs ON sites.id = uptime_logs.site_id
        GROUP BY sites.id, sites.name, sites.url
        ORDER BY sites.id DESC
    """)

    stats = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(stats)


scheduler = BackgroundScheduler()
scheduler.add_job(
    func=monitor_all_sites,
    trigger="interval",
    minutes=1
)
scheduler.start()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)