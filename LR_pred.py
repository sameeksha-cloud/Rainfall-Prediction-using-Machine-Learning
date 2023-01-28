from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtGui
#Import necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
data = pd.read_csv('E:\\Project_Rainfall_prediction\\rainfalldoc.csv')

# Getting rid of the columns with objects which will not be used in our model:
data.drop(['Date', 'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RISK_MM'], axis=1, inplace=True)

# And we need to replace NaN values with mean values of each column:
data.fillna(data.mean(), inplace=True)

# Now we can change that day and next days'predictions (yes and no) to 1 and 0:
data.RainToday = [1 if each == 'Yes' else 0 for each in data.RainToday]
data.RainTomorrow = [1 if each == 'Yes' else 0 for each in data.RainTomorrow]
y = data.RainTomorrow.values
X = data.drop('RainTomorrow', axis=1)

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state=0)

#feature Scaling
from sklearn.preprocessing import StandardScaler
st_X= StandardScaler()
X_train= st_X.fit_transform(X_train)
X_test= st_X.transform(X_test)

#Fitting Logistic Regression to the training set
from sklearn.linear_model import LogisticRegression
classifier= LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)


class Pred(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("LR_pred.ui", self)
        self.btnpred.clicked.connect(self.info)



    def info(self):
        self.min = self.txtmin.text().strip()
        self.max = self.txtmax.text().strip()
        self.rain= self.txtrain.text().strip()
        self.eva = self.txteva.text().strip()
        self.sun= self.txtsun.text().strip()
        self.win= self.txtwin.text().strip()
        self.win9=self.txtwin9.text().strip()
        self.win3= self.txtwin3.text().strip()
        self.humi9 = self.txthumi9.text().strip()
        self.humi3= self.txthumi3.text().strip()
        self.press9 = self.txtpress9.text().strip()
        self.press3 = self.txtpress3.text().strip()
        self.cl9 = self.txtcl9.text().strip()
        self.cl3 = self.txtcl3.text().strip()
        self.temp9 = self.txttemp9.text().strip()
        self.temp3 = self.txttemp3.text().strip()
        self.tday = self.txttoday.text().strip()

        self.array = np.array([[self.min,self.max,self.rain,self.eva,self.sun,self.win,self.win9,self.win3,self.humi9,self.humi3,self.press9,self.press3,self.cl9,self.cl3,self.temp9,self.temp3,self.tday]])
        p = self.array.astype(np.float)

        prediction_result = (classifier.predict(p))
        print(type(prediction_result))
        str= prediction_result.item(0)
        print(str)
        if str == 1:
           self.txtresult.setText("Yes")

        else:
           self.txtresult.setText("NO")
        # str = np.array_str(prediction_result)
        # print(type(str))

        # if str==[0]:
        #    self.txtresult.setText("NO")
        # else:
        #    self.txtresult.setText("Yes")





def main():

    app = QApplication(sys.argv)
    frame = Pred()
    frame.show()
    app.exec_()


if __name__ == '__main__': main()




