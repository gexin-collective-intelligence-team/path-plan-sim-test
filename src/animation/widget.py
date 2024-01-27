import sys

import pygame
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from .surface import Surface


class AnimationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.surface = Surface()
        self.w = self.surface.get_width()
        self.h = self.surface.get_height()
        self.data = self.surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)
        self.frame = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)
        self.start_timer()

    # sloth
    def update_pyqt(self):
        self.data = self.surface.get_buffer().raw
        self.image = QImage(self.data, self.w, self.h, QImage.Format_RGB32)

    def update_pygame(self):
        # sur = pygame.Surface((640, 480))
        # sur.fill((64, 128, 192, 224))
        # pygame.draw.circle(sur, (55, 11, 55, 111), (self.mu, self.mu), 50)
        self.surface.update()
        self.update_pyqt()
        # self.surface.update()

    def next_frame(self):
        self.frame += 1
        # print(self.mu)
        self.update_pygame()
        self.update()

    def start_timer(self):
        self.timer.start(10)

    def end_timer(self):
        self.timer.stop()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, surface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedWidth(900)
        self.setFixedHeight(900)
        self.surface = surface
        self.img = AnimationWidget(self.surface)

        self.setCentralWidget(self.img)

        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This is an example button')
        self.button.move(800, 70)

        self.button.clicked.connect(self.hago_algo)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.hago_algo)
        # self.start_timer()

        self.mu = 0

    def update_pygame(self):
        sur = pygame.Surface((640, 480))
        sur.fill((64, 128, 192, 224))
        pygame.draw.circle(sur, (55, 11, 55, 111), (self.mu, self.mu), 50)
        self.img.update_pyqt(sur)
        # self.img = AnimationWidget(self.animation_widget)

    def hago_algo(self):
        self.mu += 1
        # print(self.mu)
        self.update_pygame()
        self.update()

    def start_timer(self):
        self.timer.start(10)

    def end_timer(self):
        self.timer.stop()


if __name__ == '__main__':
    pygame.init()

    s = pygame.Surface((640, 480))
    s.fill((64, 128, 192, 224))
    pygame.draw.circle(s, (255, 255, 255, 255), (100, 100), 50)

    app = QApplication(sys.argv)
    w = MainWindow(s)
    w.show()
    app.exec_()
