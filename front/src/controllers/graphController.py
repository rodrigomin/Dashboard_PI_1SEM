# CHARTS
from charts.lineChart import create_line_chart
from charts.pieChart import create_pie_chart
from charts.barChart import create_bar_chart
from heatmap.heatmap import createHeatMap


from data.data import (
    dados_mensal,
    dados_anual,
    dados_bar,
    dados_faixa,
    dados_donut,
    dados_sex
)

def setup_graphs(window):

    window.balls = [
        window.ball0,
        window.ball1,
        window.ball2
    ]
    
    window.sex_widgets = {
        0: {
            "layout": window.graph_6,
            "labels": [
                window.homens_val_5,
                window.mulheres_val_5
            ]
        },
        1: {
            "layout": window.graph_2,
            "labels": [
                window.homens_val,
                window.mulheres_val
            ]
        },
        2: {
            "layout": window.graph_3,
            "labels": [
                window.homens_val_2,
                window.mulheres_val_2
            ]
        },
        3: {
            "layout": window.graph_5,
            "labels": [
                window.homens_val_4,
                window.mulheres_val_4
            ]
        }
    }
    
    window.faixa_layouts = {
        0: window.faixaGRAPHExames_5,
        1: window.faixaGRAPHExames,
        2: window.faixaGRAPHExames_2,
        3: window.faixaGRAPHExames_4
    }

    createHeatMap(
        window.CMap_Layout,
        None
    )

    create_line_chart(
        layout=window.horizontalLayout_6,
        dados=dados_anual,
        max_val=8000
    )

    create_line_chart(
        layout=window.graphicsVol_2,
        dados=dados_mensal,
        max_val=8000
    )

    create_bar_chart(
        layout=window.TIP_ATNDMNT_GRAPH,
        dados=dados_bar['data'],
        cores=dados_bar['cores'],
        labels=dados_bar['labels']
    )

    create_pie_chart(
        layout=window.Atd_tipServico_graph,
        dados=dados_donut['data'],
        cores=dados_donut['cores'],
        donut=True
    )

    for index, graph in dados_sex.items():
        create_pie_chart(
            layout=window.sex_widgets[index]['layout'],
            dados=graph['data'],
            cores=graph['cores'],
            donut=False,
            labels=window.sex_widgets[index]['labels']
        )

    for index, graph in dados_faixa.items():
        create_bar_chart(
            layout=window.faixa_layouts[index],
            dados=graph['data'],
            cores=graph['cores'],
            labels=graph['labels']
        )