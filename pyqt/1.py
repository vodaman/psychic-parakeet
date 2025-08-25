# Робота з таблицями та списками в PyQt5
#1. QListWidget
#Використовується для відображення списку елементів.
#Кожен елемент — це QListWidgetItem.
#Основні методи:
#addItem("текст") – додати елемент.
#takeItem(index) – видалити елемент за індексом.
#currentItem() – отримати вибраний елемент.
#Події: itemClicked.connect(function) – викликає функцію при кліку на елемент.

#2. QTableWidget
#Віджет для відображення таблиць.
#Основні властивості:
#setRowCount(n) – встановити кількість рядків.
#setColumnCount(n) – встановити кількість стовпців.
#setHorizontalHeaderLabels([...]) – встановити заголовки.
#Додавання даних:
#setItem(row, column, QTableWidgetItem("Текст")).
#Отримання даних:
#item(row, column).text().
#Події: itemSelectionChanged.connect(func)

# Завдання 1: Робота зі списком
# Умова:
# Створити програму, яка дозволяє:
# Додати текст, введений у QLineEdit, до QListWidget натисканням кнопки.
# Видаляти вибраний елемент.
# Виводити в QLabel текст вибраного елемента
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
list_ = QListWidget()
button = QPushButton("very button button")
alsoButton = QPushButton("not so very button button :(")
edit = QLineEdit()
edit.setPlaceholderText("i am a QLineEdit")
label = QLabel("Lable")
layout = QVBoxLayout()

window.resize(300, 400)
window.setWindowTitle("title")

def addElement():
   editText = edit.text()
   if editText:
        list_.addItem(editText)
def removeElement():
    row = list_.currentRow()
    if row:
        list_.takeItem(row)
def showElement(item):
      label.setText(item.text())  

button.clicked.connect(addElement)
alsoButton.clicked.connect(removeElement)
list_.itemClicked.connect(showElement)

layout.addWidget(list_)
layout.addWidget(button)
layout.addWidget(alsoButton)
layout.addWidget(edit)
layout.addWidget(label)

window.setLayout(layout)
window.show()
app.exec_()
