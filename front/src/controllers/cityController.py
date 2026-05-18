from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from data.data import dados_bairroCidade


def atualizarBairros(window):

    cidadeIndex = window.comboCidade.currentIndex()

    window.comboBairro.clear()

    for bairro in dados_bairroCidade[cidadeIndex]['bairros']:
        window.comboBairro.addItem(bairro)



def atualizarRuas(window):

    cidadeIndex = window.comboCidade.currentIndex()

    bairroIndex = window.comboBairro.currentText()

    layout = window.scrollAreaWidgetContents

    layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    if layout is not None:

        while layout.count():

            item = layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    for sitio in dados_bairroCidade[cidadeIndex]['bairros'][bairroIndex]:

        font = QFont('Roboto', 6)

        newLabel = QLabel(sitio)

        newLabel.setFont(font)

        window.scrollAreaWidgetContents.addWidget(newLabel)



def setup_cities(window):

    for cidade in dados_bairroCidade:

        window.comboCidade.addItem(
            cidade['cidade']
        )

    window.comboCidade.currentTextChanged.connect(
        lambda: atualizarBairros(window)
    )

    window.comboCidade.currentTextChanged.connect(
        lambda: atualizarRuas(window)
    )

    window.comboBairro.currentTextChanged.connect(
        lambda: atualizarRuas(window)
    )

    atualizarBairros(window)

    atualizarRuas(window)