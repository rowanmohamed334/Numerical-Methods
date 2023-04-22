# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_one.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import math


class Ui_MainWindow(QMainWindow):
    input_parameters = pyqtSignal(str, int, int, float, int)
    input_parameters_fp = pyqtSignal(str, int, int, float, int)
    input_parameters_fixed = pyqtSignal(str, float, float, int)
    input_parameters_nr = pyqtSignal(str, int, float, int)
    input_parameters_sc = pyqtSignal(str, int, int, float, int)
    left = 0
    right = 0
    epsilon = 0
    max_iteration = 0
    xr = 0
    eqn = ''

    # self.input_parameters.emit(str(eqn), int(left), int(right), float(epsilon), int(max_iteration))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(771, 789)
        self.setStyleSheet("#centralwidget {\n"
                           "    background-color: rgb(60, 42, 77);\n"
                           "}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("color:rgb(60, 42, 77);")
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(290, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(224, 240, 234)")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(149, 173, 190)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.equationlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.equationlineEdit.setGeometry(QtCore.QRect(220, 80, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.equationlineEdit.setFont(font)
        self.equationlineEdit.setStyleSheet("border-radius: 25px;\n"
                                            "background-color:rgb(224, 240, 234);\n"
                                            "border: 2px solid rgb(149, 173, 190);\n"
                                            "")
        self.equationlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.equationlineEdit.setObjectName("equationlineEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 50, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 550, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(149, 173, 190);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 460, 541, 261))
        self.frame.setStyleSheet("border-radius: 25px;\n"
                                 "border: 2px solid white;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bisectionPushButton = QtWidgets.QPushButton(self.frame)
        self.bisectionPushButton.setGeometry(QtCore.QRect(10, 10, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bisectionPushButton.setFont(font)
        self.bisectionPushButton.setStyleSheet("border-radius: 20px;\n"
                                               "border-color:rgb(87, 79, 125);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "background-color:rgb(87, 79, 125);\n"
                                               "border: 2px solid white;")
        self.bisectionPushButton.setObjectName("bisectionPushButton")
        self.falsePositionPushButton = QtWidgets.QPushButton(self.frame)
        self.falsePositionPushButton.setGeometry(QtCore.QRect(10, 60, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.falsePositionPushButton.setFont(font)
        self.falsePositionPushButton.setStyleSheet("border-radius: 20px;\n"
                                                   "border-color:rgb(87, 79, 125);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "background-color:rgb(87, 79, 125);\n"
                                                   "border: 2px solid white;")
        self.falsePositionPushButton.setObjectName("falsePositionPushButton")
        self.fixedPointPushButton = QtWidgets.QPushButton(self.frame)
        self.fixedPointPushButton.setGeometry(QtCore.QRect(10, 110, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fixedPointPushButton.setFont(font)
        self.fixedPointPushButton.setStyleSheet("border-radius: 20px;\n"
                                                "border-color:rgb(87, 79, 125);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color:rgb(87, 79, 125);\n"
                                                "border: 2px solid white;")
        self.fixedPointPushButton.setObjectName("fixedPointPushButton")
        self.newtonRaphsonPushButton = QtWidgets.QPushButton(self.frame)
        self.newtonRaphsonPushButton.setGeometry(QtCore.QRect(10, 160, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.newtonRaphsonPushButton.setFont(font)
        self.newtonRaphsonPushButton.setStyleSheet("border-radius: 20px;\n"
                                                   "border-color:rgb(87, 79, 125);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "background-color:rgb(87, 79, 125);\n"
                                                   "border: 2px solid white;")
        self.newtonRaphsonPushButton.setObjectName("newtonRaphsonPushButton")
        self.secantPushButton = QtWidgets.QPushButton(self.frame)
        self.secantPushButton.setGeometry(QtCore.QRect(10, 210, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.secantPushButton.setFont(font)
        self.secantPushButton.setStyleSheet("border-radius: 20px;\n"
                                            "border-color:rgb(87, 79, 125);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:rgb(87, 79, 125);\n"
                                            "border: 2px solid white;")
        self.secantPushButton.setObjectName("secantPushButton")
        self.precisionlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.precisionlineEdit.setGeometry(QtCore.QRect(220, 150, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.precisionlineEdit.setFont(font)
        self.precisionlineEdit.setStyleSheet("border-radius: 25px;\n"
                                             "background-color:rgb(224, 240, 234);\n"
                                             "border: 2px solid rgb(149, 173, 190);\n"
                                             "")
        self.precisionlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.precisionlineEdit.setObjectName("precisionlineEdit")
        self.MaxIterationlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxIterationlineEdit.setGeometry(QtCore.QRect(220, 220, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MaxIterationlineEdit.setFont(font)
        self.MaxIterationlineEdit.setStyleSheet("border-radius: 25px;\n"
                                                "background-color:rgb(224, 240, 234);\n"
                                                "border: 2px solid rgb(149, 173, 190);\n"
                                                "")
        self.MaxIterationlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.MaxIterationlineEdit.setObjectName("MaxIterationlineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.enterpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterpushButton.setGeometry(QtCore.QRect(610, 410, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.enterpushButton.setFont(font)
        self.enterpushButton.setStyleSheet("border-radius: 20px;\n"
                                           "border-color:rgb(87, 79, 125);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:rgb(149, 173, 190);\n"
                                           "border: 2px solid white;")
        self.enterpushButton.setObjectName("enterpushButton")
        self.resultPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultPushButton.setGeometry(QtCore.QRect(610, 730, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.resultPushButton.setFont(font)
        self.resultPushButton.setStyleSheet("border-radius: 20px;\n"
                                            "border-color:rgb(87, 79, 125);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:rgb(149, 173, 190);\n"
                                            "border: 2px solid white;")
        self.resultPushButton.setObjectName("resultPushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(5, 300, 130, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 300, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.leftIntervallineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.leftIntervallineEdit.setGeometry(QtCore.QRect(360, 300, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftIntervallineEdit.setFont(font)
        self.leftIntervallineEdit.setStyleSheet("border-radius: 25px;\n"
                                                "background-color:rgb(224, 240, 234);\n"
                                                "border: 2px solid rgb(149, 173, 190);\n"
                                                "")
        self.leftIntervallineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.leftIntervallineEdit.setObjectName("leftIntervallineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 300, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 300, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.rightIntervallineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rightIntervallineEdit.setGeometry(QtCore.QRect(540, 300, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rightIntervallineEdit.setFont(font)
        self.rightIntervallineEdit.setStyleSheet("border-radius: 25px;\n"
                                                 "background-color:rgb(224, 240, 234);\n"
                                                 "border: 2px solid rgb(149, 173, 190);\n"
                                                 "")
        self.rightIntervallineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.rightIntervallineEdit.setObjectName("rightIntervallineEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 370, 140, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(149, 173, 190)")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.leftIntervallineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.leftIntervallineEdit_2.setGeometry(QtCore.QRect(460, 370, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftIntervallineEdit_2.setFont(font)
        self.leftIntervallineEdit_2.setStyleSheet("border-radius: 25px;\n"
                                                  "background-color:rgb(224, 240, 234);\n"
                                                  "border: 2px solid rgb(149, 173, 190);\n"
                                                  "")
        self.leftIntervallineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.leftIntervallineEdit_2.setObjectName("leftIntervallineEdit_2")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Root Finder"))
        self.label.setText(_translate("MainWindow", "ENTER EQUATION:"))
        self.label_2.setText(_translate("MainWindow", "Choose Method:"))
        self.bisectionPushButton.setText(_translate("MainWindow", "Bisection"))
        self.falsePositionPushButton.setText(_translate("MainWindow", "False Position"))
        self.fixedPointPushButton.setText(_translate("MainWindow", "Fixed Point"))
        self.newtonRaphsonPushButton.setText(_translate("MainWindow", "Newton Raphson"))
        self.secantPushButton.setText(_translate("MainWindow", "Secant"))
        self.precisionlineEdit.setPlaceholderText(_translate("MainWindow", "FOR DEFAULT VALUE ENTER 0"))
        self.MaxIterationlineEdit.setPlaceholderText(_translate("MainWindow", "FOR DEFAULT VALUE ENTER 0"))
        self.label_3.setText(_translate("MainWindow", "Max. Iterations:"))
        self.label_4.setText(_translate("MainWindow", "precision:"))
        self.enterpushButton.setText(_translate("MainWindow", "ENTER"))
        self.resultPushButton.setText(_translate("MainWindow", "FILE"))
        self.label_5.setText(_translate("MainWindow", "Guess:"))
        self.label_6.setText(_translate("MainWindow", "["))
        self.label_7.setText(_translate("MainWindow", ","))
        self.label_8.setText(_translate("MainWindow", "]"))
        self.label_9.setText(_translate("MainWindow", "Xr:"))

    @pyqtSlot()
    def test_input(self):
        self.left = self.leftIntervallineEdit.text()
        self.right = self.rightIntervallineEdit.text()
        self.xr = self.leftIntervallineEdit_2.text()
        if self.precisionlineEdit.text() == 0 or self.precisionlineEdit.text() == '':
            self.epsilon = 0.00001
        else:
            self.epsilon = self.precisionlineEdit.text()
        if self.MaxIterationlineEdit.text() == 0 or self.MaxIterationlineEdit.text() == '':
            self.max_iteration = 50
        else:
            self.max_iteration = self.MaxIterationlineEdit.text()

        self.eqn = self.equationlineEdit.text()
        if 'e' in self.eqn:
            self.eqn = self.eqn.replace('e', 'math.e')

        print("input equation", self.eqn)

    def readFile(self):
        f = open("E:\8th term\\numerical\project one\\functions.txt", "r")
        line = f.read()
        currentline = line.split(",")
        self.eqn = currentline[0]
        if 'e' in self.eqn:
            self.eqn = self.eqn.replace('e', 'math.e')
        self.epsilon = currentline[1]
        self.max_iteration = currentline[2]
        if self.max_iteration == ' - ':
            self.max_iteration = 50
        if self.epsilon == ' - ':
            self.epsilon = 0.00001

        self.left = currentline[3]
        self.right = currentline[4]
        self.xr = currentline[5]
        self.leftIntervallineEdit.setText(self.left)
        self.MaxIterationlineEdit.setText(str(self.max_iteration))
        self.precisionlineEdit.setText(str(self.epsilon))
        self.rightIntervallineEdit.setText(self.right)
        self.equationlineEdit.setText(self.eqn)
        self.leftIntervallineEdit_2.setText(self.xr)

    def bisection_input(self):
        self.input_parameters.emit(str(self.eqn), float(self.left), float(self.right), float(self.epsilon),
                                   int(self.max_iteration))

    def falseposition_input(self):
        self.input_parameters_fp.emit(str(self.eqn), float(self.left), float(self.right), float(self.epsilon),
                                      int(self.max_iteration))

    def fixedpoint_input(self):
        self.input_parameters_fixed.emit(str(self.eqn), float(self.xr), float(self.epsilon),
                                         int(self.max_iteration))

    def newtonraphson_input(self):
        self.input_parameters_nr.emit(str(self.eqn), float(self.xr), float(self.epsilon),
                                      int(self.max_iteration))

    def secant_input(self):
        self.input_parameters_sc.emit(str(self.eqn), float(self.left), float(self.right), float(self.epsilon),
                                      int(self.max_iteration))