from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import *
import time

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

def changeSpeed(value):
    player.setPlaybackRate(value / 100)

button = QPushButton()
global timer

player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))

player2 = QMediaPlayer()
player2.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/Downloads/hello-moto-sound-notification.mp3")))

p1s = QSlider(Qt.Vertical) 
p1s.setRange(0,100)
p1s.setValue(100)

p2s = QSlider(Qt.Vertical)
p2s.setRange(1,100)
p2s.setValue(100)

def start():
   player.play()
   global timer
   timer = time.time()
   while True:
       pass

p1s.valueChanged.connect(player.setVolume)
p2s.valueChanged.connect(player2.setVolume)
button.clicked.connect(player.play)

layout.addWidget(p1s)
layout.addWidget(p2s)
layout.addWidget(button)



window.setLayout(layout)
window.show()
app.exec_()