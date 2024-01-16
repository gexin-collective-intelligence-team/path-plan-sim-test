import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QApplication, QFileDialog
from AlgorithmList import AlgorithmList
from GridWidget import GridWidget


class Ui_MainWindow(object):
    windows = []  # 存储所有创建的窗口实例

    def setupUi(self, MainWindow, grid_widget):
        self.loginWindow_new = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 850))
        # MainWindow.setStyleSheet("background-color: rgb(0, 191, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input.setPlaceholderText("输入起始点横纵坐标(x,y):")
        self.text_input.setGeometry(QtCore.QRect(430, 425, 200, 25))
        text = self.text_input.text()
        # 横坐标输入框
        self.text_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input_2.setPlaceholderText("输入终点横纵坐标(x,y):")
        self.text_input_2.setGeometry(QtCore.QRect(640, 425, 200, 25))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        # self.pushButton.setGeometry(QtCore.QRect(40, 450, 75, 23))
        # 纵坐标输入框
        self.pushButton.setGeometry(QtCore.QRect(130, 425, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.text_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(40, 520, 921, 251))
        self.text_result.setObjectName("text_result")
        # 开始规划按钮
        self.pushButton_new = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(40, 450, 75, 23))
        self.pushButton_new.setGeometry(QtCore.QRect(40, 425, 75, 25))
        self.pushButton_new.setObjectName("pushButton_new")
        self.pushButton_new.clicked.connect(self.startPath)
        # 清除起始点按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 425, 75, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.clicked.connect(self.clearStartAndEnd)
        # 清除起始点方法链接
        self.pushButton_3.clicked.connect(grid_widget.clearStartAndEnd)
        # 清楚所有障碍方法链接
        self.pushButton.clicked.connect(grid_widget.clearObstacles)
        # self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox.setGeometry(QtCore.QRect(310, 450, 71, 21))
        # self.checkBox.setObjectName("checkBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 921, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.combo_arithmetic = QtWidgets.QComboBox(self.centralwidget)
        self.combo_arithmetic.setGeometry(QtCore.QRect(310, 425, 100, 25))
        self.combo_arithmetic.setObjectName("combo_arithmetic")
        self.combo_arithmetic.addItem("")
        self.combo_arithmetic.addItem("")
        self.combo_arithmetic.addItem("")
        self.combo_arithmetic.addItem("")
        self.combo_arithmetic.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLoadTest = QtWidgets.QAction(MainWindow)
        self.actionLoadTest.setObjectName("actionLoadTest")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.label_map = QtWidgets.QLabel(self.centralwidget)
        self.label_map.setGeometry(QtCore.QRect(40, 455, 54, 21))
        self.label_map.setObjectName("label_map")

        self.label_map_block = QtWidgets.QLabel(self.centralwidget)
        self.label_map_block.setGeometry(QtCore.QRect(40, 480, 70, 21))
        self.label_map_block.setObjectName("label_map_block")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(85, 455, 51, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(10))

        self.lineEdit_block = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_block.setGeometry(QtCore.QRect(110, 480, 90, 21))
        self.lineEdit_block.setObjectName("lineEdit_block")
        self.lineEdit_block.setPlaceholderText("请输入障碍物的数量")
        self.lineEdit_block.setText(str(50))

        self.btn_modifyMap = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modifyMap.setGeometry(QtCore.QRect(150, 455, 75, 23))
        self.btn_modifyMap.setObjectName("btn_modifyMap")
        # 调整地图的粒度
        self.btn_modifyMap.clicked.connect(lambda: grid_widget.modifyMap(int(self.lineEdit.text())))
        # 默认地图按钮
        self.btn_default = QtWidgets.QPushButton(self.centralwidget)
        self.btn_default.setGeometry(QtCore.QRect(230, 455, 75, 23))
        self.btn_default.setObjectName("btn_default")
        # 恢复地图默认粒度
        self.btn_default.clicked.connect(grid_widget.defaultMap)
        # 打开地图的方法
        self.actionOpen.triggered.connect(grid_widget.openMap)
        # 输入起始点确认按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 425, 75, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ori_end_input)
        # 随机障碍物按钮
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 480, 80, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.clicked.connect(self.block_click)
        self.pushButton_5.clicked.connect(lambda:grid_widget.randomBlock(int(self.lineEdit_block.text())))
        # 随机起始点按钮
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 480, 80, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(grid_widget.generateRandomStart)
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        # 点击菜单连接方法
        self.actionCreate.triggered.connect(self.openNewWindow)
        # 点击菜单退出方法
        self.actionExit.triggered.connect(self.loginOut)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        # 保存地图的方法
        self.actionSave.triggered.connect(grid_widget.saveMap)

        self.createArithmetic = QtWidgets.QAction(MainWindow)
        self.createArithmetic.setObjectName("createArithmetic")

        self.createArithmetic.triggered.connect(self.openArithmeticList)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")

        # 版本信息弹出框链接
        self.actionVersion.triggered.connect(self.versionInformation)

        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        # 帮助手册弹出框链接
        self.actionhelp.triggered.connect(self.helpInfo)
        self.actionmodel = QtWidgets.QAction(MainWindow)
        self.actionmodel.setObjectName("actionmodel")

        # 下载地图模板
        self.actionmodel.triggered.connect(grid_widget.downLoadModelMap)
        self.actionArithmeticList = QtWidgets.QAction(MainWindow)
        self.actionArithmeticList.setObjectName("actionArithmeticList")
        self.actionArithmeticList.triggered.connect(self.openArithmeticList)
        self.menu.addAction(self.actionCreate)
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.createArithmetic)
        self.menu.addAction(self.actionmodel)
        self.menu.addAction(self.actionArithmeticList)
        self.menu_5.addAction(self.actionExit)
        self.menu_5.addAction(self.actionVersion)
        self.menu_5.addAction(self.actionhelp)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.toolBar.addAction(self.actionCreate)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionmodel)
        self.toolBar.addAction(self.actionhelp)
        self.toolBar.addAction(self.actionArithmeticList)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.grid_widget = grid_widget

    # 文本框输出提示信息
    def printf(self, msg, x, y):
        if x is None and y is None:
            self.text_result.append("%s" % msg)
        else:
            self.text_result.append("%s(%d:%d)" % (msg, x, y))

    # 创建新窗口方法
    def openNewWindow(self):
        new_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        grid_widget = GridWidget(ui)
        ui.setupUi(new_window, grid_widget)

        new_window.setWindowTitle('基于Pygame的路径规划算法仿真平台')
        # 添加地图
        ui.layout.addWidget(grid_widget)
        new_window.show()
        self.windows.append(new_window)  # 将新创建的窗口实例添加到列表中

    # 退出登录
    def loginOut(self):
        self.close()

    # 版本信息弹出框
    def versionInformation(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("基于Pygame的路径规划算法仿真平台V1.0")
        message_box.setText(
            "路径规划算法仿真平台可以帮助实际应用中的路径规划问题，如无人车、无人机、物流配送等领域的规划和优化。通过仿真平台，可以提前预测和分析路径规划算法在实际环境中的表现，从而减少实际试验的成本和风险。同时，仿真平台还可以为实际应用中的路径规划算法提供实时的优化和调整，以满足不同场景和需求的要求。"
            "路径规划仿真平台V1.0版本是指一种软件工具，可以模拟路径，通过路径规划算法计算最优路径，并可视化显示路径和相关参数。用户可以通过输入环境地图和调整参数等方式，对仿真平台进行操作和控制。")
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.button(QMessageBox.Ok).setFixedSize(100, 40)  # 设置按钮尺寸
        message_box.setFixedSize(800, 800)  # 设置提示框尺寸

        message_box.exec()

    # 版本信息弹出框
    def helpInfo(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("基于Pygame的路径规划算法仿真平台V1.0帮助手册")
        message_box.setText(
            "路径规划仿真平台V1.0版本是指一种软件工具，可以模拟路径，通过路径规划算法计算最优路径，并可视化显示路径和相关参数。用户可以通过输入环境地图和调整参数等方式，对仿真平台进行操作和控制。"
            "仿真平台的使用：本平台使用手动设置起点、终点与障碍点的位置，通过鼠标左键设置障碍点，鼠标右键点击第一次为红色起点点击第二次为绿色终点，地图是可以实时清空和刷新的，只要用户对地图进行改变"
            "平台就会自动刷新，并且本平台采用可以手动调整地图的粒度大小的，但是建议用户采用的地图粒度大小在10-50区间为最佳效果。")
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.button(QMessageBox.Ok).setFixedSize(100, 40)  # 设置按钮尺寸
        message_box.setFixedSize(800, 800)  # 设置提示框尺寸
        message_box.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于Pygame的路径规划算法仿真平台"))
        self.pushButton.setText(_translate("MainWindow", "清空地图"))
        self.text_result.setPlaceholderText(_translate("MainWindow", "输出路径规划结果"))
        self.text_result.append(
            "欢迎来到基于Pygame的路径规划算法仿真平台，以下是路径规划的结果仅供大家参考（右键按第一次是起点第二次是终点，左键设置起点）：")
        self.text_result.append("红色为起点、绿色为终点、黑色为障碍点，平台具体方法请点击帮助手册查看！")
        self.pushButton_new.setText(_translate("MainWindow", "开始规划"))
        self.pushButton_3.setText(_translate("MainWindow", "清空起始点"))
        # self.checkBox.setText(_translate("MainWindow", "AStar算法"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_5.setTitle(_translate("MainWindow", "关于"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoadTest.setText(_translate("MainWindow", "压力测试"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionOpen.setText(_translate("MainWindow", "打开文件"))
        self.actionCreate.setText(_translate("MainWindow", "新建窗口"))
        self.actionSave.setText(_translate("MainWindow", "保存地图"))
        self.createArithmetic.setText(_translate("MainWindow", "新增算法"))
        self.actionVersion.setText(_translate("MainWindow", "版本信息"))
        self.actionhelp.setText(_translate("MainWindow", "帮助手册"))
        self.actionmodel.setText(_translate("MainWindow", "下载地图模板"))
        self.label_map.setText(_translate("MainWindow", "分辨率："))
        self.label_map_block.setText(_translate("MainWindow", "随机障碍物："))
        self.btn_modifyMap.setText(_translate("MainWindow", "调整"))
        self.btn_default.setText(_translate("MainWindow", "默认"))
        self.actionArithmeticList.setText(_translate("MainWindow", "算法列表"))
        self.pushButton_4.setText(_translate("MainWindow", "生成"))
        self.pushButton_5.setText(_translate("MainWindow", "随机障碍物"))
        self.pushButton_6.setText(_translate("MainWindow", "随机起始点"))
        self.combo_arithmetic.setItemText(0, _translate("MainWindow", "请选择算法"))
        self.combo_arithmetic.setItemText(1, _translate("MainWindow", "Astar"))
        self.combo_arithmetic.setItemText(2, _translate("MainWindow", "RRT"))
        self.combo_arithmetic.setItemText(3, _translate("MainWindow", "Dijkstra"))
        self.combo_arithmetic.setItemText(4, _translate("MainWindow", "4"))

    # 路径规划
    def startPath(self):
        # 根据不同的算法
        if self.checkBox.isChecked():
            self.grid_widget.startPath()

    def ori_end_input(self):  # 输入起始点终点函数
        coordinate = self.text_input.text()
        print(coordinate)
        pattern = r"\((\d+),(\d+)\)"  # 匹配坐标的正则表达式模式
        match = re.match(pattern, coordinate)
        print(match)
        if match:
            keyx = int(match.group(1))  # 提取横坐标
            keyy = int(match.group(2))  # 提取纵坐标
            print("起点横坐标:", keyx)
            print("起点纵坐标:", keyy)
            grid_widget.painting_ori(keyx, keyy)  # 目前执行到这里程序就结束了，应该是调用有问题
        else:
            print("坐标格式不正确")
        coordinate_2 = self.text_input_2.text()
        # print(coordinate_2)
        pattern_2 = r"\((\d+),(\d+)\)"  # 匹配坐标的正则表达式模式
        match_2 = re.match(pattern, coordinate_2)
        if match_2:
            # global keyx_2, keyy_2
            keyx_2 = int(match_2.group(1))  # 提取横坐标
            keyy_2 = int(match_2.group(2))  # 提取纵坐标
            print("终点横坐标:", keyx_2)
            print("终点纵坐标:", keyy_2)
            grid_widget.painting_end(keyx_2, keyy_2)
        else:
            print("坐标格式不正确")

    # 点击随机生成障碍物按钮
    def block_click(self):
        coordinate = self.text_input.text()
        pattern = r"\((\d+),(\d+)\)"  # 匹配坐标的正则表达式模式
        match = re.match(pattern, coordinate)
        keyx = int(match.group(1))  # 提取横坐标
        keyy = int(match.group(2))  # 提取纵坐标
        # 引用上一个类的函数
        coordinate_2 = self.text_input_2.text()
        # print(coordinate_2)
        pattern_2 = r"\((\d+),(\d+)\)"  # 匹配坐标的正则表达式模式
        match_2 = re.match(pattern, coordinate_2)
        keyx_2 = int(match_2.group(1))  # 提取横坐标
        keyy_2 = int(match_2.group(2))  # 提取纵坐标
        grid_widget.paint_block(keyx, keyy, keyx_2, keyy_2)
        # for _ in range(250):  # 随机选择若干个格子变黑
        #     row = random.randint(0, self.grid_widget.rows - 1)
        #     col = random.randint(0, self.grid_widget.columns - 1)
        #     label = self.grid_widget.layout().itemAtPosition(row, col).widget()
        #     label.setStyleSheet("background-color: black")

    def openArithmeticList(self):
        self.algorithm_list = AlgorithmList()
        self.algorithm_list.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    mainWindow = QtWidgets.QMainWindow()
    grid_widget = GridWidget(ui)
    ui.setupUi(mainWindow, grid_widget)
    # 添加地图
    ui.layout.addWidget(grid_widget)
    mainWindow.show()
    sys.exit(app.exec())
