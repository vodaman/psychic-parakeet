# Завдання 5. Повідомлення при натисканні кнопок
# Умова:
# Створіть вікно з 3 кнопками:
# Інформація – показує QMessageBox.information.
# Попередження – показує QMessageBox.warning.
# Помилка – показує QMessageBox.critical.

from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

info = QPushButton("Show info message")
warn = QPushButton("Show warning message")
crit = QPushButton("Show critical message")

def showInfo():
    result = QMessageBox.information(window, "info", "You got the information box")
def showWarn():
    result = QMessageBox.warning(window, "warn", "You got the warning box")
def showCrit():
    result = QMessageBox.critical(window, "crit", "You got the critical box")

info.clicked.connect(showInfo)
warn.clicked.connect(showWarn)
crit.clicked.connect(showCrit)

layout.addWidget(info)
layout.addWidget(warn)
layout.addWidget(crit)

window.setLayout(layout)
window.show()
app.exec_()