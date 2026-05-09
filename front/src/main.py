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


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

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

    def enterEvent(event):
        widget._anim.stop()
        start = widget.pos()
        end = start - QPoint(0, offset)
        widget._anim.setStartValue(start)
        widget._anim.setEndValue(end)
        widget._anim.start()

    def leaveEvent(event):
        widget._anim.stop()
        start = widget.pos()
        end = start + QPoint(0, offset)
        widget._anim.setStartValue(start)
        widget._anim.setEndValue(end)
        widget._anim.start()

    widget.enterEvent = enterEvent
    widget.leaveEvent = leaveEvent


def aplicar_sombra_animada(widget):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setYOffset(4)
    shadow.setColor(QColor(0, 0, 0, 40))
    widget.setGraphicsEffect(shadow)

    widget._shadow = shadow

    widget.shadow_anim = QPropertyAnimation(shadow, b"blurRadius")
    widget.shadow_anim.setDuration(150)
    widget.shadow_anim.setEasingCurve(QEasingCurve.OutCubic)

    def enterEvent(event):
        widget.shadow_anim.stop()
        widget.shadow_anim.setStartValue(15)
        widget.shadow_anim.setEndValue(30)
        widget.shadow_anim.start()

    def leaveEvent(event):
        widget.shadow_anim.stop()
        widget.shadow_anim.setStartValue(30)
        widget.shadow_anim.setEndValue(15)
        widget.shadow_anim.start()

    widget.enterEvent = enterEvent
    widget.leaveEvent = leaveEvent

def hover_glass(widget):
    # posição
    widget._anim = QPropertyAnimation(widget, b"pos")
    widget._anim.setDuration(150)
    widget._anim.setEasingCurve(QEasingCurve.OutCubic)

    start = widget.pos()

    # sombra
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setYOffset(4)
    shadow.setColor(QColor(0, 0, 0, 40))
    widget.setGraphicsEffect(shadow)

    widget._shadow = shadow
    widget.shadow_anim = QPropertyAnimation(shadow, b"blurRadius")
    widget.shadow_anim.setDuration(150)

    def enterEvent(event):
        # sobe
        widget._anim.stop()
        widget._anim.setStartValue(widget.pos())
        widget._anim.setEndValue(widget.pos() - QPoint(0, 4))
        widget._anim.start()

        # sombra cresce
        widget.shadow_anim.stop()
        widget.shadow_anim.setStartValue(15)
        widget.shadow_anim.setEndValue(30)
        widget.shadow_anim.start()

    def leaveEvent(event):
        # desce
        widget._anim.stop()
        widget._anim.setStartValue(widget.pos())
        widget._anim.setEndValue(widget.pos() + QPoint(0,4))
        widget._anim.start()

        widget.shadow_anim.stop()
        widget.shadow_anim.setStartValue(30)
        widget.shadow_anim.setEndValue(15)
        widget.shadow_anim.start()

    widget.enterEvent = enterEvent
    widget.leaveEvent = leaveEvent

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('front/src/dashboard.ui', self)
        
        balls = cycle([self.ball1, self.ball2, self.ball3])
        it = iter(balls)

        # graphs

        sns.set_style("dark") 

        self.fig_anual, self.ax_anual = plt.subplots(figsize=(5,4), dpi=100)
        self.fig_mensal, self.ax_mensal = plt.subplots(figsize=(5,4), dpi=100)

        # Pie
        self.fig_pie, self.ax_pie = plt.subplots(figsize=(5,4), dpi=100)

        self.fig_donut, self.ax_donut = plt.subplots(figsize=(5,4), dpi=100)

        # Bar
        self.fig_bar, self.ax_bar = plt.subplots(figsize=(5,4), dpi=100)

        self.canvas_bar = FigureCanvas(self.fig_bar)
        self.TIP_ATNDMNT_GRAPH.addWidget(self.canvas_bar)

        self.canvas_donut = FigureCanvas(self.fig_donut)
        self.Atd_tipServico_graph.addWidget(self.canvas_donut)

        self.canvas_pie = FigureCanvas(self.fig_pie)
        self.graph_2.addWidget(self.canvas_pie)


        self.canvas_anual = FigureCanvas(self.fig_anual)
        self.horizontalLayout_6.addWidget(self.canvas_anual)

        self.canvas_mensal = FigureCanvas(self.fig_mensal)
        self.graphicsVol_2.addWidget(self.canvas_mensal)

        dados_mensal = {
            'x': ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
            'y': [1000, 2000, 3000, 1000, 1500, 2400, 5000, 2300, 3000, 3500, 2500, 8000]
        }
        dados_anual = {
            "x": ['2019', '2020', '2021', '2022', '2023', '2024'],
            "y": [random.randint(3000, 8000) for _ in range(6)]
        }

        dados_donut = {
            "data": [12, 43, 30, 90],
            "cores": ['#143982', '#1B61DB', '#79CDFC', '#87BAD3'],
            "labels": [self.prontoSocorro, self.Internacao, self.exames, self.outro]
            }
        
        dados_bar = {
            "data": [20, 30, 40, 15],
            "cores": ['#1B61DB', '#79CDFC', '#143982', '#87BAD3'],
            "labels": ['Triagem', 'Consulta', 'Exames', 'Cirurgias'],
        }

        
        self.gerarGraficoLine(self.fig_anual, self.ax_anual, self.canvas_anual, dados_anual, 8500)
        self.gerarGraficoLine(self.fig_mensal, self.ax_mensal, self.canvas_mensal, dados_mensal, 8500)

        self.gerarPizza(self.ax_pie, self.fig_pie, self.canvas_pie, [180, 80], ['#0066FF', '#FF00EE'], [self.homens_val, self.mulheres_val], False)
        self.gerarPizza(self.ax_donut, self.fig_donut, self.canvas_donut, dados_donut['data'], dados_donut['cores'], dados_donut['labels'], True)

        self.gerarBarGraph(self.ax_bar, self.fig_bar, self.canvas_bar, dados_bar['data'], dados_bar['cores'], dados_bar['labels'])
        # button functions

        self.goLeft.clicked.connect(lambda: self.teste('left'))
        self.goRight.clicked.connect(lambda: self.teste('right'))
        self.goLeft_2.clicked.connect(lambda: self.teste('left'))
        self.goRight_2.clicked.connect(lambda: self.teste('right'))

        self.fechar.clicked.connect(lambda: sys.exit())
        self.fechar_2.clicked.connect(lambda: sys.exit())
    
        self.VolAtdComboBox.currentIndexChanged.connect(self.graphsAtd)
        self.DistAtdComboBox.currentIndexChanged.connect(self.graphsDistAtd)

    def gerarBarGraph(self, ax, fig, canvas, dados, cores, labels):
        ax.clear()
        x = range(len(dados))

        # 1. Desenha as barras
        ax.bar(
            x,
            height=dados,
            color=cores,
            tick_label=labels,
            width=0.4 # Aumentei um pouco, 0.25 fica muito fininha
        )

        # 2. Define explicitamente o que deve aparecer no Y
     
        # 3. Configura os ticks (números)
        ax.tick_params(axis='y', labelsize=8, colors='#666666')
        ax.tick_params(axis='x', labelsize=6, colors='#666666')

        ax.set_axisbelow(True) 
        ax.grid(axis='y', color='gray', linestyle='--', alpha=0.3)
    
        fig.subplots_adjust(left=0.2, bottom=0.2, top=0.9, right=0.95)

        canvas.draw()




    def gerarPizza(self, ax, fig, canvas, dados, cores, labels, rosca):


        ax.clear()

        ax.pie(
            dados,
            startangle=20,
            colors=cores,
            textprops={'fontsize': 9, 'color': '#444444'},
            wedgeprops={'edgecolor': 'white', 'linewidth': 2}
        )

        # definindo valor de homens e mulheres

        for index, valor in enumerate(dados):
            labels[index].setText(f"{(valor / sum(dados)) * 100:.0f}%")
        
        if (rosca == True):
            circulo = plt.Circle((0,0), 0.70, fc='white')
            ax.add_artist(circulo)

        ax.axis('equal')

        fig.tight_layout()

        canvas.draw()


    def gerarGraficoLine(self, fig, ax, canvas,dados, max_val):

        ax.clear()

        
        sns.lineplot(
            data=dados,
            x='x', 
            y='y', 
            ax=ax, 
            marker='o', 
            color='#ff7f0e', 
            linewidth=1
        )

        # Define o tamanho base para todos os textos do gráfico
        ax.tick_params(axis='both', labelsize=8) 

        ax.set_ylim(0, max_val) 

        ax.set_ylabel("") # Remove o texto "Volume" (ou qualquer outro) do eixo Y
        
        ax.set_xticklabels(dados['x'])

        ax.grid()
        fig.tight_layout()
        canvas.draw()


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