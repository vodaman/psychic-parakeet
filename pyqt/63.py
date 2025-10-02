# Завдання 5:
# Створити інтерфейс PyQt5 з кнопкою для запуску музики та повзунком для зміни гучності в реальному часі.
# Додай ще один повзунок, який буде керувати швидкістю відтворення.
# player.setPlaybackRate(value / 100)

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

def changeSpeed(value):
    player.setPlaybackRate(value / 100)

button = QPushButton()

player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))

volumeSlider = QSlider(Qt.Vertical) # type: ignore
volumeSlider.setRange(0,100)
volumeSlider.setValue(67)

playbackSlider = QSlider(Qt.Vertical)
volumeSlider.setRange(1,100)
volumeSlider.setValue(100)

volumeSlider.valueChanged.connect(player.setVolume)
playbackSlider.valueChanged.connect(changeSpeed)
button.clicked.connect(player.play)

layout.addWidget(volumeSlider)
layout.addWidget(playbackSlider)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()