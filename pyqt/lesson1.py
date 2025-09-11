from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
list_ = QListWidget()
add = QPushButton("Add")
remove = QPushButton("Remove")
edit = QLineEdit()
edit.setPlaceholderText("Enter your item")
label = QLabel("Shopping list")
layout = QVBoxLayout()


window.resize(300, 400)
window.setWindowTitle("Shopping List")

def addElement():
   editText = edit.text()
   if editText:
        list_.addItem(editText)
def removeElement():
    row = list_.currentRow()
    if row:
        list_.takeItem(row)

add.clicked.connect(addElement)
remove.clicked.connect(removeElement)

layout.addWidget(label)
layout.addWidget(list_)
layout.addWidget(add)
layout.addWidget(remove)
layout.addWidget(edit)

window.setLayout(layout)
window.show()
app.exec_()