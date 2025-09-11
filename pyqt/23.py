# Завдання 3. Подвійний список
# Умова:
# Створити два QListWidget. У першому — "Доступні продукти", у другому — "Кошик". При кліку на елемент першого списку він переноситься у другий.
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
list1 = QListWidget()
list2 = QListWidget()
add = QPushButton("Add")
remove = QPushButton("Remove")
edit = QLineEdit()
edit.setPlaceholderText("Enter your item")
layout = QVBoxLayout()


window.resize(300, 400)
window.setWindowTitle("Ultra Shopping List")

list1.addItems(["mangoes", "apples", "juice", "rocks"])

def addElement():
    item = list1.currentItem().text()
    print(item)
    list2.addItem(item)

list1.itemClicked.connect(addElement)

layout.addWidget(list1)
layout.addWidget(list2)

window.setLayout(layout)
window.show()
app.exec_()