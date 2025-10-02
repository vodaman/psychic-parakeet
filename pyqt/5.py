#Робота з діалоговими вікнами в PyQt5

#1. QMessageBox – повідомлення, підтвердження, попередження
#Використання:
#повідомити користувача (інформація, помилка, попередження);
#запитати підтвердження (Yes / No).
#Типи вбудованих повідомлень:
#QMessageBox.information() – звичайне інформування;
#QMessageBox.warning() – попередження;
#QMessageBox.critical() – помилка;
#QMessageBox.question() – питання з кнопками.
#Кнопки:
#QMessageBox.Yes, QMessageBox.No, QMessageBox.Ok, QMessageBox.Cancel.
#from PyQt5.QtWidgets import *
#app = QApplication([])
#window = QWidget()
#result = QMessageBox.question(window, 'Exit', 'Do u really wanna exit?', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)

#2. QFileDialog – вибір файлів і папок
#Для чого потрібен?
#Вибрати існуючий файл;
#Вибрати шлях і назву для збереження файлу;
#Вибрати цілу папку.
#Методи:
#getOpenFileName() – вибрати файл для відкриття;
#getSaveFileName() – вибрати шлях для збереження файлу;
#getExistingDirectory() – вибрати папку.
#from PyQt5.QtWidgets import *
#app = QApplication([])
#window = QWidget()
#file, _ = QFileDialog.getOpenFileName(window, 'Pick an image', '', 'Images (*.png *.jpg);;All files (*.*)')

#3. QColorDialog – вибір кольору
#Для чого потрібен?
#Змінити фон, колір тексту або інші кольорові параметри.
#Метод:
#QColorDialog.getColor() – відкриває палітру.
#Результат:
#Повертає об’єкт QColor.
#Перевіряємо, чи користувач натиснув "Ок":
#from PyQt5.QtWidgets import *
#app = QApplication([])
#window = QWidget()
#color = QColorDialog.getColor()
#if color.isValid():
#    print('picked color:', color.name())

#4. QFontDialog – вибір шрифту
#Для чого потрібен?
#Дає змогу користувачу змінити стиль і розмір шрифту.
#Метод:
#QFontDialog.getFont() – відкриває вікно вибору шрифтів.
#Результат:
#Повертає кортеж (QFont, bool) де bool = чи натиснув користувач "Ок".
#from PyQt5.QtWidgets import *
#app = QApplication([])
#window = QWidget()
#font, ok = QFontDialog.getFont()
#if ok:
#    pass

#5. QInputDialog – швидке введення даних
#Використання:
#Ввести текст, число, вибрати зі списку.
#Методи:
#getText() – вводимо текст;
#getInt() – вводимо число;
#getItem() – вибір зі списку.
#from PyQt5.QtWidgets import *
#app = QApplication([])
#window = QWidget()
#text, ok = QInputDialog.getText(window, 'Enter a name', 'Name:')
#if ok:
#    print('ur name:', text)

# Завдання 1. Повідомлення користувачу
# Умова: створити вікно з кнопкою, при натисканні на яку з'являється повідомлення "Привіт"

from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
button = QPushButton("Click me")
layout = QVBoxLayout()

def buton():
   result = QMessageBox.information(window, "hello", "hello") 

layout.addWidget(button)

button.clicked.connect(buton)

window.setLayout(layout)
window.show()
app.exec_()