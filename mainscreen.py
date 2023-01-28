from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
import sys
from login import MyLogin
from register import Reg_info
from about import About

class Main(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("mainscreen.ui", self)
        QFrame.setStyleSheet(self, "background-image: url(loginimg.jpg)")
        self.btnlogin.clicked.connect(self.show_login)
        self.btnregister.clicked.connect(self.show_reg)
        self.btnabout.clicked.connect(self.show_abt)


    def show_login(self):
        self.login =MyLogin()
        self.login.show()
    def show_reg(self):
        self.reg = Reg_info()
        self.reg.show()
    def show_abt(self):
        self.load=About()
        self.load.show()



def main():
    app = QApplication(sys.argv)
    tm = Main()
    tm.show()
    app.exec_()


if __name__ == '__main__':
    main()
