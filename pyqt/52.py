# Завдання 2. Вибір файлу
# Умова: додати кнопку, при натисканні на яку відкривається діалог вибору файлу і виводиться обраний шлях у QLabel.# # 
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton("push me")
label = QLabel()

def veryCoolFuction():
    file, _ = QFileDialog.getOpenFileName(window, "pick a file or something idk", '', "Flipchart archive (*.flipchart);;All Files(*.*)")
    label.setText(file)

layout.addWidget(button)
layout.addWidget(label)
button.clicked.connect(veryCoolFuction)

window.setLayout(layout)
window.show()
app.exec_()