# Завдання 4: Створити вікно з кнопкою, яка відкриває вибір файлу і відображає розмір файлу у байтах у QLabel.
# Додати кнопку "Вибрати шрифт" за допомогою QFontDialog і застосувати вибраний шрифт до тексту в QLabel.
# Зробити програму, де користувач обирає колір тексту і шрифт для свого повідомлення.
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
fontButton = QPushButton("Pick a font")
colorButton = QPushButton("Pick a color")
label = QLabel("Label")
global messageFont
global messageColor

def getFont():
    font, ok = QFontDialog.getFont()
    if ok:
        global messageFont
        messageFont = font
        label.setFont(messageFont)

def getColor():
    color = QColorDialog.getColor()
    if color.isValid():
        label.setStyleSheet(f"background-color: {color.name()}")
        global messageColor
        messageColor = color

layout.addWidget(fontButton)
layout.addWidget(colorButton)
layout.addWidget(label)
fontButton.clicked.connect(getFont)
colorButton.clicked.connect(getColor)

window.setLayout(layout)
window.show()
app.exec_()