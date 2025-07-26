from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout,
                             QDateTimeEdit, QSpacerItem, QHBoxLayout,
                             QLineEdit, QTextEdit, QSizePolicy, QPushButton)
import sys
from PyQt6.QtCore import QDateTime



class ReminderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Reminder")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        #Event date and time
        self.datetime_label = QLabel("Event Date and Time")
        self.datetime_picker = QDateTimeEdit()
        self.datetime_picker.setDateTime(QDateTime.currentDateTime())
        self.datetime_picker.setCalendarPopup(True)
        layout.addWidget(self.datetime_label)
        layout.addWidget(self.datetime_picker)

        #Email
        self.email_label = QLabel("Email: ")
        self.email_input = QLineEdit("vkumar080@rku.ac.in")
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        #Reminder
        self.reminder_label = QLabel("Reminder: ")
        self.reminder_input = QTextEdit()
        layout.addWidget(self.reminder_label)
        layout.addWidget(self.reminder_input)

        #Repeat interval
        self.repeat_label = QLabel("Repeat Interval: ")
        self.repeat_input = QLineEdit()
        self.repeat_input.setPlaceholderText("e.g., 1d, 2w, 3m")
        layout.addWidget(self.repeat_label)
        layout.addWidget(self.repeat_input)

        ##Button_layout
        button_layout = QHBoxLayout()
        self.submit_button = QPushButton("Add Reminder")
        self.close_button = QPushButton("Close")
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.close_button)
        layout.addLayout(button_layout)


        layout.addSpacerItem(QSpacerItem(20, 40,
                                         QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))
        self.setLayout(layout)

app = QApplication(sys.argv)
window = ReminderApp()
window.show()
sys.exit(app.exec())