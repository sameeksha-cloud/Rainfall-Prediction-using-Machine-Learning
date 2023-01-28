from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import seaborn as sns
import sys



class Plot_graph():
    def accuracy(self):
        sns.set(font_scale=1.5)
        data = {'Logistic_regression ': 0.843569787613109, 'Decision_Tree': 0.7851985559566786,
                'Random_Forest': 0.8545173238314032}
        score = list(data.keys())
        values = list(data.values())

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(score, values, color=['#fff5ab', '#94edff', '#e6abff'],
                width=0.4)
        plt.suptitle("Accuracy Based Perfomance", fontsize=36,color='blue')
        plt.xlabel("Algorithms",fontsize = 24,color='blue')
        plt.ylabel("Accuracy",fontsize = 24,color='blue')

        plt.show()


    def time(self):
        sns.set(font_scale=1.5)
        data = {'LR_time ': 0.33309316635131836, 'DT_time': 1.2237663269042969, 'RF_time': 21.629181385040283}
        score = list(data.keys())
        values = list(data.values())

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(score, values, color=['#ffa442', '#94edff', '#e6abff'],
                width=0.4)
        plt.suptitle("Time Based Perfomance",fontsize = 36,color='blue')
        plt.xlabel("Algorithms",fontsize = 24,color='blue')
        plt.ylabel("Time Taken",fontsize = 24,color='blue')
        plt.show()


def main():
    app = QApplication(sys.argv)

    app.exec_()
if __name__ == '__main__':
    main()