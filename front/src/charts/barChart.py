import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_bar_chart(layout, dados, cores, labels):
        
        fig, ax = plt.subplots(figsize=(5,4), dpi=100)

        ax.clear()
        x = range(len(dados))

        ax.bar(
            x,
            height=dados,
            color=cores,
            tick_label=labels,
            width=0.4
        )

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

     
        ax.tick_params(axis='y', labelsize=6, colors='#666666')
        ax.tick_params(axis='x', labelsize=5, colors='#666666')

        ax.set_axisbelow(True) 
        ax.grid(axis='y', color='gray', linestyle='--', alpha=0.3)
    
        fig.subplots_adjust(left=0.2, bottom=0.2, top=0.9, right=0.95)

        canvas.draw()

        return fig, ax, canvas
