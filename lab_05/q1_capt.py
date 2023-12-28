import sys
from q1 import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

  
class Simple_drawing_window1(Simple_drawing_window):
    def paintEvent(self, e):
        super().paintEvent(e)
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPolygon([QPoint(350, 100), QPoint(370, 150), QPoint(400, 150), QPoint(375, 175), QPoint(390, 220), QPoint(350, 190), QPoint(310, 220), QPoint(325, 175), QPoint(300, 150), QPoint(330, 150),])
        
        p.end()

        
def main():
    app = QApplication(sys.argv)
    
    window_1 = Simple_drawing_window1()
    window_1.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
