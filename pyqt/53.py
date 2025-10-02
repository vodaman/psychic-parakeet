# Завдання 3. Вибір кольору
# Умова: при натисканні кнопки відкривається вікно вибору кольору, і обраний колір змінює фон QLabel.
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton("push me")
label = QLabel("Label")

def veryCoolFuction():
    color = QColorDialog.getColor()
    if color.isValid():
        label.setStyleSheet(f"background-color: {color.name()}")

layout.addWidget(button)
layout.addWidget(label)
button.clicked.connect(veryCoolFuction)

window.setLayout(layout)
window.show()
app.exec_()