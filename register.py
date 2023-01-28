from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import mysql.connector
from PyQt5 import QtGui
from login import MyLogin



class Reg_info(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("register.ui", self)
        self.mydb = mysql.connector.connect(host="localhost",user="root", passwd="P@ss123",database="rainfall_prediction")
        self.mycursor = self.mydb.cursor()
        self.btnreg.clicked.connect(self.info)
        #self.btnreg.setIcon(QtGui.QIcon("icon.png"))
        #self.btnradio.clicked.connect(self.info)


    def info(self):
        self.us =   self.txtuser.text().strip()
        self.pswd = self.txtpswd.text().strip()
        self.con= self.txtno.text().strip()
        self.em = self.txtemail.text().strip()
        self.nm = self.txtname.text().strip()



        if len(self.us)==0 or len(self.pswd)==0 or len(self.con)==0 or len(self.em)==0 or len(self.nm)==0 :
             self.showMessage("error","data needed")
        else:
         strinsert = "insert into register_user(UserID, Password, Contact, Email,Name)values(%s,%s,%s,%s,%s)"
         self.mycursor.execute(strinsert,(self.us,self.pswd,self.con,self.em,self.nm))
         self.mydb.commit()
         self.showMessage("insertion","data added sucessfully")

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    frame = Reg_info()
    frame.show()
    app.exec_()


if __name__ == '__main__':
    main()

