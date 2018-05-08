from PyQt5 import QtWidgets, QtGui
import sys

import design
import matplotlib.figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import os

import time

import random



class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow, QtWidgets.QAction):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #self.pitch = [0.79, 0.5, 0.33, 0.28, 0.35, 0.53, 0.84, 1.23, 1.53, 1.71, 1.73, 1.62, 1.42, 1.17, 0.93, 0.75, 0.58, 0.47, 0.41, 0.4, 0.42, 0.46, 0.5, 0.52, 0.51, 0.46, 0.33, 0.19, -0.05, -0.29, -0.5, -0.58, -0.51, -0.25, 0.07, 0.33, 0.51, 0.54, 0.39, 0.01, -0.43, -0.72, -0.82, -0.88, -0.81, -0.61, -0.52, -0.78, -1.09, -1.36, -1.65, -1.81, -1.84, -1.77, -1.63, -1.53, -1.47, -1.46, -1.5, -1.59, -1.7, -1.76, -1.69, -1.48, -1.27, -1.21, -1.36, -1.78, -2.42, -3.02, -3.45, -3.6, -3.45, -3.11, -2.76, -2.4, -2.0, -1.62, -1.25, -0.99, -1.02, -1.24, -1.57, -1.96, -2.32, -2.6, -2.8, -3.08, -3.24, -3.27, -2.91, -2.44, -1.86, -1.17, -0.39, 0.3, 0.82, 1.17, 1.28, 1.12, 0.76, 0.31, -0.12, -0.61, -1.08, -1.37, -1.49, -1.58, -1.59, -1.5, -1.41, -1.38, -1.5, -1.74, -2.0, -2.19, -2.34, -2.43, -2.5, -2.57, -2.68, -2.86, -3.08, -3.25, -3.27, -3.1, -2.81, -2.48, -2.14, -1.85, -1.68, -1.69, -1.76, -1.82, -1.88, -1.9, -1.86, -1.72, -1.58, -1.47, -1.35, -1.19, -1.03, -0.93, -0.83, -0.82, -0.84, -0.99, -1.23, -1.49, -1.68, -1.76, -1.72, -1.45, -0.96, -0.19, 0.73, 1.71, 2.46, 3.14, 3.74, 4.21, 4.43, 4.48, 4.37, 4.09, 3.74, 3.34, 2.84, 2.29, 1.91, 1.67, 1.41, 1.11, 0.82, 0.55, 0.28, -0.04, -0.47, -0.83, -1.05, -1.28, -1.59, -1.97, -2.35, -2.71, -3.0, -3.16, -3.31, -3.53, -3.77, -3.89, -4.0, -4.04, -4.02, -4.15, -4.52, -4.99, -5.34, -5.49, -5.54, -5.49, -5.34, -5.06, -4.73, -4.35, -3.99, -3.77, -3.79, -4.03, -4.48, -5.04, -5.66, -6.25, -6.7, -6.9, -6.84, -6.58, -6.2, -5.71, -5.12, -4.45, -3.64, -2.85, -2.31, -2.08, -2.16, -2.54, -3.23, -4.19, -5.34, -6.56, -7.46, -8.08, -8.56, -9.0, -9.34, -9.5, -9.39, -8.95, -8.27, -7.43, -6.66, -6.27, -6.21, -6.21, -6.26, -6.19, -5.93, -5.45, -4.79, -4.03, -3.26, -2.52, -1.84, -1.34, -1.14, -1.28, -1.61, -1.97, -2.39, -2.93, -3.48, -3.88, -4.04, -3.92, -3.5, -2.89, -2.32, -1.92, -1.77, -1.83, -2.01, -2.23, -2.35, -2.5, -2.7, -2.88, -3.14, -3.4, -3.48, -3.29, -2.92, -2.38, -1.6, -0.76, -0.08, 0.48, 0.93, 1.17, 1.21, 0.93, 0.49, -0.13, -0.93, -1.75, -2.62, -3.43, -3.99, -4.18, -4.14, -3.85, -3.43, -2.99, -2.47, -1.84, -1.29, -0.92, -0.86, -1.02, -1.3, -1.71, -2.31, -3.02, -3.74, -4.39, -4.78, -4.9, -4.87, -4.71, -4.55, -4.45, -4.38, -4.3, -4.13, -4.0, -3.92, -3.76, -3.81, -4.03, -4.34, -4.69, -4.98, -5.2, -5.21, -5.05, -4.78, -4.42, -4.05, -3.75, -3.5, -3.34, -3.31, -3.37, -3.51, -3.68, -3.98, -4.32, -4.7, -5.18, -5.71, -6.2, -6.68, -6.87, -6.82, -6.58, -6.25, -5.88, -5.59, -5.52, -5.69, -6.05, -6.52, -6.95, -7.39, -7.86, -8.21, -8.57, -8.97, -9.26, -9.34, -9.29, -9.01, -8.62, -8.19, -7.76, -7.35, -6.87, -6.48, -6.31, -6.36, -6.7, -7.3, -8.06, -8.96, -9.83, -10.61, -11.2, -11.64, -12.03, -12.41, -12.75, -12.82, -12.6, -12.17, -11.62, -10.91, -10.17, -9.69, -9.32, -9.1, -9.03, -9.18, -9.44, -9.73, -9.98, -10.12, -9.91, -9.27, -8.41, -7.59, -6.86, -6.22, -5.89, -5.85, -6.07, -6.52, -7.13, -7.75, -8.22, -8.49, -8.56, -8.42, -8.08, -7.64, -7.03, -6.33, -5.68, -5.07, -4.54, -4.22, -4.13, -4.32, -4.74, -5.3, -5.87, -6.43, -6.9, -7.39, -7.92, -8.28, -8.46, -8.38, -8.0, -7.43, -6.78, -6.01, -5.1, -4.17, -3.51, -3.08, -3.0, -3.27, -3.71, -4.33, -5.09, -5.94, -6.71, -7.34, -7.82, -8.02, -7.83, -7.38, -6.77, -6.06, -5.33, -4.58, -4.0, -3.65, -3.47, -3.53, -3.88, -4.47, -5.3, -6.28, -7.29, -8.19, -8.85, -9.12, -9.09, -8.8, -8.25, -7.58, -6.83, -6.09, -5.49, -5.21, -5.25, -5.62, -6.28, -7.13, -7.98, -8.84, -9.53, -10.06, -10.34, -10.38, -10.3, -10.08, -9.73, -9.24, -8.61, -7.99, -7.49, -7.12, -6.86, -6.72, -6.72, -6.86, -7.11, -7.43, -7.75, -8.0, -8.14, -8.05, -7.8, -7.49, -7.1, -6.69, -6.27, -5.9, -5.66, -5.53, -5.52, -5.62, -5.85, -6.13, -6.28, -6.32, -6.26, -6.14, -6.01, -5.83, -5.56, -5.26, -4.91, -4.51, -4.11, -3.74, -3.37, -3.05, -2.89, -2.98, -3.23, -3.63, -4.1, -4.52, -4.89, -5.15, -5.25, -5.12, -4.81, -4.47, -4.14, -3.95, -3.88, -3.71, -3.47, -3.35, -3.32, -3.53, -3.94, -4.51, -5.2, -5.82, -6.35, -6.68, -6.84, -6.88, -6.64, -6.32, -6.01, -5.72, -5.42, -5.24, -5.22, -5.34, -5.64, -6.07, -6.75, -7.57, -8.27, -9.0, -9.7, -10.21, -10.37, -10.26, -9.93, -9.45, -8.94, -8.43, -7.99, -7.63, -7.4, -7.35, -7.61, -8.03, -8.58, -9.24, -9.92, -10.3, -10.49, -10.55, -10.27, -9.83, -9.18, -8.34, -7.45, -6.62, -5.92, -5.34, -4.9, -4.66, -4.55, -4.64, -4.97, -5.54, -6.25, -6.87, -7.31, -7.46, -7.38, -7.14, -6.79, -6.38, -5.94, -5.43, -4.96, -4.59, -4.36, -4.25, -4.37, -4.71, -5.26, -6.06, -6.95, -7.83, -8.75, -9.68, -10.42, -10.88, -11.1, -11.08, -10.87, -10.43, -9.81, -9.15, -8.4, -7.69, -7.16, -6.89, -6.86, -7.08, -7.56, -8.33, -9.31, -10.33, -11.22, -11.78, -11.92, -11.8, -11.41, -10.8, -10.08, -9.18, -8.28, -7.48, -6.91, -6.6, -6.48, -6.63, -7.0, -7.55, -8.13, -8.54, -8.67, -8.66, -8.54, -8.38, -8.16, -7.95, -7.73, -7.52, -7.19, -6.77, -6.33, -5.96, -5.68, -5.52, -5.35, -5.17, -5.0, -4.87, -4.83, -4.89, -4.99, -5.1, -5.27, -5.45, -5.57, -5.65, -5.7, -5.72, -5.81, -5.99, -6.25, -6.54, -6.76, -6.75, -6.46, -6.02, -5.54, -4.98, -4.44, -4.0, -3.65, -3.52, -3.57, -3.69, -3.78, -3.79, -3.73, -3.61, -3.35, -3.0, -2.63, -2.34, -1.99, -1.59, -1.23, -0.98, -0.92, -1.01, -1.15, -1.29, -1.43, -1.57, -1.84, -2.19, -2.64, -3.07, -3.37, -3.49, -3.4, -3.2, -2.99, -2.8, -2.62, -2.49, -2.44, -2.55, -2.88, -3.4, -4.02, -4.69, -5.25, -5.74, -6.2, -6.49, -6.61, -6.57, -6.29, -5.96, -5.65, -5.36, -5.14, -4.99, -5.04, -5.27, -5.64, -6.07, -6.46, -6.88, -7.22, -7.43, -7.53, -7.39, -7.09, -6.62, -6.04, -5.47, -4.8, -4.17, -3.82, -3.75, -4.0, -4.5, -5.11, -5.79, -6.39, -7.0, -7.17, -7.0, -6.73, -6.33, -5.85, -5.27, -4.69, -4.25, -4.0, -3.94, -3.87, -3.87, -3.95, -4.03, -4.08, -4.12, -4.12, -4.18, -4.18, -4.22, -4.23, -4.18, -4.15, -4.03, -3.82, -3.61, -3.46, -3.36, -3.22, -3.0, -2.75, -2.64, -2.6, -2.56, -2.48, -2.21, -1.69, -0.91, 0.11, 1.11, 1.79, 2.13, 2.13, 1.93, 1.65, 1.45, 1.33, 1.23, 1.07, 0.89, 0.62, 0.27, -0.07, -0.32, -0.51, -0.68, -0.88, -1.12, -1.33, -1.32, -1.13, -0.9, -0.8, -0.94, -1.26, -1.65, -1.98, -2.22, -2.35, -2.49, -2.76, -3.1, -3.44, -3.69, -3.74, -3.55, -3.23, -2.86, -2.51, -2.16, -1.73, -1.26, -0.8, -0.39, -0.12, -0.07, -0.1, -0.18, -0.28, -0.35, -0.39, -0.42, -0.41, -0.4, -0.25, 0.05, 0.28, 0.42, 0.53, 0.57, 0.59, 0.67, 0.89, 1.21, 1.44, 1.53, 1.48]
        fileMenu = self.actionImport_SnP
        fileMenu.triggered.connect(self.plot)
     
        

    def plot(self):
        self.pitch = list(random.random()*100 for x in range(100))
        self.graphicsView.figure.clear()
        ax=self.graphicsView.figure.add_subplot(111)
        ax.plot(self.pitch, '*-')
        self.graphicsView.draw()

        


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form

    sys.exit(app.exec_())
    


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function

