#Меню та панель інструментів (QMenuBar, QToolBar)
#Що таке QMainWindow і чому ми його використовуємо?
#У PyQt5 є два основні типи вікон:
#QWidget – базове просте вікно (без додаткових можливостей).
#QMainWindow – спеціальне вікно, яке дозволяє:
#додати меню (menuBar),
#додати панель інструментів (toolBar),
#додати рядок стану (statusBar) – місце для підказок і повідомлень.
#Висновок: для програм із меню, кнопками швидкого доступу та підказками використовуємо QMainWindow.


#Меню (QMenuBar)
#Меню у верхній частині вікна (приклад: Файл, Правка, Довідка).
#У PyQt5 його створюють методом:
#menu_bar = window.menuBar()
#Додати в меню категорію (наприклад, Файл):
#file_menu = menu_bar.addMenu("Файл")
#У категорії меню можуть бути дії (QAction):
#action_open = QAction("Відкрити", window)
#file_menu.addAction(action_open)

#Панель інструментів (QToolBar)
#Це горизонтальна або вертикальна панель із кнопками.
#У ній повторюються часто потрібні дії з меню (наприклад, Зберегти, Відкрити, Вихід).
#Створення в PyQt5:
#toolbar = window.addToolBar("Головна панель")
#toolbar.addAction(action_open)

#Дії (QAction)
#QAction — це "опис команди" для програми.
#Може містити:
#Текст (назва)
#Іконку
#Гарячу клавішу
#Підказку (tooltip)
#Може використовуватись одночасно і в меню, і на панелі інструментів:
#open_action = QAction("Відкрити", window)
#open_action.setShortcut("Ctrl+O")
#open_action.setStatusTip("Відкрити файл")
#open_action.triggered.connect(open_file)

# Завдання 1: Меню з пунктами "Відкрити" та "Вихід"
# Очікуваний результат:
# Меню "Файл" із двома пунктами.
# Натискання на "Вихід" закриває програму.
# Натискання на "Відкрити" виводить у консоль "Відкриття файлу...".

# Завдання 2: Панель інструментів із кнопкою "Відкрити"
# Очікуваний результат:
# Тепер у вікні є панель інструментів (з кнопками "Відкрити" та "Вихід").
# Кнопки роблять те саме, що й пункти меню.

# Завдання 3: Гарячі клавіші та підказки
# Очікуваний результат:
# Працюють гарячі клавіші Ctrl+O і Ctrl+Q.
# Коли наводимо мишку на кнопку або пункт меню, внизу (status bar) показується підказка.

from PyQt5.QtWidgets import *

app = QApplication([])
window = QMainWindow()
menu = window.menuBar()
fileMenu = menu.addMenu("File")
exit = QAction("Exit", window)
open = QAction("Open nothing (yet)", window)
toolbar = window.addToolBar("Bar")
toolbar.addActions([exit, open])
status_bar = window.statusBar()

def quit(): # why are you reading this...
    app.quit()
def opeen():
    print("Opening file...")

exit.setShortcuts(["Ctrl+W", "Ctrl+Q"])
open.setShortcut("Ctrl+O")
exit.setStatusTip("Contrary to popular belief, this is the exit button.")
open.setStatusTip("Unbelivabely, this opens.")

exit.triggered.connect(quit)
open.triggered.connect(opeen)

fileMenu.addActions([exit, open])

window.show()
app.exec_()