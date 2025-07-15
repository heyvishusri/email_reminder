import csv
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

# print(email_address)
# print(email_password)


with open("reminders.csv") as file:
    reader = csv.DictReader(file)
    reminders = list(reader)


# print(reminders)
remaining = []
for r in reminders:
    if r['date'] == datetime.now().strftime("%Y-%m-%d"):
        msg = EmailMessage()
        msg['subject'] = "⏰ Your reminder for Today"
        msg['From']  = "Vishwash Kumar"
        msg['To'] = r['email']
        msg.set_content(f"Message: {r['message']}\n"
                        f"Date: {r['date']}\n"
                        f"Time: {r['time']}")
        # print(msg)
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(email_address,email_password)
            smtp.send_message(msg)
    else:
        remaining.append(r)

print(remaining)

with open("reminders.csv", "w") as file:
    writer = csv.DictWriter(file,
                            fieldnames=["date", "time", "email", "message"])
    writer.writeheader()
    writer.writerows(remaining)
