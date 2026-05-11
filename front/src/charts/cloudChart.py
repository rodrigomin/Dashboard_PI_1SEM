
def changeCloudByDB(labels: list, valuesLabels: list, data: dict):

    itens_ordenados = sorted(data.items(), key=lambda item: item[1], reverse=True)

    for i,(chave, valor) in enumerate(itens_ordenados):

        if i >= len(labels):
            break

        labels[i].setText(str(chave))
        valuesLabels[i].setText(str(valor))

