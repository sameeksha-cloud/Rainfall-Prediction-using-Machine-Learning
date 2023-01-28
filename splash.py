from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import pyttsx3 as p
import sys

from mainscreen import Main
def main():
    app = QApplication(sys.argv)
    splash_pix=QPixmap("rain.jpg")
    splash=QSplashScreen(splash_pix)
    splash.showFullScreen()

    current_window_flags = splash.windowFlags()
    splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|current_window_flags)

    font=QtGui.QFont()
    font.setFamily("Fantasy")
    font.setPointSize(80)
    splash.setFont(font)
    message=" Welcome!!"

    #to write sm text along with the welcome
    splash.showMessage(message,QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight,QtGui.QColor.fromRgb(247, 243, 230))

    # splash.setMask(splash_pix.mask())
    # splash.showFullScreen()

    splash.show()
    app.processEvents()
    import time
    time.sleep(2)

    engine = p.init()  # object creation
    engine.setProperty("rate",160)

    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say("APP WELCOMES YOU")
    engine.runAndWait()
    engine.stop()

    main = Main()
    main.show()
    splash.finish(main)
    app.exec_()

if __name__ == '__main__':
    main()