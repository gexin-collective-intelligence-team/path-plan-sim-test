# 姓名：jujianqiang
# 2023/12/25 10:50
import json
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QWidget, QFileDialog

from arithmetic.Astar.Map import Map
from arithmetic.Astar.astar import astar
from programResult import programResult


class GridWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        # 多少个格子取决于像素的大小，宽高除以像素的大小等于格子数，需要向下取整 默认值为10 TODO
        self.cell_size = 10
        self.width = 92
        self.height = 40
        # 上述问题解决后需要设置方法，调整格子粒度，重新刷新载入页面
        self.block_map = []
        self.grid_colors = [[QColor(255, 255, 255) for _ in range(self.width)] for _ in range(self.width)]
        self.Map = []
        for i in range(self.height):
            col = []
            for j in range(self.width):
                col.append(1)
            self.Map.append(col)
        self.startPoint = None
        self.endPoint = None
        self.result = None
        self.win_main = main_window

    # 绘图
    def paintEvent(self, event):
        painter = QPainter(self)
        for i in range(self.width):
            for j in range(self.height):
                painter.fillRect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size,
                                 self.grid_colors[i][j])
                painter.drawRect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)

    # 鼠标点击事件
    def mousePressEvent(self, event):
        x = event.pos().x() // self.cell_size
        y = event.pos().y() // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.width:
            if event.button() == Qt.LeftButton:  # 左键
                if (x, y) != self.startPoint and (x, y) != self.endPoint:
                    self.Map[y][x] = (1 if self.Map[y][x] == 0 else 0)
                    if self.grid_colors[x][y] == QColor(255, 255, 255):
                        print(self.Map)
                        self.win_main.printf("添加障碍点：", y, x)
                        self.grid_colors[x][y] = QColor(0, 0, 0)
                    else:
                        self.win_main.printf("取消障碍点：", y, x)
                        self.grid_colors[x][y] = QColor(255, 255, 255)
                self.update()
            if event.button() == Qt.RightButton:
                if self.Map[y][x] == 1:
                    if self.startPoint is None:  # 起点设置
                        self.win_main.printf("添加起始点：", y, x)
                        if self.grid_colors[x][y] == QColor(255, 255, 255):
                            self.grid_colors[x][y] = QColor(255, 0, 0)
                        else:
                            self.win_main.printf("取消起始点：", x, y)
                            self.grid_colors[x][y] = QColor(255, 255, 255)
                        self.startPoint = (y, x)
                        print(self.startPoint)
                    elif self.endPoint is None and self.startPoint != (x, y):  # 终点设置
                        self.win_main.printf("添加终点：", y, x)

                        if self.grid_colors[x][y] == QColor(255, 255, 255):
                            self.grid_colors[x][y] = QColor(0, 255, 0)
                        else:
                            self.win_main.printf("取消终点：", x, y)
                            self.grid_colors[x][y] = QColor(255, 255, 255)
                        self.endPoint = (y, x)
                        print(self.endPoint)
                self.update()

    # 清空起始点坐标以及颜色的方法
    def clearStartAndEnd(self):
        # print(self.startPoint)
        # print(self.endPoint)
        if self.startPoint:
            x, y = self.startPoint
            self.startPoint = None
            self.grid_colors[y][x] = QColor(255, 255, 255)
            self.win_main.printf("清除起始点：", x, y)

        if self.endPoint:
            # print(self.Map)
            x, y = self.endPoint
            self.endPoint = None
            self.grid_colors[y][x] = QColor(255, 255, 255)
            self.win_main.printf("清除终点：", x, y)

        if self.result is not None:
            for i in self.result:
                if i != self.startPoint and i != self.endPoint:
                    self.grid_colors[i[1]][i[0]] = QColor(255, 255, 255)
        self.update()

    # 清空地图方法
    def clearObstacles(self):
        if self.result is not None:
            for i in self.result:
                if i != self.startPoint and i != self.endPoint:
                    self.grid_colors[i[1]][i[0]] = QColor(255, 255, 255)
        for i in range(self.height):
            for j in range(self.width):
                if self.Map[i][j] == 0:
                    self.Map[i][j] = 1
                    if self.grid_colors[j][i] == QColor(0, 0, 0):
                        self.grid_colors[j][i] = QColor(255, 255, 255)
        self.update()
        self.clearStartAndEnd()
        self.win_main.printf("已清空地图！", None, None)
        # print(self.Map)

    def startPath(self):
        window = programResult(self.height, self.width, self.cell_size, self.startPoint, self.endPoint, self.Map)
        window.run()

    # 路径规划调用方法 后期根据不同的用户选择，运行不同的算法，现阶段采用简单的AStar算法实现路径规划
    # def startPath(self):
    #     # print("aaa")
    #     map = Map(self.Map, self.startPoint[0], self.startPoint[1], self.endPoint[0], self.endPoint[1])
    #     self.result = astar(map)
    #     self.result.reverse()
    #     # print(len(self.result))
    #     if len(self.result) > 0:
    #         for i in self.result:
    #             if i != self.startPoint and i != self.endPoint:
    #                 self.grid_colors[i[1]][i[0]] = QColor(255, 255, 0)
    #         self.update()
    #     else:
    #         self.win_main.printf("无可规划路径",None,None)
    #     self.win_main.printf("AStar算法路径规划长度：%d,路径为 %s" %(len(self.result),self.result),None,None)

    # 修改地图方法
    def modifyMap(self,size):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.Map[i][j] == 0:
                    count += 1
        if self.result is None and self.startPoint is None and self.endPoint is None and count > 0:
            if isinstance(size, str):
                self.win_main.printf("请输入正确的分辨率！", None, None)
            if int(size) >= 0:
                new_size = int(size)
                self.cell_size = new_size
                self.width = int(920 / self.cell_size)
                self.height = int(399 / self.cell_size)
                self.Map = []
                for i in range(self.height):
                    col = []
                    for j in range(self.width):
                        col.append(1)
                    self.Map.append(col)
                self.win_main.printf("分辨率调整成功！", None, None)
                self.update()
            else:
                self.win_main.printf("请输入正确的分辨率！", None, None)
        else:
            self.win_main.printf("当前地图已起始点或障碍点不可调整地图分辨率，请清空地图后再次调整分辨率！",None,None)
    # 默认地图
    def defaultMap(self):
        if self.result is None:
            if self.cell_size == 10:
                self.win_main.printf("该地图已经是默认地图！", None, None)
            else:
                self.cell_size = 10
                self.width = int(920 / self.cell_size)
                self.height = int(399 / self.cell_size)
                self.Map = []
                for i in range(self.height):
                    col = []
                    for j in range(self.width):
                        col.append(1)
                    self.Map.append(col)
                self.win_main.printf("分辨率调整成功！", None, None)
                self.update()
        else:
            self.win_main.printf("当前地图已规划结果不可调整地图分辨率率", None, None)

    # 保存地图的方法,我们需要保存的是地图的起始点坐
    # 标,障碍物坐标,以及运行结果的坐标,当我们点击打开文件时会自动识别并展示地图的效果
    # 保存地图的方法现在只是保存的地图的起始点障碍以及规划后的路径结果
    def saveMap(self):
        # 创建文件对话框
        dialog = QFileDialog()
        # 设置文件对话框为保存文件模式
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        # 设置对话框标题
        dialog.setWindowTitle('保存地图')
        # 设置文件过滤器
        dialog.setNameFilter('地图文件 (*.txt)')
        # 设置默认文件名，包含文件类型后缀
        dialog.setDefaultSuffix('txt')

        # 打开文件对话框，并返回保存的文件路径
        file_path, _ = dialog.getSaveFileName(self, '保存地图', '', '地图文件 (*.txt)')
        for i in range(self.height):
            for j in range(self.width):
                if self.Map[i][j] == 0:
                    self.block_map.append((i, j))
        # print(self.block_map)


        if file_path:
            data = {
                'startPoint': self.startPoint,
                'endPoint': self.endPoint,
                'map': self.block_map,
                'result': self.result,
                'cell_size': self.cell_size
            }
            with open(file_path, 'w') as file:
                json.dump(data, file)
            self.win_main.printf("地图已成功保存！", None, None)
            # 关闭文件保存对话框
            # self.win_main.quit()

    # 下载地图模板的方法，因为平台有打开文件的功能，但不是每个人都是从平台保存的地图，那么就需要提高一个模板让用户使用
    def downLoadModelMap(self):
        # 创建文件对话框
        dialog = QFileDialog()
        # 设置文件对话框为保存文件模式
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        # 设置对话框标题
        dialog.setWindowTitle('保存地图')
        # 设置文件过滤器
        dialog.setNameFilter('地图文件 (*.txt)')
        # 设置默认文件名，包含文件类型后缀
        dialog.setDefaultSuffix('txt')

        # 打开文件对话框，并返回保存的文件路径
        file_path, _ = dialog.getSaveFileName(self, '保存地图', '', '地图文件 (*.txt)')
        if file_path:
            data = {
                'startPoint': None,
                'endPoint': None,
                'map': [],
                'result': None,
                'cell_size': 10
            }
            with open(file_path, 'w') as file:
                json.dump(data, file)
            self.win_main.printf("地图模板已成功下载！", None, None)
            # 关闭文件保存对话框
            # self.win_main.quit()

    # 打开地图的方法其实和保存地图的方法相似,但是我们要如何将拿来的文件识别出来,如果不是我们可以识别的地图我们应该提示用户,并且让用户下载模板信息
    def openMap(self):
        # 创建文件对话框
        dialog = QFileDialog()
        # 设置文件对话框标题
        dialog.setWindowTitle('打开地图')
        # 设置文件过滤器
        dialog.setNameFilter('地图文件 (*.txt *.csv)')

        # 打开文件对话框，并返回选择的文件路径
        file_path, _ = dialog.getOpenFileName(self, '打开地图', '', '地图文件 (*.txt *.csv)')
        # 打开地图前需要先清空地图
        self.clearObstacles()
        # 如果选择了文件路径，则进行地图识别的操作
        if file_path:
            if file_path:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    # 解析地图数据，并赋值给属性
                    self.startPoint = data.get('startPoint')
                    self.endPoint = data.get('endPoint')
                    self.block_map = data.get('map')
                    self.result = data.get('result')
                    self.cell_size = data.get('cell_size')
                # 获取到我们保存的地图数据后,我们需要展示地图的效果,并且需要判断障碍,起始点,规划路径等结果是否为空,避免不需要的操作
                # 清空地图后，重新设置地图分辨率
                self.modifyMap(int(self.cell_size))
                # 将障碍点设置在地图中
                for i in range(len(self.block_map)):
                    self.Map[self.block_map[i][0]][self.block_map[i][1]] = 0
                # 根据新地图绘图
                for i in range(self.height):
                    for j in range(self.width):
                        if self.Map[i][j] == 0:
                            if self.grid_colors[j][i] == QColor(255, 255, 255):
                                self.grid_colors[j][i] = QColor(0, 0, 0)
                    self.update()
                # 绘制起点
                if self.startPoint is not None:
                    self.grid_colors[self.startPoint[1]][self.startPoint[0]] = QColor(255, 0, 0)
                self.update()
                # 绘制终点
                if self.endPoint is not None:
                    # print(self.endPoint[0])
                    # print(self.endPoint[1])
                    self.grid_colors[self.endPoint[1]][self.endPoint[0]] = QColor(0, 255, 0)
                self.update()
                # 绘制规划结果
                if self.result is not None:
                    for i in range(len(self.result)):
                        if self.grid_colors[self.result[i][1]][self.result[i][0]] == QColor(255, 255, 255):
                            self.grid_colors[self.result[i][1]][self.result[i][0]] = QColor(255, 255, 0)
                        self.update()
                    # 更新地图显示
                self.update()
                self.win_main.printf("地图已成功打开！", None, None)

    def painting_ori(self, x, y):  # 这个和点击画起始点功能冲突 暂时分隔这两个功能，假设输入起始点前地图为空，所以直接填色即可
        if self.Map[y][x] == 1:
            if self.startPoint is None:  # 起点设置
                self.win_main.printf("添加起始点：", y, x)
                if self.grid_colors[x][y] == QColor(255, 255, 255):
                    self.grid_colors[x][y] = QColor(255, 0, 0)
                self.startPoint = (y, x)
                print(self.startPoint)
            else:
                self.win_main.printf("已设置起点！",None,None)
            self.update()

    def painting_end(self, x1, y1):  # 假设输入终止点前地图为空，所以直接填色即可
        if self.Map[y1][x1] == 1:
            if self.endPoint is None and self.startPoint != (x1, y1):  # 终点设置
                self.win_main.printf("添加终点：", y1, x1)

                if self.grid_colors[x1][y1] == QColor(255, 255, 255):
                    self.grid_colors[x1][y1] = QColor(0, 255, 0)
                self.endPoint = (y1, x1)
            else:
                self.win_main.printf("已设置终点！", None, None)
                print(self.endPoint)
            self.update()

    # 随机绘制障碍物
    def paint_block(self, x1, y1, x2, y2):
        for i in range(3):
            x = random.randint(x1, x2)
            y = random.randint(y1, y2)
            z = random.randint(10, 15)
            for j in range(z):
                if (x, y) != self.startPoint and (x, y) != self.endPoint and x < 100 and y < 40:
                    self.Map[y][x] = 0
                    if self.grid_colors[x][y] == QColor(255, 255, 255):
                        print(self.Map)
                        self.win_main.printf("添加障碍点：", y, x)
                        self.grid_colors[x][y] = QColor(0, 0, 0)
                    x = x + 1
                    # else:
                    #     self.win_main.printf("取消障碍点：", y, x)
                    #     self.grid_colors[x][y] = QColor(255, 255, 255)
        self.update()
        for i in range(4):
            x = random.randint(x1, x2)
            y = random.randint(y1, y2)
            z = random.randint(10, 15)
            for j in range(z):
                if (x, y) != self.startPoint and (x, y) != self.endPoint and x < 100 and y < 40:
                    self.Map[y][x] = 0
                    if self.grid_colors[x][y] == QColor(255, 255, 255):
                        print(self.Map)
                        self.win_main.printf("添加障碍点：", y, x)
                        self.grid_colors[x][y] = QColor(0, 0, 0)
                    y = y + 1
                    # else:
                    #     self.win_main.printf("取消障碍点：", y, x)
                    #     self.grid_colors[x][y] = QColor(255, 255, 255)

        self.update()

    # 根据数量生成随机障碍物新方法
    def randomBlock(self,num):
        for i in range(num):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if (x, y) != self.startPoint and (x, y) != self.endPoint and self.Map[y][x] != 0:
                    self.Map[y][x] = 0 # 设置障碍物
                    self.grid_colors[x][y] = QColor(0, 0, 0)
                    break
        print(self.Map)
        self.update()

    # 随机起始点方法
    def generateRandomStart(self):
        if self.startPoint is None:
            # 生成随机的x和y坐标
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.startPoint = (y, x)
            self.win_main.printf("添加起始点：", y, x)
            if self.grid_colors[x][y] == QColor(255, 255, 255):
                self.grid_colors[x][y] = QColor(255, 0, 0)
            self.update()
        else:
            self.win_main.printf("error: 已经设置起点！", None, None)

        if self.endPoint is None and self.endPoint != self.startPoint:
            # 生成随机的x和y坐标
            x_1 = random.randint(0, self.width - 1)
            y_1 = random.randint(0, self.height - 1)
            self.endPoint = (y_1,x_1)
            self.win_main.printf("添加终点：",y_1,x_1)
            if self.grid_colors[x_1][y_1] == QColor(255, 255, 255):
                self.grid_colors[x_1][y_1] = QColor(0, 255, 0)
            self.update()
        else:
            self.win_main.printf("error: 已经设置终点！", None, None)
        self.update()

