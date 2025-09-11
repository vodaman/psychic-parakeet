# Завдання 2: Додавання елементів у вкладки
# Мета: Використати QLineEdit, QPushButton, QLabel у вкладках.
# Створити 2 вкладки:
# "Ввід даних" — містить поле введення та кнопку "Вивести".
# При натисканні текст з поля з’являється під ним у QLabel.
# "Інформація" — містить статичний текст і кнопку "Закрити програму".
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
tabs = QTabWidget()
tab1 = QWidget()
tab2 = QWidget()
tab1Layout = QVBoxLayout()
tab2Layout = QVBoxLayout()
lineEditLabel = QLabel()
infoLabel = QLabel("Demonstracja wkladok w PyQt5\nSozdatel: kakoy to czel")
lineEdit = QLineEdit()
button = QPushButton("Dobawit info")
exitButton = QPushButton("Wiyty iz programmy")

window.resize(500,500)

tab1Layout.addWidget(lineEdit)
tab1Layout.addWidget(button)
tab1Layout.addWidget(lineEditLabel)
tab1.setLayout(tab1Layout)
tabs.addTab(tab1, "Dobawit kakie-to dannie")

tab2Layout.addWidget(infoLabel)
tab2Layout.addWidget(exitButton)
tab2.setLayout(tab2Layout)
tabs.addTab(tab2, "Informacja")

def addInfo():
    data = lineEdit.text()
    lineEditLabel.setText(data)

def exit():
    app.quit()

button.clicked.connect(addInfo)
exitButton.clicked.connect(exit)

layout.addWidget(tabs)

window.setLayout(layout)
window.show()
app.exec_()