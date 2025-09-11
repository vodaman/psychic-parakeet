#Основні можливості QTabWidget
#addTab(widget, "Назва") — додає вкладку.
#insertTab(index, widget, "Назва") — вставляє вкладку на потрібну позицію.
#removeTab(index) — видаляє вкладку.
#setCurrentIndex(index) — перемикає на вкладку за індексом.
#currentIndex() — повертає номер активної вкладки.
#setTabText(index, "Новий текст") — змінює назву вкладки.
#setTabsClosable(True) — додає кнопку "хрестик" для закриття вкладок.
#setMovable(True) — дозволяє перетягувати вкладки.

#Структура роботи з QTabWidget
#Створити QTabWidget.
#Для кожної вкладки створити віджет (наприклад, QWidget або інший контейнер).
#Додати в цей віджет елементи інтерфейсу (QLabel, QLineEdit, QPushButton тощо).
#Додати вкладку до QTabWidget.
# Завдання 1: Створення власних вкладок
# Мета: Закріпити базові методи addTab(), setTabText(), setCurrentIndex().
# Створити вікно з трьома вкладками:
# Перша: текст "Вітаю у першій вкладці".
# Друга: текст "Тут друга вкладка".
# Третя: текст "А це третя".
# Додати кнопку, яка при натисканні перемикає на другу вкладку.
# Змінити назву третьої вкладки на "Оновлена".
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
line = QVBoxLayout()
window.resize(500, 500)
tabs = QTabWidget()
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()
tab1_layout = QVBoxLayout()
tab2_layout = QVBoxLayout()
tab3_layout = QVBoxLayout()
label1 = QLabel('witayu u pershiy wkladci')
label2 = QLabel('tut druga wkladka')
label3 = QLabel('a tse tretia')
button = QPushButton("Knopka")

tab1_layout.addWidget(label1)
tab1.setLayout(tab1_layout)
tabs.addTab(tab1, 'First tab')
tab2_layout.addWidget(label2)
tab2.setLayout(tab2_layout)
tabs.addTab(tab2, 'Second tab')
tab3_layout.addWidget(label3)
tab3.setLayout(tab3_layout)
tabs.addTab(tab3, 'Third tab')

def buttondoessomething():
    tabs.setCurrentIndex(1)
    tabs.setTabText(2, "Onowlena")

button.clicked.connect(buttondoessomething)
line.addWidget(tabs)
line.addWidget(button)
window.setLayout(line)

window.show()
app.exec_()
