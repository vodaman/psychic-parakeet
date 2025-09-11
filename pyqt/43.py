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
label = QLabel("Pick a color")
menuBar = QMenuBar()
statusBar = window.addst

window.show()
app.exec_()