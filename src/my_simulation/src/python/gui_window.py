# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gui_window(object):
    def setupUi(self, Gui_window):
        Gui_window.setObjectName("Gui_window")
        Gui_window.resize(1563, 1128)
        self.centralwidget = QtWidgets.QWidget(Gui_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(820, 230, 231, 211))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(:/pic_logo/image/98576c3bc08bc5393154d43d2ec07e47.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../../../../LENOVO/.designer/backup/image/98576c3bc08bc5393154d43d2ec07e47.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(470, 510, 931, 101))
        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.home)
        self.label_6.setGeometry(QtCore.QRect(770, 420, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Likhan")
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_26 = QtWidgets.QLabel(self.home)
        self.label_26.setGeometry(QtCore.QRect(690, 640, 721, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_29 = QtWidgets.QLabel(self.home)
        self.label_29.setGeometry(QtCore.QRect(690, 700, 791, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.home)
        self.label_30.setGeometry(QtCore.QRect(800, 740, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_log_out = QtWidgets.QPushButton(self.home)
        self.pushButton_log_out.setGeometry(QtCore.QRect(1830, 0, 71, 61))
        self.pushButton_log_out.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../do_an_QT_designer/image/log_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_log_out.setIcon(icon)
        self.pushButton_log_out.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_log_out.setObjectName("pushButton_log_out")
        self.label_25 = QtWidgets.QLabel(self.home)
        self.label_25.setGeometry(QtCore.QRect(560, 10, 861, 101))
        font = QtGui.QFont()
        font.setFamily("Likhan")
        font.setPointSize(25)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_28 = QtWidgets.QLabel(self.home)
        self.label_28.setGeometry(QtCore.QRect(750, 100, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Likhan")
        font.setPointSize(25)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(self.home)
        self.label_31.setGeometry(QtCore.QRect(670, 160, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Likhan")
        font.setPointSize(25)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.home, "")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.label_camera = QtWidgets.QLabel(self.main)
        self.label_camera.setGeometry(QtCore.QRect(510, 0, 801, 521))
        self.label_camera.setStyleSheet("background-color: rgb(85, 255, 255,100);\n"
"border-radius:10px;\n"
"border-color: black;\n"
"border: 3px solid blue;")
        self.label_camera.setObjectName("label_camera")
        self.pushButton_unlock = QtWidgets.QPushButton(self.main)
        self.pushButton_unlock.setGeometry(QtCore.QRect(650, 560, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_unlock.setFont(font)
        self.pushButton_unlock.setStyleSheet("QPushButton{;\n"
"    background-color: rgb(85, 0, 127);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:8px;}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_unlock.setObjectName("pushButton_unlock")
        self.pushButton_lock = QtWidgets.QPushButton(self.main)
        self.pushButton_lock.setGeometry(QtCore.QRect(550, 560, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_lock.setFont(font)
        self.pushButton_lock.setStyleSheet("QPushButton{    background-color: rgb(85, 0, 127);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:8px;}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_lock.setObjectName("pushButton_lock")
        self.pushButton_run = QtWidgets.QPushButton(self.main)
        self.pushButton_run.setGeometry(QtCore.QRect(1110, 570, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_home = QtWidgets.QPushButton(self.main)
        self.pushButton_home.setGeometry(QtCore.QRect(1110, 630, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_home.setObjectName("pushButton_home")
        self.label_69 = QtWidgets.QLabel(self.main)
        self.label_69.setGeometry(QtCore.QRect(820, 540, 491, 161))
        self.label_69.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_69.setText("")
        self.label_69.setObjectName("label_69")
        self.label_74 = QtWidgets.QLabel(self.main)
        self.label_74.setGeometry(QtCore.QRect(510, 540, 281, 161))
        self.label_74.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_74.setText("")
        self.label_74.setObjectName("label_74")
        self.pushButton_connect_drone = QtWidgets.QPushButton(self.main)
        self.pushButton_connect_drone.setGeometry(QtCore.QRect(550, 630, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_connect_drone.setFont(font)
        self.pushButton_connect_drone.setStyleSheet("QPushButton{    background-color: rgb(85, 0, 127);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:8px;}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_connect_drone.setObjectName("pushButton_connect_drone")
        self.comboBox_choose_location = QtWidgets.QComboBox(self.main)
        self.comboBox_choose_location.setGeometry(QtCore.QRect(860, 570, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.comboBox_choose_location.setFont(font)
        self.comboBox_choose_location.setStyleSheet("QComboBox{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QComboBox:hover {background-color: rgb(85, 0, 127,200);}\n"
"QComboBox:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.comboBox_choose_location.setEditable(False)
        self.comboBox_choose_location.setObjectName("comboBox_choose_location")
        self.comboBox_choose_location.addItem("")
        self.comboBox_choose_location.addItem("")
        self.comboBox_choose_location.addItem("")
        self.textEdit_location = QtWidgets.QTextEdit(self.main)
        self.textEdit_location.setGeometry(QtCore.QRect(970, 640, 101, 41))
        self.textEdit_location.setObjectName("textEdit_location")
        self.label_location = QtWidgets.QLabel(self.main)
        self.label_location.setGeometry(QtCore.QRect(860, 650, 101, 31))
        self.label_location.setObjectName("label_location")
        self.textEdit_message = QtWidgets.QTextEdit(self.main)
        self.textEdit_message.setGeometry(QtCore.QRect(510, 719, 801, 121))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.textEdit_message.setFont(font)
        self.textEdit_message.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_message.setReadOnly(True)
        self.textEdit_message.setObjectName("textEdit_message")
        self.label_74.raise_()
        self.label_69.raise_()
        self.label_camera.raise_()
        self.pushButton_unlock.raise_()
        self.pushButton_lock.raise_()
        self.pushButton_run.raise_()
        self.pushButton_home.raise_()
        self.pushButton_connect_drone.raise_()
        self.comboBox_choose_location.raise_()
        self.textEdit_location.raise_()
        self.label_location.raise_()
        self.textEdit_message.raise_()
        self.tabWidget.addTab(self.main, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.comboBox_chose_the_mode = QtWidgets.QComboBox(self.history)
        self.comboBox_chose_the_mode.setGeometry(QtCore.QRect(1120, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.comboBox_chose_the_mode.setFont(font)
        self.comboBox_chose_the_mode.setStyleSheet("border: 2px solid black;")
        self.comboBox_chose_the_mode.setEditable(False)
        self.comboBox_chose_the_mode.setObjectName("comboBox_chose_the_mode")
        self.comboBox_chose_the_mode.addItem("")
        self.comboBox_chose_the_mode.addItem("")
        self.comboBox_chose_the_mode.addItem("")
        self.pushButton_clear = QtWidgets.QPushButton(self.history)
        self.pushButton_clear.setGeometry(QtCore.QRect(1420, 70, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_search = QtWidgets.QPushButton(self.history)
        self.pushButton_search.setGeometry(QtCore.QRect(1310, 70, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_calendar_1 = QtWidgets.QPushButton(self.history)
        self.pushButton_calendar_1.setGeometry(QtCore.QRect(1070, 200, 51, 51))
        self.pushButton_calendar_1.setStyleSheet("QPushButton{border:none;}\n"
"\n"
"")
        self.pushButton_calendar_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../do_an_QT_designer/image/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_calendar_1.setIcon(icon1)
        self.pushButton_calendar_1.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_calendar_1.setObjectName("pushButton_calendar_1")
        self.pushButton_calendar_2 = QtWidgets.QPushButton(self.history)
        self.pushButton_calendar_2.setGeometry(QtCore.QRect(1070, 280, 51, 41))
        self.pushButton_calendar_2.setStyleSheet("QPushButton{border:none;}\n"
"\n"
"")
        self.pushButton_calendar_2.setText("")
        self.pushButton_calendar_2.setIcon(icon1)
        self.pushButton_calendar_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_calendar_2.setObjectName("pushButton_calendar_2")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.history)
        self.dateEdit_1.setGeometry(QtCore.QRect(1120, 130, 161, 41))
        self.dateEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 24), QtCore.QTime(0, 0, 0)))
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.history)
        self.dateEdit_2.setGeometry(QtCore.QRect(1120, 190, 161, 41))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 24), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.tableWidget_account = QtWidgets.QTableWidget(self.history)
        self.tableWidget_account.setGeometry(QtCore.QRect(220, 40, 821, 651))
        self.tableWidget_account.setStyleSheet("")
        self.tableWidget_account.setObjectName("tableWidget_account")
        self.tableWidget_account.setColumnCount(0)
        self.tableWidget_account.setRowCount(0)
        self.pushButton_load = QtWidgets.QPushButton(self.history)
        self.pushButton_load.setGeometry(QtCore.QRect(1320, 130, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_load.setFont(font)
        self.pushButton_load.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_report = QtWidgets.QPushButton(self.history)
        self.pushButton_report.setGeometry(QtCore.QRect(1320, 190, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_report.setFont(font)
        self.pushButton_report.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_report.setObjectName("pushButton_report")
        self.label_75 = QtWidgets.QLabel(self.history)
        self.label_75.setGeometry(QtCore.QRect(1090, 40, 451, 221))
        self.label_75.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_75.setText("")
        self.label_75.setObjectName("label_75")
        self.label_75.raise_()
        self.dateEdit_1.raise_()
        self.comboBox_chose_the_mode.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_search.raise_()
        self.pushButton_calendar_1.raise_()
        self.pushButton_calendar_2.raise_()
        self.dateEdit_2.raise_()
        self.tableWidget_account.raise_()
        self.pushButton_load.raise_()
        self.pushButton_report.raise_()
        self.tabWidget.addTab(self.history, "")
        self.verticalLayout.addWidget(self.tabWidget)
        Gui_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Gui_window)
        self.statusbar.setObjectName("statusbar")
        Gui_window.setStatusBar(self.statusbar)

        self.retranslateUi(Gui_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Gui_window)

    def retranslateUi(self, Gui_window):
        _translate = QtCore.QCoreApplication.translate
        Gui_window.setWindowTitle(_translate("Gui_window", "MainWindow"))
        self.tabWidget.setToolTip(_translate("Gui_window", "qưq"))
        self.tabWidget.setWhatsThis(_translate("Gui_window", "<html><head/><body><p>ssss</p></body></html>"))
        self.label_2.setText(_translate("Gui_window", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">MÔ PHỎNG ĐIỀU KHIỂN MÁY BAY KHÔNG NGƯỜI LÁI <br/>QUẢN LÝ HÀNG TỒN KHO</span></p></body></html>"))
        self.label_6.setText(_translate("Gui_window", "<html><head/><body><p><span style=\" color:#ff0000;\">ĐỒ ÁN TỐT NGHIỆP</span></p></body></html>"))
        self.label_26.setText(_translate("Gui_window", "GVHD: THẦY THS.NGUYỄN ĐỨC HOÀNG"))
        self.label_29.setText(_translate("Gui_window", "SVTH:    BÙI MINH HIẾU                   2011182"))
        self.label_30.setText(_translate("Gui_window", "NGUYỄN VÕ TẤN HẢI       2013076"))
        self.label_25.setText(_translate("Gui_window", "<html><head/><body><p><span style=\" color:#000000;\">TRƯỜNG ĐẠI HỌC BÁCH KHOA TP. HỒ CHÍ MINH</span></p></body></html>"))
        self.label_28.setText(_translate("Gui_window", "<html><head/><body><p><span style=\" color:#000000;\">KHOA ĐIỆN - ĐIỆN TỬ </span></p><p><br/></p></body></html>"))
        self.label_31.setText(_translate("Gui_window", "<html><head/><body><p>BỘ MÔN ĐIỀU KHIỂN TỰ ĐỘNG </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("Gui_window", "Home"))
        self.label_camera.setText(_translate("Gui_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#55007f;\">Camera</span></p></body></html>"))
        self.pushButton_unlock.setText(_translate("Gui_window", "Unlock"))
        self.pushButton_lock.setText(_translate("Gui_window", "Lock"))
        self.pushButton_run.setText(_translate("Gui_window", "RUN"))
        self.pushButton_home.setText(_translate("Gui_window", "HOME"))
        self.pushButton_connect_drone.setText(_translate("Gui_window", "Connect Drone"))
        self.comboBox_choose_location.setItemText(0, _translate("Gui_window", "Chose the Mode"))
        self.comboBox_choose_location.setItemText(1, _translate("Gui_window", "A  Location"))
        self.comboBox_choose_location.setItemText(2, _translate("Gui_window", "All"))
        self.label_location.setText(_translate("Gui_window", "Location"))
        self.textEdit_message.setHtml(_translate("Gui_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:15pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("Gui_window", "MAIN"))
        self.comboBox_chose_the_mode.setItemText(0, _translate("Gui_window", "Chose the Mode"))
        self.comboBox_chose_the_mode.setItemText(1, _translate("Gui_window", "Account"))
        self.comboBox_chose_the_mode.setItemText(2, _translate("Gui_window", "Detected Box "))
        self.pushButton_clear.setText(_translate("Gui_window", "Clear"))
        self.pushButton_search.setText(_translate("Gui_window", "Search"))
        self.dateEdit_1.setDisplayFormat(_translate("Gui_window", "dd/MM/yyyy"))
        self.dateEdit_2.setDisplayFormat(_translate("Gui_window", "dd/MM/yyyy"))
        self.pushButton_load.setText(_translate("Gui_window", "Product infomation"))
        self.pushButton_report.setText(_translate("Gui_window", "Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history), _translate("Gui_window", "HISTORY"))
import pic_logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gui_window = QtWidgets.QMainWindow()
    ui = Ui_Gui_window()
    ui.setupUi(Gui_window)
    Gui_window.show()
    sys.exit(app.exec_())
