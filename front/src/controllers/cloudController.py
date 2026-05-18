from charts.cloudChart import changeCloudByDB

from data.data import (
    dados_diagfreq
)

def setup_cloud(window):
    window.cloud_labels = [
        window.label1stSqr,
        window.label2ndSqr,
        window.label3rdSqr,
        window.label4thSqr,
        window.label5thSqr,
        window.label6thSqr
    ]
    window.cloud_values = [
        window.value1stSqr,
        window.value2ndSqr,
        window.value3rdSqr,
        window.value4thSqr,
        window.value5thSqr,
        window.value6thSqr
    ]

    changeCloudByDB(
            window.cloud_labels,
            window.cloud_values,
            dados_diagfreq
        )