from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import mysql.connector
from menubar import Menubar

class MyLogin(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("loginframe.ui", self)
        self.btnlogin.clicked.connect(self.checklogin)
        self.setWindowTitle("login")

    def checklogin(self):
        ui = self.txtuser.text()
        upass = self.txtpswd.text()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="P@ss123", database="rainfall_prediction")
        mycursor = mydb.cursor()
        query = "select * from register_user where Email=%s and Password=%s"
        data = mycursor.execute(query,(ui,upass))
        if(len(mycursor.fetchall())>0):
            self.msgshow()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("errormessage")
            msg.setText("invalid userid\password")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setDetailedText("incorrect userid and password")
            msg.show()

            msg.exec_()

    def msgshow(self):
        msg = QMessageBox()
        msg.setWindowTitle("login successfull")
        msg.setText("login successfull")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        print("login successfull")
        msg.show()
        msg.exec_()


        self.m =Menubar ()
        self.m.show()





def main():
    app = QApplication(sys.argv)
    frame = MyLogin()
    frame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


