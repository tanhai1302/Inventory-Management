# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(1150, 834)
        Form_2.setStyleSheet("/* Styles for the info_frame element */\n"
"#info_frame {\n"
"    background-color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Styles for labels, input fields, and combo boxes inside \"info_frame\" */\n"
"#info_frame QLabel,\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section {\n"
"    font-family: Segoe UI Semibold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Styles for input fields and combo boxes inside */\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"    padding: 4px 5px;\n"
"    border: 1px solid #838383;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* Focus styles for input fields and combo boxes */\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus {\n"
"    border-color: #0055ff;\n"
"}\n"
"\n"
"/* Styles for combo boxes drop-down */\n"
"QComboBox::drop-down {\n"
"    background: transparent;\n"
"    border: none;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"/* Styles for the \'result_frame\' */\n"
"#result_frame {\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"/* Style for border QTableWidget */\n"
"QTableWidget {\n"
"    border-radius: 3px;\n"
"    border: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"/* Style for the header section */\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: left;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"/* Styles for table items */\n"
"QTableWidget::item {\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    color: #000;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"/* Styles for buttons inside the \'function_frame\' */\n"
"#function_frame QPushButton {\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"    background-color: #84e8f7;\n"
"}\n"
"\n"
"/* Style for delete_btn */\n"
"#function_frame #delete_btn {\n"
"    background-color: #ff8183;\n"
"}\n"
"\n"
"/* Hover styles for buttons inside the \'function_frame\' */\n"
"#function_frame QPushButton:hover {\n"
"    border-color: #4c96f7;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"/* Hover styles for the delete_btn */\n"
"#function_frame #delete_btn:hover {\n"
"    border-color: #dc0004;\n"
"}")
        self.frame = QtWidgets.QFrame(Form_2)
        self.frame.setGeometry(QtCore.QRect(-10, 40, 1021, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(30)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(220, 20, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(23)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.info_frame = QtWidgets.QFrame(Form_2)
        self.info_frame.setGeometry(QtCore.QRect(190, 150, 761, 111))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout_2.setContentsMargins(30, 10, 30, 15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.info_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.info_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.info_frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.info_frame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_5 = QtWidgets.QLabel(self.info_frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)
        self.function_frame = QtWidgets.QFrame(Form_2)
        self.function_frame.setGeometry(QtCore.QRect(230, 260, 711, 52))
        self.function_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_frame.setObjectName("function_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.function_frame)
        self.gridLayout_3.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.select_btn = QtWidgets.QPushButton(self.function_frame)
        self.select_btn.setObjectName("select_btn")
        self.gridLayout_3.addWidget(self.select_btn, 0, 2, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.function_frame)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_3.addWidget(self.search_btn, 0, 3, 1, 1)
        self.update_btn = QtWidgets.QPushButton(self.function_frame)
        self.update_btn.setObjectName("update_btn")
        self.gridLayout_3.addWidget(self.update_btn, 0, 1, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.function_frame)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout_3.addWidget(self.delete_btn, 0, 5, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.function_frame)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_3.addWidget(self.add_btn, 0, 0, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(self.function_frame)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout_3.addWidget(self.clear_btn, 0, 4, 1, 1)
        self.result_frame = QtWidgets.QFrame(Form_2)
        self.result_frame.setGeometry(QtCore.QRect(270, 320, 631, 471))
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.tableWidget = QtWidgets.QTableWidget(self.result_frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 471))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Form"))
        self.title_label.setText(_translate("Form_2", "Product information system"))
        self.label_3.setText(_translate("Form_2", "Location"))
        self.label_2.setText(_translate("Form_2", "QR Code"))
        self.label_6.setText(_translate("Form_2", "Status"))
        self.label_7.setText(_translate("Form_2", "Date of import"))
        self.label_5.setText(_translate("Form_2", "Type of goods"))
        self.select_btn.setText(_translate("Form_2", "Select"))
        self.search_btn.setText(_translate("Form_2", "Search"))
        self.update_btn.setText(_translate("Form_2", "Update"))
        self.delete_btn.setText(_translate("Form_2", "Delete"))
        self.add_btn.setText(_translate("Form_2", "Add"))
        self.clear_btn.setText(_translate("Form_2", "Clear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_2", "QR Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_2", "Location"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_2", "Type of goods"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_2", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_2", "Date of import"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_2 = QtWidgets.QWidget()
    ui = Ui_Form_2()
    ui.setupUi(Form_2)
    Form_2.show()
    sys.exit(app.exec_())
