# Завдання 2: Робота з таблицею
# Умова:
# Створити програму, яка:
# Має таблицю на 3 стовпці (Ім'я, Вік, Місто).
# Дозволяє додати новий рядок із введеними даними.
# Виводить дані вибраного рядка в QLabel.

from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
table = QTableWidget()
nameLineEdit = QLineEdit()
ageLineEdit = QLineEdit()
citySkyLineEdit = QLineEdit()
addButton = QPushButton("Add")
outputLabel = QLabel("Your info will be here...")
layout = QVBoxLayout()
lineEditLayout = QHBoxLayout()

window.resize(500,400)
window.setWindowTitle("lesoon 2")

table.setColumnCount(3)
table.setRowCount(0)
table.setHorizontalHeaderLabels(["name", "age", "city"])
nameLineEdit.setPlaceholderText("Enter your name")
ageLineEdit.setPlaceholderText("Enter your age")
citySkyLineEdit.setPlaceholderText("Enter your city")

def addNewRow():
    rowCount = table.rowCount()
    table.insertRow(rowCount)
    table.setItem(rowCount, 0, QTableWidgetItem(nameLineEdit.text()))
    table.setItem(rowCount, 1, QTableWidgetItem(ageLineEdit.text()))
    table.setItem(rowCount, 2, QTableWidgetItem(citySkyLineEdit.text()))
    nameLineEdit.clear()
    ageLineEdit.clear()
    citySkyLineEdit.clear()

def outToLabel():
    row = table.currentRow()
    if row != -1:
        listWithAllTheData = []
        for column in range(3):
            listWithAllTheData.append(table.item(row, column).text())
        outputLabel.setText(f"{listWithAllTheData[0]}, {listWithAllTheData[1]}, {listWithAllTheData[2]}")

addButton.clicked.connect(addNewRow)
table.itemSelectionChanged.connect(outToLabel)

lineEditLayout.addWidget(nameLineEdit)
lineEditLayout.addWidget(ageLineEdit)
lineEditLayout.addWidget(citySkyLineEdit)

layout.addWidget(table)
layout.addLayout(lineEditLayout)
layout.addWidget(addButton)
layout.addWidget(outputLabel)

window.setLayout(layout)

window.show()
app.exec_()