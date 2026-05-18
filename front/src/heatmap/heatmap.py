import os
import requests
import folium
import random

import geopandas as gpd
from shapely.geometry import Point

from folium.plugins import HeatMap

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def createHeatMap(layout, data):

    navegador = QWebEngineView()

    layout.addWidget(navegador)

    mapa_sp = folium.Map(
        location=[-22.39071, -47.02148],
        zoom_start=6,
        tiles="CartoDB positron",
        zoom_control=False,
        scrollWheelZoom=True,
        max_zoom=8,
        min_zoom=2,
        dragging=True,
        prefer_canvas=True,
        attribution_control=False
    )

    url = (
        "https://raw.githubusercontent.com/"
        "codeforamerica/click_that_hood/master/"
        "public/data/brazil-states.geojson"
    )
    gdf = gpd.read_file(url)
    sp = gdf[gdf["name"] == "São Paulo"].geometry.values[0]

    def gerar_ponto_em_sp(poligono):
    
        minx, miny, maxx, maxy = poligono.bounds
        while True:
        
            ponto = Point(
                random.uniform(minx, maxx),
                random.uniform(miny, maxy)
            )
            if poligono.contains(ponto):
                return ponto.y, ponto.x
    resposta = requests.get(url)

    brasil_geojson = resposta.json()

    sp_feature = None
    for feature in brasil_geojson["features"]:
        nome = feature["properties"]["name"]
        if nome.lower() == "são paulo":
            sp_feature = feature
            break

    geojson_sp = {
        "type": "FeatureCollection",
        "features": [sp_feature]
    }
    
    coordenadas_teste = []
    for _ in range(200):
    
        lat, lon = gerar_ponto_em_sp(sp)
        intensidade = random.uniform(0.3, 1.0)
        coordenadas_teste.append([lat, lon, intensidade])
    HeatMap(coordenadas_teste,
            radius=18,
            blur=25,
            min_opacity=0.2
            ).add_to(mapa_sp)
    
    folium.GeoJson(
        geojson_sp,
        style_function=lambda feature: {
            "fillColor": "transparent",
            "color": "#838383",
            "weight": 2,
            "fillOpacity": 0,
        }
    ).add_to(mapa_sp)

    arquivo_html = "mapa.html"
    mapa_sp.save(arquivo_html)

    caminho = os.path.abspath(arquivo_html)
    navegador.load(
        QUrl.fromLocalFile(caminho)
    )

    return navegador