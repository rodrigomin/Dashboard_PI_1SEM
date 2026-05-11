import sys
from PyQt5.QtGui import QColor, QTransform, QPixmap, QFont, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizePolicy, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt, QMargins
from PyQt5 import uic
from itertools import cycle


import matplotlib
matplotlib.use('Qt5Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random

# from widgets.glass_cards import GlassCard

from charts.lineChart  import create_line_chart
from charts.pieChart import create_pie_chart
from charts.barChart import create_bar_chart
from charts.cloudChart import changeCloudByDB

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('front/src/dashboard.ui', self)
        
        balls = cycle([self.ball1, self.ball2, self.ball3])
        it = iter(balls)

        # graphs

        sns.set_style("dark") 

        self.dados_mensal = {
            'x': ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
            'y': [1000, 2000, 3000, 1000, 1500, 2400, 5000, 2300, 3000, 3500, 2500, 8000]
        }
        self.dados_anual = {
            "x": ['2019', '2020', '2021', '2022', '2023', '2024'],
            "y": [random.randint(3000, 8000) for _ in range(6)]
        }

        self.dados_donut = {
            "data": [12, 43, 30, 90],
            "cores": ['#143982', '#1B61DB', '#79CDFC', '#87BAD3'],
            "labels": [self.prontoSocorro, self.Internacao, self.exames, self.outro]
            }
        
        self.dados_bar = {
            "data": [20, 30, 40, 15],
            "cores": ['#1B61DB', '#79CDFC', '#143982', '#87BAD3'],
            "labels": ['Triagem', 'Consulta', 'Exames', 'Cirurgias'],
        }

        dados_diagfreq = {
            'HIV': 40,
            'Hemorróida': 20,
            'Gripe': 349,
            'Dor no corpo': 120,
            'Tosse': 200,
            'Diarréia': 50,
            'HPV': 34
        }
        
        labels_cloud = {
            'labels': [self.label1stSqr, self.label2ndSqr, self.label3rdSqr, self.label4thSqr, self.label5thSqr, self.label6thSqr],
            'value': [self.value1stSqr, self.value2ndSqr, self.value3rdSqr, self.value4thSqr, self.value5thSqr, self.value6thSqr]
        }
        
        changeCloudByDB(labels_cloud['labels'], labels_cloud['value'], dados_diagfreq)
        
        self.setup_graphs()
        
        # button functions

        self.goLeft.clicked.connect(lambda: self.teste('left'))
        self.goRight.clicked.connect(lambda: self.teste('right'))
        self.goLeft_2.clicked.connect(lambda: self.teste('left'))
        self.goRight_2.clicked.connect(lambda: self.teste('right'))

        self.fechar.clicked.connect(lambda: sys.exit())
        self.fechar_2.clicked.connect(lambda: sys.exit())
    
        self.VolAtdComboBox.currentIndexChanged.connect(self.graphsAtd)
        self.DistAtdComboBox.currentIndexChanged.connect(self.graphsDistAtd)

    
    def setup_graphs(self):
        create_line_chart(
            layout=self.horizontalLayout_6,
            dados=self.dados_anual,
            max_val=8000
        )
        create_line_chart(
            layout=self.graphicsVol_2,
            dados=self.dados_mensal,
            max_val=8000
        )
        create_bar_chart(
            layout=self.TIP_ATNDMNT_GRAPH,
            dados=self.dados_bar['data'],
            cores=self.dados_bar['cores'],
            labels=self.dados_bar['labels']
        )
        create_pie_chart(
            layout=self.Atd_tipServico_graph,
            dados=self.dados_donut['data'],
            cores=self.dados_donut['cores'],
            donut=True
        )
        create_pie_chart(
            layout=self.graph_2,
            dados=[180, 80],
            cores=['#0066FF', '#FF00EE'],
            donut=False,
            labels=[self.homens_val, self.mulheres_val]
        )



    def teste(self, dir):
        if (dir == 'left'):
            print('clicou esquerda')
            self.stackedWidget.setCurrentWidget(self.page)
        else:
            print('clicou direita')
            self.stackedWidget.setCurrentWidget(self.page_2)

    def graphsAtd(self, value):
        print('cu')
        value = self.VolAtdComboBox.currentText()

        if (value == 'Mensal'):
            self.GraphicsVOLATD.setCurrentWidget(self.GraphicsMensal)
        else:
            self.GraphicsVOLATD.setCurrentWidget(self.GraphicsAnual)

    def graphsDistAtd(self, value):
        print('cu')
        value = self.DistAtdComboBox.currentText()

        match (value):
            case ('Exames'):
                self.DistGraphs.setCurrentWidget(self.ExamesPg)
                print('Exames')
            case ('Triagem'):
                self.DistGraphs.setCurrentWidget(self.TriagemPage)
                print('Triagem')
            case ('Consulta'):
                self.DistGraphs.setCurrentWidget(self.ConsultaPage)
                print('Consulta')
            case ('Cirurgias'):
                self.DistGraphs.setCurrentWidget(self.CirurgiaPage)
                print('Cirurgias')

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Roboto", 10)  # ou Arial, Roboto

    app.setFont(font)
    app.setStyle("Fusion")

    demo = AppDemo()
    demo.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Fechando App...")