from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
import sys
from accuracy import Plot_graph
from weather import Weather
from LR_pred import Pred

class Menubar(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("menubar.ui", self)
        self.btnpre.clicked.connect(self.show_pred)
        self.btnweather.clicked.connect(self.show_weather)
        self.btnacc.clicked.connect(self.show_accuracy)


    def show_pred(self):
        self.pred = Pred()
        self.pred.show()

    def show_weather(self):
        self.weather = Weather()
        self.weather.show()

    def show_accuracy(self):
        self.plot = Plot_graph()
        self.plot.accuracy()
        self.plot.time()




def main():
    app = QApplication(sys.argv)
    tm = Menubar()
    tm.show()
    app.exec_()


if __name__ == '__main__':
    main()
