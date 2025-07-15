# 📬 Email Reminder App – Real World Python Project

This project is part of the **Real World Python** Project. It demonstrates how to build a production-ready **Email Reminder Application** with scheduled and recurring notifications using Python, SMTP, and PyQt6.

🔗 **Repository**: [heyvishusri/email_reminder](https://github.com/heyvishusri/email_reminder)

## 🚀 Key Features
- 📅 Add **one-time** or **recurring** reminders (e.g., every 2 weeks, 3 months, etc.)
- 🖥️ GUI interface for easy input using **PyQt6**
- 📧 Automatic email notifications via **Gmail SMTP**
- ☁️ Remote storage of reminders in **CSV** via API (Flask + PythonAnywhere)
- 🔁 Daily cron job to send due reminders automatically

## 📁 Project Structure
📦 email_reminder_app/  
├── gui.py              → PyQt6 GUI to add reminders  
├── flask_app.py        → Flask API hosted on PythonAnywhere  
├── send_reminders.py   → Script to send reminders via cron (daily)  
├── reminders.csv       → Stores all reminder entries  
├── .env                → Gmail credentials (excluded from repo)

## 🛠️ Installation Guide

1. **Clone the repository**
   git clone https://github.com/heyvishusri/email_reminder.git
   cd email_reminder

3. **Create and activate a virtual environment**  
   Linux/macOS:
   
   python -m venv .venv
   
   source .venv/bin/activate

   Windows:
   
   .venv\Scripts\activate


3. **Install required dependencies**  
   pip install -r requirements.txt


4. **Create your `.env` file**  
   EMAIL_ADDRESS=yourgmail@gmail.com
   
   EMAIL_PASSWORD=your_app_password


6. **Run the GUI application**  
   python gui.py



## ⏰ Running the Daily Email Job

Deploy `send_reminders.py` to your [PythonAnywhere](https://www.pythonanywhere.com/) account.  
Schedule it using the built-in **Task Scheduler** (e.g., run daily at 8:00 AM IST).

This script will:
- Load the latest `reminders.csv`
- Check for due reminders
- Send email notifications automatically

## 🧠 Skills Learn

- Reading & writing **CSV files** in Python  
- Handling **datetime** and **recurrence** logic  
- Building desktop apps with **PyQt6**  
- Creating & consuming **REST APIs**  
- **Deploying Python applications** to the cloud (PythonAnywhere)

📫 Feel free to fork, star ⭐ the repo, and connect with me!  
If you encounter any issues or have suggestions, feel free to open an issue on the repo.

🔒 **Note**: This project uses Gmail SMTP. For security, always use an [App Password](https://support.google.com/accounts/answer/185833) instead of your main Gmail password.

## 📄 License

This project is licensed under the [MIT License](LICENSE).




