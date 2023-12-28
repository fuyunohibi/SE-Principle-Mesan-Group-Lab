from q1 import *
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("simple_drawing1_tw")

    def paintEvent(self, e):
        super().paintEvent(e)
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.drawRect(300,200,200,200)
        p.drawPolygon([QPoint(300,200), QPoint(500,200), QPoint(400,100)])
        p.drawRect(350,300,100,100 )
        p.end()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

