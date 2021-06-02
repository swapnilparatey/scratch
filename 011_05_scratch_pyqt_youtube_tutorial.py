# YouTube PyQt tutorial - https://www.youtube.com/watch?v=fqK8N48kPXs&list=PLA955A8F9A95378CE&index=2
# More details at - https://stackoverflow.com/questions/58661539/create-splash-screen-in-pyqt5 - check Example 2
# Splash Screen

import sys
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"

    if len(sys.argv) < 2:
        raise ValueError

    hours, minutes = sys.argv[1].split(":")
    due = QTime(int(hours), int(minutes))

    if not due.isValid():
        raise ValueError

    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

except ValueError:
    message = "Usage: python.exe <filename>.py HH:MM <optional message>"


while QTime.currentTime() < due:
    sleep(10)

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
label.show()

QTimer.singleShot(20000, app.quit)
app.exec_()