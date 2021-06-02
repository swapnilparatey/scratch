# https://www.youtube.com/watch?v=0vvb7Kv59qA&list=PLA955A8F9A95378CE&index=3
# Expression evaluator - basically take a text and then do something with it

import sys
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None)
        super(Form, self).__init__(parent)
        # WTFF is this ^^ - https://stackoverflow.com/questions/29173299/super-init-vs-parent-init
        # Try this out later - for OOPS - super guarantees multiple inheritance in diamond structured inheritance

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type and press Enter")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        # ^ just remember ^ - don't completely trust the PyCharm editor OR syntax checker
        # https://stackoverflow.com/questions/27382053/where-is-the-connect-method-in-pyqt5 - for the connect thing
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()