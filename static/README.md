# Site Uptime Monitoring System

A real-time website uptime monitoring dashboard built with Flask, SQLite, APScheduler, JavaScript, and Telegram alerts. This project monitors website availability, response time, HTTP status codes, uptime percentage, and sends instant alerts when a website goes down.

## 🚀 Features

- Add and monitor multiple websites
- Automatic uptime checks using background scheduler
- Manual “Check All Now” option
- UP / DOWN / SLOW status tracking
- Response time monitoring
- Uptime percentage calculation
- Recent monitoring logs
- Premium dashboard UI
- Response time analytics chart
- Telegram downtime alerts
- Delete monitored websites
- Secure environment variables using `.env`

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Scheduler:** APScheduler
- **Frontend:** HTML, CSS, JavaScript
- **Charts:** Chart.js
- **Alerts:** Telegram Bot API
- **Security:** python-dotenv for environment variables

## 📁 Project Structure

```txt
uptime-monitor/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/site-uptime-monitor.git
cd site-uptime-monitor
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows PowerShell:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env` file

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

### 6. Run the project

```bash
python app.py
```

Open in browser:

```txt
http://127.0.0.1:5000
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Dashboard UI |
| POST | `/api/add-site` | Add a website |
| GET | `/api/sites` | Get all websites |
| POST | `/api/check-site` | Check single website |
| GET | `/api/check-all` | Check all websites manually |
| GET | `/api/logs` | Get recent monitoring logs |
| GET | `/api/site-stats` | Get uptime percentage stats |
| DELETE | `/api/delete-site/<site_id>` | Delete a website |

## 📊 How It Works

1. User adds website URL from the dashboard.
2. Flask backend stores the website in SQLite database.
3. APScheduler automatically checks all websites every minute.
4. System records response time, status code, and website status.
5. If a website is down, Telegram alert is sent instantly.
6. Dashboard displays uptime percentage, logs, cards, and charts.

## ☁️ Azure Use Case

This project can be deployed and enhanced using Azure services:

- **Azure App Service:** Host the Flask backend and dashboard
- **Azure Database for PostgreSQL:** Replace SQLite for production database
- **Azure Monitor:** Track app performance, logs, failures, and uptime
- **Application Insights:** Monitor API response time and exceptions
- **Azure Key Vault:** Store Telegram bot token and secrets securely
- **Azure Functions:** Run scheduled uptime checks serverlessly

## 💼 Resume Description

Built a real-time Site Uptime Monitoring System using Python Flask, SQLite, APScheduler, JavaScript, and Telegram Bot API. The system monitors multiple websites, tracks response time, calculates uptime percentage, stores monitoring logs, displays analytics on a dashboard, and sends instant downtime alerts.

## 📌 Future Improvements

- Email alerts
- User authentication
- PostgreSQL database
- Azure App Service deployment
- Docker support
- Advanced charts and reports
- Public status page

## 👨‍💻 Author

Abhay Shukla
