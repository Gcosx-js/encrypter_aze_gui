# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin_screen_reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle('Şifrə təyin edin')
        Form.resize(1561, 836)
        Form.setFixedSize(1561,836)
        Form.setStyleSheet("#Form{\n"
"    background-color:white;\n"
"\n"
"}")
        self.login_logos = QtWidgets.QLabel(Form)
        self.login_logos.setGeometry(QtCore.QRect(720, 110, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.login_logos.setFont(font)
        self.login_logos.setAlignment(QtCore.Qt.AlignCenter)
        self.login_logos.setObjectName("login_logos")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 340, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 340, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 340, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 460, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 460, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(880, 460, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(880, 590, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(730, 590, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(730, 710, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 590, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(610, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 1px solid rgba(80,80,80.0.5);\n"
"    \n"
"    border-radius:20px;\n"
"}")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border: 1px solid rgba(80,80,80.0.5);\n"
"    \n"
"    border-radius:20px;\n"
"}")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(790, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border: 1px solid rgba(80,80,80.0.5);\n"
"    \n"
"    border-radius:20px;\n"
"}")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(880, 260, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border: 1px solid rgba(80,80,80.0.5);\n"
"    border-radius:20px;\n"
"}")
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_delete = QtWidgets.QPushButton(Form)
        self.pushButton_delete.setGeometry(QtCore.QRect(880, 710, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_delete.setStyleSheet("QPushButton{\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:35px;\n"
"}")
        self.pushButton_delete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./gifler/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.welcome_label = QtWidgets.QLabel(Form)
        self.welcome_label.setGeometry(QtCore.QRect(290, 50, 951, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Semibold")
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(250, 98, 0);")
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.welcome_label_2 = QtWidgets.QLabel(Form)
        self.welcome_label_2.setGeometry(QtCore.QRect(290, 200, 951, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        self.welcome_label_2.setFont(font)
        self.welcome_label_2.setStyleSheet("color: rgb(53, 53, 53);")
        self.welcome_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label_2.setObjectName("welcome_label_2")
        self.imtina_btn = QtWidgets.QPushButton(Form)
        self.imtina_btn.setGeometry(QtCore.QRect(1470, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.imtina_btn.setFont(font)
        self.imtina_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.imtina_btn.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 135, 15);\n"
"    background-color:transparent;\n"
"    border: qpx solid transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(80, 80, 80,0.1);\n"
"    border:1px solid transparent;\n"
"    border-radius:15px;\n"
"}")
        self.imtina_btn.setObjectName("imtina_btn")
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.login_logos.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_9.raise_()
        self.pushButton_8.raise_()
        self.pushButton_10.raise_()
        self.pushButton_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_delete.raise_()
        self.welcome_label.raise_()
        self.welcome_label_2.raise_()
        self.imtina_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_logos.setText(_translate("Form", "Logo"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_10.setText(_translate("Form", "0"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.welcome_label.setText(_translate("Form", "Güvənlik məqsədi ilə xaiş edirik PİN təyin edin."))
        self.welcome_label_2.setText(_translate("Form", "Bunu unutmayın! Əks təqdirdə proqramı sıfırlamalı olacaqsınız"))
        self.imtina_btn.setText(_translate("Form", "İmtina"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())