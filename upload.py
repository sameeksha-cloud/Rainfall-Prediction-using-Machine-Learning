from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pandas as pd
import numpy as np
import sys



class Upload(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("welcome.ui", self)
        self.btnfile.clicked.connect(self.openfile)
        self.btnget.clicked.connect(self.get_columnsname)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)



    def openfile(self):

        filename= QFileDialog.getOpenFileName(self,'open csv')

        if filename[0]:

            global df
            df = pd.read_csv(filename[0])

            print(filename[0])

            mycolumns = []
            for col in df.columns:
                mycolumns.append(col)

            for item in mycolumns:
                self.item = QListWidgetItem("%s" % item)
                self.listWidget.addItem(item)
                self.listWidget.show()
# Code galat kar rahe ho
    # yeh function button ke click per call hona chahiye tum loop me call kar rahe ho ??
    #sir ab loop k bahar kr diya maine

    def get_columnsname(self):
        #setValues =self.listWidget.curselection()
        setValues1 = self.listWidget.selectedIndexes()
        self.label.setText("col1 : " + setValues1)
        setValues2 = self.listWidget.selectedIndexes()
        self.label.setText("Col2 : " + setValues2)
        # print(setValues.index())
        #[<PyQt5.QtCore.QModelIndex object at 0x000001F4B3258748>]
        #setValues = self.listWidget.selectedItems()
        #[<PyQt5.QtWidgets.QListWidgetItem object at 0x000001A37B455A68>]
        #print(setValues.index())

        # print(len(setValues))

        # x = setValues[0]
        # y = setValues[1]
#        print("Hello")
#        print(x)
#        print(y)
#         for val in setValues:
#          print(df.iloc[:, x])
#          print(df.iloc[:, y])

def main():
    app = QApplication(sys.argv)
    frame = Upload()
    frame.show()
    app.exec_()

if __name__ == '__main__':
    main()
