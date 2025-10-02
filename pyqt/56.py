from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button = QPushButton("Open file")
text = QTextEdit()

def veryCoolFuction():
    file, _ = QFileDialog.getOpenFileName(window, "pick a file or skomething idk", '', "Flipchart archive (*.flipchart);;All Files(*.*)", "",)
    with open(file, "r") as f:
        try:
            temp = f.read()
            text.setText(temp)
        except:
            text.setText("why you putting a video in here 😔💔")

button.clicked.connect(veryCoolFuction)

layout.addWidget(button)
layout.addWidget(text)

window.setLayout(layout)
window.show()
app.exec_()