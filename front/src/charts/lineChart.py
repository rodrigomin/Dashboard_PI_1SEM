import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_line_chart(layout, dados, max_val=1000):

    fig, ax = plt.subplots(figsize=(5,4), dpi=100)

    sns.lineplot(
        data=dados,
        x='x',
        y='y',
        ax=ax,
        marker='o'
    )

    ax.set_ylim(0, max_val)

    ax.tick_params('both', labelsize=6)
    ax.set_ylabel("")
    canvas = FigureCanvas(fig)
    fig.tight_layout()

    layout.addWidget(canvas)

    ax.grid()
    canvas.draw()

    return fig, ax, canvas