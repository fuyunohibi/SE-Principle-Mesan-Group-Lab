from q1 import *
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("simple_drawing1_tw")

    def paintEvent(self, e):
        super().paintEvent(e)
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))

        p.setBrush(QColor(139, 69, 19))  # Dark brown color for the bear
        p.drawEllipse(250, 200, 200, 200)  # Main body

        p.drawEllipse(300, 150, 100, 100)  # Head

        p.drawEllipse(290, 120, 30, 30)  # Left ear
        p.drawEllipse(380, 120, 30, 30)  # Right ear

        p.setBrush(QColor(0, 0, 0))
        p.drawEllipse(320, 170, 10, 10)  # Left eye
        p.drawEllipse(370, 170, 10, 10)  # Right eye

        p.drawEllipse(345, 200, 10, 10)  # Nose

        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

