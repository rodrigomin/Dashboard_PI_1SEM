import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class HeatmapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mapa de Calor - Matplotlib + PyQt5")
        self.setGeometry(100, 100, 700, 500)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Figura do matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)

        # Cria o heatmap
        self.plot_heatmap()

    def plot_heatmap(self):
        # Dados aleatórios 10x10
        data = np.random.rand(100, 100)

        ax = self.figure.add_subplot(111)

        # Heatmap
        heatmap = ax.imshow(data, cmap="hot", interpolation="nearest")

        # Barra lateral de cores
        self.figure.colorbar(heatmap)

        ax.set_title("Exemplo de Heatmap")
        ax.set_xlabel("Colunas")
        ax.set_ylabel("Linhas")

        # Atualiza canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = HeatmapWindow()
    window.show()

    sys.exit(app.exec_())