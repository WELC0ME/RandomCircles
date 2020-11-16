import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            for i in range(randint(5, 10)):
                qp.setBrush(QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
                radius = randint(5, 25)
                qp.drawEllipse(randint(60, 230), randint(110, 230), radius * 2, radius * 2)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
