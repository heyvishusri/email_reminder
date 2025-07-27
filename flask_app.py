from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = "/home/vishu9931/reminders.csv"

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "date", "time", "email", "message", "repeat_interval", "remind_days_before"
        ])
        writer.writeheader()

@app.route("/add", methods=["POST"])
def add_reminder():
    data = request.json

    required_fields = ["date", "time", "email", "message"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "date", "time", "email", "message", "repeat_interval"])
            writer.writerow({
                "date": data.get("date"),
                "time": data.get("time"),
                "email": data.get("email"),
                "message": data.get("message"),
                "repeat_interval": data.get("repeat_interval", "")
            })
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()