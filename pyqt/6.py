#Робота зі звуками в PyQt5
#1. Підключення модуля звуку
#У PyQt5 використовується модуль QMediaPlayer з бібліотеки PyQt5.QtMultimedia.
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QFileInfo
#QMediaPlayer — головний клас для відтворення аудіо.
#QMediaContent — клас, що представляє медіафайл.

#Відтворення звуку
#player = QMediaPlayer()
#player.setMedia(QMediaContent(QUrl.fromLocalFile("sound.mp3")))
#player.play()

#Основні методи QMediaPlayer
#| Метод           | Опис                        |
#| --------------- | --------------------------- |
#| `play()`        | Відтворити звук             |
#| `pause()`       | Поставити на паузу          |
#| `stop()`        | Зупинити                    |
#| `setVolume(50)` | Встановити гучність (0–100) |

#Керування гучністю звуку в PyQt5 за допомогою повзунка (QSlider)
#slider = QSlider(Qt.Horizontal)
#slider.setRange(0, 100)
#slider.setValue(50)
#slider.valueChanged.connect(player.setVolume)

# Завдання 1: Відтворити звук по натисканню кнопки
# Умова: Створити просту програму з кнопкою "Грати", яка запускає mp3-файл.

# Завдання 2: Додати кнопки «Пауза» та «Стоп»
# Умова: Розширити попередню програму, додавши ще дві кнопки — «Пауза» та «Стоп».

from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

play = QPushButton("Play")
pause = QPushButton("Pause")
stop = QPushButton("Stop")
player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/Donathan Joe/psychic-parakeet/pyqt/67.mp3")))
player.setVolume(67)
play.clicked.connect(player.play)
pause.clicked.connect(player.pause)
stop.clicked.connect(player.stop)

layout.addWidget(play)
layout.addWidget(pause)
layout.addWidget(stop)

window.setLayout(layout)
window.show()
app.exec_()