# Завдання: Зміна кольору фону
# Умови:
# Програма на основі QMainWindow.
# У центрі — QLabel з написом "Оберіть колір".
# Меню "Кольори" з пунктами:
# Червоний
# Зелений
# Синій
# Скинути (повертає білий фон і напис "Оберіть колір").
# Панель інструментів з кнопками для Червоний, Зелений, Синій, Скинути.
# Гарячі клавіші:
# Червоний — Ctrl+1
# Зелений — Ctrl+2
# Синій — Ctrl+3
# Скинути — Ctrl+0
# У рядку стану (status bar) відображається підказка при наведенні на дію.

from PyQt5.QtWidgets import *

app = QApplication([])
window = QMainWindow()
label = QLabel("Pick a color", window)
menu = window.menuBar()
toolBar = window.addToolBar("Bar")
statusBar = window.statusBar()

red = QAction("R E D", window)
green = QAction("green", window)
blue = QAction("blue", window)
res = QAction("reset", window)

red.setShortcut("Ctrl+1")
green.setShortcut("Ctrl+2")
blue.setShortcut("Ctrl+3")
res.setShortcut("Ctrl+0")

label.setGeometry(100,100,250,50)

toolBar.addActions({red, green, blue, res})

def tored():
    window.setStyleSheet("background-color: red;")
def togreen():
    window.setStyleSheet("background-color: green;")
def toblue():
    window.setStyleSheet("background-color: blue;")
def reset():
    window.setStyleSheet("background-color: white;")

red.triggered.connect(tored)
green.triggered.connect(togreen)
blue.triggered.connect(toblue)
res.triggered.connect(reset)

red.setStatusTip("the world is your canvas so take your brush and paint the world  R E D.")
green.setStatusTip("Set the background to green")
blue.setStatusTip("Set the background to blue")
res.setStatusTip("Reset the background")

window.show()
app.exec_()