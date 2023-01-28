import requests
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

class Weather(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("weather.ui", self)
        self.btn.clicked.connect(self.getInput)


    def getInput(self):
        cityvalue = self.txtcity.text()
        API = "7f5322883dbdf676d5f984af830f595c"
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7f5322883dbdf676d5f984af830f595c&units=metric'.format(
            cityvalue, API)
        res = requests.get(url)

        data = res.json()

        temperature = data['main']['temp']
        rain = data['weather'][0]['description']
        sys = data['sys']['country']




        self.temp.setText(str(temperature))
        self.desc.setText(rain)
        self.press.setText(sys)






def main():
    app = QApplication(sys.argv)
    frame = Weather()
    frame.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




