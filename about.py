from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys



class About(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("about.ui", self)



def main():
    app = QApplication(sys.argv)
    frame = About()
    frame.show()
    app.exec_()

if __name__ == '__main__':
    main()
