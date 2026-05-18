import sys


#def teste(window, direction):
#
#    index = window.stackedWidget.currentIndex()
#
#    # =========================
#    # MOVE STACK
#    # =========================
#
#    if direction == 'left' and index > 0:
#        index -= 1
#        window.stackedWidget.setCurrentIndex(index)
#
#    elif direction == 'right' and index < window.stackedWidget.count() - 1:
#        index += 1
#        window.stackedWidget.setCurrentIndex(index)
#
#    # =========================
#    # STYLE BALLS
#    # =========================
#
#    style_default = """
#    background-color: rgba(255, 255, 255, 0.25);
#    border-radius: 20;
#    border: 1px solid rgba(255, 255, 255, 0.35);
#    """
#
#    style_active = """
#    background-color: rgba(255, 255, 255, 0.8);
#    border-radius: 20px;
#    """
#
#    for i, bola in enumerate(window.balls):
#
#        if i == index:
#            bola.setStyleSheet(style_active)
#        else:
#            bola.setStyleSheet(style_default)
#

def teste(window, dir=None): 
    index = window.stackedWidget.currentIndex() 
    balls = [window.ball0, window.ball1, window.ball2]
    style_default = 'QPushButton.bubble {\n background-color: rgba(255, 255, 255, 0.25);\n border-radius: 20px; /* metade do tamanho */\n\n border: 1px solid rgba(255, 255, 255, 0.35);\n\n /* brilho tipo vidro */\n background-image: linear-gradient(\n to bottom,\n rgba(255, 255, 255, 0.5),\n rgba(255, 255, 255, 0.1)\n );\n} ' 
    style_active = 'background-color: rgba(255, 255, 255, 0.25);'


    if dir == 'left' and index > 0:
        index -= 1
        window.stackedWidget.setCurrentIndex(index)

    elif dir == 'right' and index < window.stackedWidget.count() - 1:
        
        index += 1
        window.stackedWidget.setCurrentIndex(index)
    else:
        if (index > 0 and index < window.stackedWidget.count() - 1):
            window.stackedWidget.setCurrentWidget(dir)
            index = window.stackedWidget.currentIndex()


    for i, bola in enumerate(balls):
        if i == index:
            bola.setStyleSheet(style_active)
        else:
            bola.setStyleSheet(style_default)


def graphsAtd(window, value):

    if value == 'Mensal':

        window.GraphicsVOLATD.setCurrentWidget(
            window.GraphicsMensal
        )

    else:

        window.GraphicsVOLATD.setCurrentWidget(
            window.GraphicsAnual
        )


def graphsDistAtd(window, value):

    match value:

        case 'Exames':

            window.DistGraphs.setCurrentWidget(
                window.ExamesPg
            )

        case 'Triagem':

            window.DistGraphs.setCurrentWidget(
                window.TriagemPage
            )

        case 'Consulta':

            window.DistGraphs.setCurrentWidget(
                window.ConsultaPage
            )

        case 'Cirurgias':

            window.DistGraphs.setCurrentWidget(
                window.CirurgiaPage
            )


def setup_navigation(window):


    window.goLeft.clicked.connect(
        lambda: teste(window, 'left')
    )

    window.goRight.clicked.connect(
        lambda: teste(window, 'right')
    )

    window.fechar.clicked.connect(
        lambda: sys.exit()
    )

    window.map.clicked.connect(
        lambda: teste(window, window.page_3)
    )
    window.home.clicked.connect(
        lambda: teste(window, window.page)
    )


    window.VolAtdComboBox.currentTextChanged.connect(
        lambda value: graphsAtd(window, value)
    )

    window.DistAtdComboBox.currentTextChanged.connect(
        lambda value: graphsDistAtd(window, value)
    )