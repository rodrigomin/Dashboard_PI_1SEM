import sys
from PyQt5.QtGui import QColor, QTransform, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt
from PyQt5 import uic

def aplicar_sombra(widget, y):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setYOffset(y)
        shadow.setXOffset(0)
        shadow.setColor(QColor(0, 0, 0, 40))
        widget.setGraphicsEffect(shadow)

def animar_hover(widget, offset=4, duration=150):
        widget._anim = QPropertyAnimation(widget, b"pos")
        widget._anim.setDuration(duration)
        widget._anim.setEasingCurve(QEasingCurve.OutCubic)

        original_pos = widget.pos()

        def enterEvent(event):
            widget._anim.stop()
            widget._anim.setStartValue(widget.pos())
            widget._anim.setEndValue(original_pos - QPoint(0, offset))
            widget._anim.start()

        def leaveEvent(event):
            widget._anim.stop()
            widget._anim.setStartValue(widget.pos())
            widget._anim.setEndValue(original_pos)
            widget._anim.start()

        widget.enterEvent = enterEvent
        widget.leaveEvent = leaveEvent

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('front/src/dashboard.ui', self)

        print(self.GRAPH_2.styleSheet())

        self.goLeft.clicked.connect(lambda: self.teste('left'))
        self.goRight.clicked.connect(lambda: self.teste('right'))

        aplicar_sombra(self.Febre, 4)
        aplicar_sombra(self.Nause, 4)
        aplicar_sombra(self.DorCbc, 4)
        aplicar_sombra(self.InputF, 2)
        aplicar_sombra(self.buscar, 4)
        aplicar_sombra(self.div, 4)

        pixmap = QPixmap('../assets/suitcase-medical-solid-full.svg')
        transform = QTransform().rotate(25)
        rotated_pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)
        
        self.BG_ICOMED.setPixmap(rotated_pixmap)

        animar_hover(self.Febre)
        animar_hover(self.Nause)
        animar_hover(self.DorCbc)

    def teste(self, dir):
        if (dir == 'left'):
            print('clicou esquerda')
        else:
            print('clicou direita')




    



if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Fechando App...")