import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton


class AlgorithmList(QWidget):
    def __init__(self):
        super().__init__()

        # 窗口标题
        self.setWindowTitle('算法列表')
        # 窗口固定大小
        self.setFixedSize(800, 400)

        # 创建表格控件
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # 设置列数，这里是四列
        self.table.setHorizontalHeaderLabels(['算法', '接口名', '接口规范', '描述'])  # 设置表头

        # 算法数据
        self.algorithms = [
            ('AStar', '......', '...', '......'),
            ('RRT', '......', '...', '......'),
            ('Dijkstra', '......', '...', '......')
        ]

        # 设置行数为算法数据的长度
        self.table.setRowCount(len(self.algorithms))

        # 在表格中填充数据
        for row, algorithm in enumerate(self.algorithms):
            algorithm_name = QTableWidgetItem(algorithm[0])  # 算法名称
            algorithm_interface = QTableWidgetItem(algorithm[1])  # 算法接口名
            algorithm_specification = QTableWidgetItem(algorithm[2])  # 算法接口规范
            algorithm_desc = QTableWidgetItem(algorithm[3])  # 算法描述

            self.table.setItem(row, 0, algorithm_name)
            self.table.setItem(row, 1, algorithm_interface)
            self.table.setItem(row, 2, algorithm_specification)
            self.table.setItem(row, 3, algorithm_desc)

        # 设置表格为自适应大小
        self.table.setColumnWidth(0, 150)  # 第一列宽度为 150 像素
        self.table.setColumnWidth(1, 250)  # 第二列宽度为 250 像素
        self.table.setColumnWidth(2, 200)  # 第三列宽度为 200 像素
        self.table.setColumnWidth(3, 200)  # 第四列宽度为 200 像素

        # 创建垂直布局，并将表格添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        # 创建添加新数据按钮
        add_button = QPushButton("添加新算法")
        add_button.clicked.connect(self.add_new_data)
        layout.addWidget(add_button)

        # 创建保存按钮
        save_button = QPushButton("保存")
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def add_new_data(self):
        # 在算法数据列表中添加新数据
        self.algorithms.append(('New Algorithm', '...', '...', '...'))

        # 更新表格行数
        self.table.setRowCount(len(self.algorithms))

        # 在表格中填充新数据
        row = len(self.algorithms) - 1
        algorithm_name = QTableWidgetItem(self.algorithms[row][0])  # 算法名称
        algorithm_interface = QTableWidgetItem(self.algorithms[row][1])  # 算法接口名
        algorithm_specification = QTableWidgetItem(self.algorithms[row][2])  # 算法接口规范
        algorithm_desc = QTableWidgetItem(self.algorithms[row][3])  # 算法描述

        self.table.setItem(row, 0, algorithm_name)
        self.table.setItem(row, 1, algorithm_interface)
        self.table.setItem(row, 2, algorithm_specification)
        self.table.setItem(row, 3, algorithm_desc)

    def save_data(self):
        rows = self.table.rowCount()
        columns = self.table.columnCount()

        data = []

        # 遍历表格，获取数据
        for row in range(rows):
            row_data = []
            for column in range(columns):
                item = self.table.item(row, column)
                if item is not None:
                    row_data.append(item.text())
            data.append(row_data)

        # 打印数据
        for row in data:
            print(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    algorithm_list = AlgorithmList()
    algorithm_list.show()
    sys.exit(app.exec_())