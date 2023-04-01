import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class App (QApplication):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.ui()

    def ui(self):
        win=QWidget()
        win.setWindowTitle("Res Bulletin")
        win.setFixedWidth(1000)
        win.setStyleSheet("background: #FDFD96")    
        
        win.textbox = QLineEdit()
        win.textbox.move(20, 20)
        win.textbox.resize(280,40)
        win.show()

    if __name__ == '__main__':
        app=QApplication(sys.argv)
        sys.exit(app.exec())