# import DfaToRegex
import converter
import ToJSON
import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
sys.path.insert(1, './static/ui')
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(796, 845)
        MainWindow.setFixedSize(800, 832)  # Fixed Size
        MainWindow.setMouseTracking(False)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StatesTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.StatesTB.setGeometry(QtCore.QRect(200, 200, 431, 41))
        self.StatesTB.setMouseTracking(False)
        self.StatesTB.setWhatsThis("")
        self.StatesTB.setAutoFillBackground(False)
        self.StatesTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StatesTB.setObjectName("StatesTB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 170, 101, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label.setObjectName("label")
        self.lettersTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lettersTB.setGeometry(QtCore.QRect(200, 300, 431, 41))
        self.lettersTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lettersTB.setObjectName("lettersTB")
        self.tfTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tfTB.setGeometry(QtCore.QRect(200, 420, 431, 71))
        self.tfTB.setWhatsThis("")
        self.tfTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tfTB.setObjectName("tfTB")
        self.startTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.startTB.setGeometry(QtCore.QRect(200, 540, 431, 41))
        self.startTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.startTB.setPlaceholderText("")
        self.startTB.setObjectName("startTB")
        self.finalTB = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.finalTB.setGeometry(QtCore.QRect(200, 640, 431, 41))
        self.finalTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finalTB.setObjectName("finalTB")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 280, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 400, 421, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 520, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 620, 161, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label_5.setObjectName("label_5")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(340, 740, 141, 41))
        self.Button.setStyleSheet("\n"
                                  "background-color: rgb(186, 214, 234);")
        self.Button.setObjectName("Button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 29, 451, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 811, 861))
        self.frame.setStyleSheet("background-image: url(:/newPrefix/geometry-background.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.StatesTB.raise_()
        self.label.raise_()
        self.lettersTB.raise_()
        self.tfTB.raise_()
        self.startTB.raise_()
        self.finalTB.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Button.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##########################################################################
        self.Button.clicked.connect(self.onSubmit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StatesTB.setPlaceholderText(_translate("MainWindow", "states seperated by <space>"))
        self.label.setText(_translate("MainWindow", "Enter States"))
        self.lettersTB.setPlaceholderText(_translate("MainWindow", "symbols separated by <space>"))
        self.tfTB.setPlaceholderText(_translate("MainWindow", "transitions seperated by <space>"))
        self.finalTB.setPlaceholderText(_translate("MainWindow", "final states seperated by <space>"))
        self.label_2.setText(_translate("MainWindow", "Enter Alphabet"))
        self.label_3.setText(_translate("MainWindow", "Enter Transitions : <CurrentState;Input;NextState>"))
        self.label_4.setText(_translate("MainWindow", "Enter Initial State"))
        self.label_5.setText(_translate("MainWindow", "Enter Final States"))
        self.Button.setText(_translate("MainWindow", "Submit!"))
        self.label_6.setText(_translate("MainWindow", "<strong>DFA</strong> to Regex converter"))

    def onSubmit(self):
        try:

            states = self.StatesTB.toPlainText().split()
            # self.StatesTB.setPlainText("")
            letters = self.lettersTB.toPlainText().split()
            # self.lettersTB.setPlainText("")
            tf = self.tfTB.toPlainText().split()
            # self.tfTB.setPlainText("")
            tf2 = [[] * 3] * len(tf)
            for i in range(len(tf2)):
                tf2[i] = tf[i].split(";")
            startStates = self.startTB.toPlainText().split()
            # self.startTB.setPlainText("")
            finalStates = self.finalTB.toPlainText().split()
            # self.finalTB.setPlainText("")

            ToJSON.w2json(states, letters, tf2, startStates, finalStates)
            # DfaToRegex.Convertor()
            converter.Convertor()

            msg = QMessageBox()
            msg.setWindowTitle("Regular Expression")
            msg.setIcon(QMessageBox.Information)
            with open('static/json/outputMain.json') as json_file:
                data = json.load(json_file)
            msg.setText("   Regex:  " + str(data['regex'] + " \t\t\n\n"))
            x = msg.exec_()
            self.StatesTB.setPlainText("")
            self.lettersTB.setPlainText("")
            self.tfTB.setPlainText("")
            self.startTB.setPlainText("")
            self.finalTB.setPlainText("")

        except Exception:

            msg2 = QMessageBox()
            msg2.setWindowTitle("Invalid Input")
            msg2.setIcon(QMessageBox.Warning)
            msg2.setText("   Invalid Input!  ")
            x = msg2.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())