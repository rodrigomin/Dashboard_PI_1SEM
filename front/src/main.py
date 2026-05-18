import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic

import seaborn as sns
import matplotlib
matplotlib.use("Qt5Agg")


# CONTROLLERS 

from controllers.graphController import setup_graphs
from controllers.cloudController import setup_cloud
from controllers.cityController import setup_cities
from controllers.navigationController import setup_navigation


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


class AppDemo(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi('front/src/dashboard.ui', self)

        sns.set_style("dark")


        setup_cloud(self)

        setup_graphs(self)

        setup_cities(self)

        setup_navigation(self)


        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self.scrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    font = QFont("Roboto", 10)

    app.setFont(font)

    app.setStyle("Fusion")

    demo = AppDemo()

    demo.show()

    try:
        sys.exit(app.exec())

    except SystemExit:
        print("Fechando App...")