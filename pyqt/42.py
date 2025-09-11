# Завдання: Простий лічильник із меню і панеллю інструментів
# Умови:
# Вікно на основі QMainWindow.
# В центрі — QLabel, який показує число (початково 0).
# Меню "Дії" з пунктами:
# Збільшити — збільшує число на 1
# Зменшити — зменшує число на 1
# Скинути — скидає число до 0
# Вихід — закриває програму
# Панель інструментів з кнопками для Збільшити, Зменшити і Скинути (текст або іконки).
# Гарячі клавіші:
# Збільшити — Ctrl+Up
# Зменшити — Ctrl+Down
# Скинути — Ctrl+R
# Вихід — Ctrl+Q
# Підказки (StatusTip) для кожної дії, що відображаються внизу у рядку стану.

from PyQt5.QtWidgets import *

app = QApplication([])
window = QMainWindow()
window.resize(1280, 720)
menu = window.menuBar()
toolbar = window.addToolBar("Bar")
status_bar = window.statusBar()
global number
number = 0
lable = QLabel(f"{number}", window)
inc = QAction("Increase", window)
dec = QAction("Decrease", window)
res = QAction("Reset", window)
ext = QAction("Quit", window)

inc.setShortcut("Ctrl+Up")
dec.setShortcut("Ctrl+Down")
res.setShortcut("Ctrl+R")
ext.setShortcut("Ctrl+Q")

toolbar.addActions({inc, dec, res, ext})

lable.setGeometry(640, 360, 50, 50)
lable.setStyleSheet('font-size: 30px;')

def addOne():
    global number
    number += 1
    lable.setText(f"{number}")
def removeOne():
    global number
    number -= 1
    lable.setText(f"{number}")
def reset():
    global number
    number = 0
    lable.setText(f"{number}")
def exit():
    app.quit()

inc.triggered.connect(addOne)
dec.triggered.connect(removeOne)
res.triggered.connect(reset)
ext.triggered.connect(exit)

window.show()
app.exec_()