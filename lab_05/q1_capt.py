import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(70, 100), QPoint(100, 110), QPoint(130, 100), QPoint(100, 150),])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),])

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
    
  
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
