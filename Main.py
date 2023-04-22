import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend.inputWindow import Ui_MainWindow
from frontend.resultWindow import Ui_ResultWindow
from Methods import Methods

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    result_window = Ui_ResultWindow()
    methods = Methods()
    ui.enterpushButton.clicked.connect(ui.test_input)
    ui.bisectionPushButton.clicked.connect(ui.bisection_input)
    ui.bisectionPushButton.clicked.connect(result_window.show)

    ui.falsePositionPushButton.clicked.connect(ui.falseposition_input)
    ui.falsePositionPushButton.clicked.connect(result_window.show)

    ui.fixedPointPushButton.clicked.connect(ui.fixedpoint_input)
    ui.fixedPointPushButton.clicked.connect(result_window.show)

    ui.newtonRaphsonPushButton.clicked.connect(ui.newtonraphson_input)
    ui.newtonRaphsonPushButton.clicked.connect(result_window.show)

    ui.secantPushButton.clicked.connect(ui.secant_input)
    ui.secantPushButton.clicked.connect(result_window.show)

    ui.resultPushButton.clicked.connect(ui.readFile)

    result_window.okPushButton.clicked.connect(result_window.close)
    ui.input_parameters.connect(methods.bisection)
    ui.input_parameters_fp.connect(methods.falsePosition)
    ui.input_parameters_fixed.connect(methods.fixedPoint)
    ui.input_parameters_nr.connect(methods.newtonRaphson)
    ui.input_parameters_sc.connect(methods.secant)

    methods.output_signal.connect(result_window.show_results)
    methods.method_name_signal.connect(result_window.show_method_name)
    ui.show()
    sys.exit(app.exec_())
