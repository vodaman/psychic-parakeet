# Завдання 4: Динамічне додавання вкладок
# Мета: Навчитись створювати вкладки під час роботи програми.
# Створити одну вкладку "Головна".
# Додати кнопку "Нова вкладка".
# При натисканні:
# Додається нова вкладка з унікальним номером (Вкладка 1, Вкладка 2…).
# У цій вкладці розмістити напис "Вміст вкладки N".
# Додати кнопку "Видалити активну вкладку".
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
tabs = QTabWidget()
mainTab = QWidget()
mainTabLabel = QLabel("Nowa wkladka")
mainTabLayout = QVBoxLayout()
newTabButton = QPushButton("Nowa wkladka")
removeButton = QPushButton("Wydality Aktiwny wkladku")

mainTabLayout.addWidget(mainTabLabel)
mainTab.setLayout(mainTabLayout)
tabs.addTab(mainTab, "Golowna wkladka")

def addTab():
    newTab = QWidget()
    count = tabs.count()
    newTabLabel = QLabel(f"Wmist Wkladky {count}")
    newTabLayout = QVBoxLayout()
    newTabLayout.addWidget(newTabLabel)
    newTab.setLayout(newTabLayout)
    tabs.addTab(newTab, f"Wkladka {count}")

def removeTab():
    index = tabs.currentIndex()
    if index == 0:
        return
    else:
        tabs.removeTab(index)

layout.addWidget(tabs)
layout.addWidget(newTabButton)
layout.addWidget(removeButton)

newTabButton.clicked.connect(addTab)
removeButton.clicked.connect(removeTab)
layout.addWidget(tabs)
window.setLayout(layout)
window.show()
app.exec_()