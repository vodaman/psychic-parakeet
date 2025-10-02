# Завдання 3: Звукове повідомлення після натискання кнопки
# Умова: Створити інтерфейс з кнопкою, яка при натисканні відтворює звук і відкриває повідомлення (QMessageBox).

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))
button = QPushButton("Play")

def showInfo():
    player.play()
    result = QMessageBox.information(window, "info", "You got the information box")

button.clicked.connect(showInfo)

layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()