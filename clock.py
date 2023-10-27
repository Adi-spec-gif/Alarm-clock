import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer, QTime

class AlarmClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Alarm Clock")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Set Alarm Time (HH:MM AM/PM)")
        self.layout.addWidget(self.label)

        self.alarm_time_input = QLineEdit()
        self.layout.addWidget(self.alarm_time_input)

        self.set_alarm_button = QPushButton("Set Alarm")
        self.set_alarm_button.clicked.connect(self.set_alarm)
        self.layout.addWidget(self.set_alarm_button)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_alarm)
        self.timer.start(100000)  # Check the alarm every second

    def set_alarm(self):
        alarm_time = self.alarm_time_input.text()
        self.alarm_time = QTime.fromString(alarm_time, "h:mm AP")

    def check_alarm(self):
        current_time = QTime.currentTime()
        if current_time == self.alarm_time:
            QMessageBox.information(self, "Alarm", "Time to wake up!")
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = AlarmClock()
    clock.show()
    sys.exit(app.exec_())
