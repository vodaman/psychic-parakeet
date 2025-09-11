from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
table = QTableWidget()
nameLineEdit = QLineEdit()
classLineEdit = QLineEdit()
gradeLineEdit = QLineEdit()
addButton = QPushButton("Add")
outputLabel = QLabel("Your info will be here...")
layout = QVBoxLayout()

window.resize(500,400)
window.setWindowTitle("lesoon 2")
gradeLineEdit.setPlaceholderText("Add grades here by comma or space (1,2 or 1 2)")

table.setColumnCount(4)
table.setRowCount(0)
table.setHorizontalHeaderLabels(["name", "class", "grade", "gpa"])

def addNewRow():
    rowCount = table.rowCount()
    if "," in gradeLineEdit.text():
        grades = gradeLineEdit.text().split(",")
    else:
        grades = gradeLineEdit.text().split()
    grades_int = [int(eger) for eger in grades]
    gpa = sum(grades_int) / len(grades_int)
    table.insertRow(rowCount)
    table.setItem(rowCount, 0, QTableWidgetItem(nameLineEdit.text()))
    table.setItem(rowCount, 1, QTableWidgetItem(classLineEdit.text()))
    table.setItem(rowCount, 2, QTableWidgetItem(gradeLineEdit.text()))
    table.setItem(rowCount, 3, QTableWidgetItem(str(gpa)))
    nameLineEdit.clear()
    classLineEdit.clear()
    gradeLineEdit.clear()

def outToLabel():
    row = table.currentRow()
    if row != -1:
        listWithAllTheData = []
        for column in range(4):
            listWithAllTheData.append(table.item(row, column).text())
        outputLabel.setText(f"{listWithAllTheData[0]}, {listWithAllTheData[1]}, {listWithAllTheData[2]}")

addButton.clicked.connect(addNewRow)
table.itemSelectionChanged.connect(outToLabel)

layout.addWidget(table)
layout.addWidget(nameLineEdit)
layout.addWidget(classLineEdit)
layout.addWidget(gradeLineEdit)
layout.addWidget(addButton)
layout.addWidget(outputLabel)

window.setLayout(layout)
window.show()
app.exec_()