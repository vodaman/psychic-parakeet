# Завдання 4: Перемикання між двома звуками
# Умова: Зробити дві кнопки. Одна запускає звук1, друга — звук2. Гравець може вибирати який звук почути.

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))
soundOne = QPushButton("Play sound 1")
soundTwo = QPushButton("Play sound 2")

def s1():
    player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))
    player.play()

def s2():
    player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/psychic-parakeet/pyqt/67.mp3")))
    player.play()

soundOne.clicked.connect(s1)
soundTwo.clicked.connect(s2)

layout.addWidget(soundOne)
layout.addWidget(soundTwo)

window.setLayout(layout)
window.show()
app.exec_()