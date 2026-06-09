# 🚀 UptimePro – Azure-Based Site Uptime Monitoring System

UptimePro is a cloud-based website uptime monitoring platform built using Python Flask and deployed completely on Microsoft Azure Cloud.

The system continuously monitors websites, tracks uptime percentage, response time, and sends instant Telegram alerts whenever a website goes down.

This project demonstrates real-world cloud deployment, monitoring, automation, database integration, and Azure cloud services implementation.

---

# 🌐 Live Features

✅ Website Uptime Monitoring
✅ Real-Time Website Health Check
✅ Automatic Monitoring Scheduler
✅ Telegram Alert Notifications
✅ Azure PostgreSQL Cloud Database
✅ Response Time Analytics
✅ Uptime Percentage Tracking
✅ Monitoring Dashboard UI
✅ Cloud Deployment on Azure
✅ Application Performance Monitoring
✅ CI/CD Deployment using GitHub & Azure

---

# 🛠️ Tech Stack

## 🔹 Backend

* Python
* Flask
* APScheduler
* Requests
* Flask-CORS
* Psycopg2

## 🔹 Frontend

* HTML
* CSS
* JavaScript

## 🔹 Database

* Azure PostgreSQL Flexible Server

## 🔹 Cloud Services

* Azure App Service
* Azure PostgreSQL
* Azure Application Insights

## 🔹 Monitoring & Alerts

* Telegram Bot API
* Azure Logs & Monitoring

## 🔹 DevOps / Deployment

* Git
* GitHub
* GitHub Actions
* Azure Deployment Center
* CI/CD Deployment

---

# ☁️ Azure Services Used

## 🔹 Azure App Service

Hosted and deployed the Flask application on Microsoft Azure cloud platform.

### Used For:

* Cloud hosting
* Application deployment
* Public URL hosting
* CI/CD integration

---

## 🔹 Azure PostgreSQL Flexible Server

Used as the cloud database to store:

* Website information
* Monitoring logs
* Uptime history
* Response time records

### Features Used:

* Cloud database management
* Firewall configuration
* Secure database access
* PostgreSQL integration with Flask

---

## 🔹 Azure Application Insights

Used for:

* Application monitoring
* Error tracking
* Performance analytics
* Request monitoring
* Log monitoring

---

# 🔄 CI/CD Deployment

Implemented automatic deployment pipeline using:

GitHub → Azure App Service Deployment Center

Whenever code is pushed to GitHub:

1. Azure automatically pulls latest code
2. Dependencies are installed
3. Application is redeployed automatically

This simulates a real-world DevOps deployment workflow.

---

# 📊 Project Workflow

## Step 1

User adds website URL from dashboard.

## Step 2

Website data is stored inside Azure PostgreSQL database.

## Step 3

APScheduler automatically checks websites periodically.

## Step 4

Application measures:

* Website status
* Response time
* Uptime percentage

## Step 5

Monitoring logs are stored in Azure PostgreSQL.

## Step 6

If website becomes DOWN:

* Telegram alert is triggered instantly.

## Step 7

Dashboard displays:

* Monitoring analytics
* Logs
* Website uptime status

---

# 📸 Dashboard Features

✅ Add Websites
✅ Delete Websites
✅ Real-Time Monitoring
✅ Response Time Graphs
✅ Uptime Analytics
✅ Monitoring Logs
✅ Telegram Alerts
✅ Cloud Monitoring Dashboard

---

# ⚡ Local Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Uptime-monitor.git
cd Uptime-monitor
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

# 🔐 Environment Variables

Create `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

DB_HOST=your_azure_postgresql_host
DB_NAME=postgres
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

---

# 📈 Future Improvements

* Email Notifications
* SMS Alerts
* AI-Based Downtime Prediction
* Docker Containerization
* Kubernetes Deployment
* Multi-user Authentication
* Public Status Page
* SLA Reporting
* SSL Monitoring

---

# 🧠 Learning Outcomes

This project helped in understanding:

✅ Azure Cloud Deployment
✅ Flask Backend Development
✅ PostgreSQL Cloud Database
✅ CI/CD Deployment
✅ Monitoring Systems
✅ Cloud Networking
✅ Automation Scheduling
✅ Real-Time Alert Systems
✅ Application Monitoring
✅ Production Deployment Workflow

---

# 👨‍💻 Author

## Abhay Shukla

Cloud & Backend Developer
Azure | Python | Flask | PostgreSQL | DevOps | Monitoring Systems

---

# ⭐ Resume Highlights

* Built and deployed a cloud-based uptime monitoring platform using Microsoft Azure.
* Integrated Azure PostgreSQL Flexible Server with Flask backend.
* Implemented automatic monitoring scheduler using APScheduler.
* Added Telegram alert system for real-time downtime notifications.
* Configured Azure Application Insights for monitoring and analytics.
* Implemented CI/CD deployment using GitHub and Azure App Service.
* Designed real-time uptime analytics dashboard with monitoring logs.
