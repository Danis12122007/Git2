import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QRectF

import random


class Git2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        x = random.randint(0, 400)
        y = random.randint(0, 300)
        r = random.randint(0, 100)
        painter.drawEllipse(QRectF(x, y, r, r))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Git2()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
