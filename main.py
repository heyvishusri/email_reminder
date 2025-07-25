import csv
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
import  dateutil.relativedelta as relativedelta

def load_credentials():
    load_dotenv()
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    return email_address, email_password


def load_reminders(filepath = "reminders.csv"):
    with open(filepath) as file:
        reader = csv.DictReader(file)
        reminders = list(reader)
        return reminders


def login_to_email(email_address,email_password):
    smtp= smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(email_address,email_password)
    return smtp


def create_email(r):
    msg = EmailMessage()
    msg['subject'] = "⏰ Your reminder for Today"
    msg['From'] = "Vishwash Kumar"
    msg['To'] = r['email']
    msg.set_content(f"Message: {r['message']}\n"
                    f"Date: {r['date']}\n"
                    f"Time: {r['time']}")
    return msg

def save_reminders(remaining):
    with open("reminders.csv", "w") as file:
        writer = csv.DictWriter(file,
                                fieldnames=["date", "time", "email", "message","repeat_interval"])
        writer.writeheader()
        writer.writerows(remaining)

def calculate_next_date(date_str, repeat_interval):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    unit = repeat_interval[-1]
    value = int(repeat_interval[:-1])
    if unit == 'm':
        next_date = date + relativedelta.relativedelta(months=value)
    if unit == 'w':
        next_date = date + relativedelta.relativedelta(weeks=value)
    if unit == 'd':
        next_date = date + relativedelta.relativedelta(days=value)
    return  next_date.strftime('%Y-%m-%d')



reminders = load_reminders()
today  = datetime.now().strftime("%Y-%m-%d")
remaining = []

email_address, email_password = load_credentials()

smtp = login_to_email(email_address,email_password)
for r in reminders:
    if r['date'] == today:
        msg = create_email(r)
        smtp.send_message(msg)
        if r.get('repeat_interval'):
            next_date = calculate_next_date(r['date'], r['repeat_interval'])
            r['date'] = next_date
            remaining.append(r)
    else:
        remaining.append(r)




save_reminders(remaining)