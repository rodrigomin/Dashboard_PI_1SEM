from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QColor

class GlassCard(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_shadow()
        self.setup_animation()

    def setup_shadow(self):

        self.shadow = QGraphicsDropShadowEffect()

        self.shadow.setBlurRadius(15)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor(0, 0, 0, 40))

        self.setGraphicsEffect(self.shadow)


    def setup_animation(self):
        self.anim = QPropertyAnimation(self, b"pos")

        self.anim.setDuration(150)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        

    def enterEvent(self, event):

        self.anim.stop()

        self.anim.setStartValue(self.pos())
        self.anim.setEndValue(self.pos() - QPoint(0, 4))

        self.anim.start()

    def leaveEvent(self, event):

        self.anim.stop()

        self.anim.setStartValue(self.pos())
        self.anim.setEndValue(self.pos() + QPoint(0,4))


        self.anim.start()
