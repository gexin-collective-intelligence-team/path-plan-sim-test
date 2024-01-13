from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QMessageBox

from MainWindow import Ui_MainWindow
from GridWidget import GridWidget


class Ui_Form(object):
    def setupUi(self, Form):
        self.mainWindow_new = None  # 新窗口对象
        Form.setObjectName("Form")
        Form.resize(580, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(580, 400))
        Form.setMaximumSize(QtCore.QSize(580, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 211, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./img/logo.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 70, 281, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edt_username = QtWidgets.QLineEdit(Form)
        self.edt_username.setGeometry(QtCore.QRect(300, 160, 171, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_username.sizePolicy().hasHeightForWidth())
        self.edt_username.setSizePolicy(sizePolicy)
        self.edt_username.setObjectName("edt_username")
        self.edt_password = QtWidgets.QLineEdit(Form)
        self.edt_password.setGeometry(QtCore.QRect(300, 200, 171, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_password.sizePolicy().hasHeightForWidth())
        self.edt_password.setSizePolicy(sizePolicy)
        self.edt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edt_password.setObjectName("edt_password")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(320, 270, 111, 23))

        self.btn_login.clicked.connect(self.loginOn)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setObjectName("btn_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "路径规划算法仿真平台"))
        self.edt_username.setPlaceholderText(_translate("Form", "用户名"))
        self.edt_password.setPlaceholderText(_translate("Form", "密码"))
        self.btn_login.setText(_translate("Form", "登录平台"))


    #  登录成功后跳转主窗口方法 默认账号密码： admin
    def loginOn(self):
        username = self.edt_username.text().strip()
        password = self.edt_password.text().strip()
        if username == 'admin' and password == 'admin':
            if self.mainWindow_new is None:
                # 创建新的窗口实例
                self.mainWindow_new = QMainWindow()
                ui_main = Ui_MainWindow()
                grid_widget = GridWidget(ui_main)
                ui_main.setupUi(self.mainWindow_new,grid_widget)

                # 添加地图

                ui_main.layout.addWidget(grid_widget)

            self.mainWindow_new.show()
            mainWindow.hide()
        else:
            error_message = "请仔细检查用户名与密码"
            QMessageBox.critical(mainWindow, "错误提示", error_message, QMessageBox.Ok)

if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui=Ui_Form()
    mainWindow=QtWidgets.QMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

