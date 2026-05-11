import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_pie_chart(layout, dados, cores: list, donut: bool, labels=None):

    
    fig, ax = plt.subplots(figsize=(5,4), dpi=100)

    ax.pie(
        dados,
        colors=cores
    )

    if (donut == True):
        circulo = plt.Circle((0,0), 0.70, fc='white') 
        ax.add_artist(circulo) 

    if labels:
        for index, label in enumerate(labels):

            porcentagem = (dados[index] / sum(dados)) * 100
        
            label.setText(f"{porcentagem:.0f}%")
    
    ax.axis('equal')

    canvas = FigureCanvas(fig)
    fig.tight_layout()

    layout.addWidget(canvas)

    canvas.draw()

    return fig, ax, canvas