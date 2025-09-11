# Завдання 3: Закриття та переміщення вкладок
# Мета: Використати setTabsClosable(), setMovable(), removeTab().
# Створити 4 вкладки з різними текстами.
# Додати можливість:
# Закривати вкладку по кліку на "хрестик".
# Перетягувати вкладки мишкою.
# Якщо користувач app = QApplication([]) закрив останню вкладку, додати автоматично нову з текстом "Порожньо".
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
tabs = QTabWidget()
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()
tab4 = QWidget()
tab1Layout = QVBoxLayout()
tab2Layout = QVBoxLayout()
tab3Layout = QVBoxLayout()
tab4Layout = QVBoxLayout()
label = QLabel("Odin label na wse tomu szo optimizacja :)")

tab1Layout.addWidget(label)
tab2Layout.addWidget(label)
tab2Layout.addWidget(label)
tab2Layout.addWidget(label)
tab1.setLayout(tab1Layout)
tab2.setLayout(tab2Layout)
tab3.setLayout(tab3Layout)
tab4.setLayout(tab4Layout)
tabs.addTab(tab1, "tab 1")
tabs.addTab(tab2, "tab 2")
tabs.addTab(tab3, "tab 3")
tabs.addTab(tab4, "tab 4")

tabs.setTabsClosable(True)
tabs.setMovable(True)

def closeTab(index):
    tabs.removeTab(index)
    if tabs.count() == 0:
        empty = QWidget()
        emptyLabel = QLabel("now im all alone :(")
        emptyLayout = QVBoxLayout()
        emptyLayout.addWidget(emptyLabel)
        empty.setLayout(emptyLayout)
        tabs.addTab(empty, "all alone.")

tabs.tabCloseRequested.connect(closeTab)

layout.addWidget(tabs)
window.setLayout(layout)
window.show()
app.exec_()