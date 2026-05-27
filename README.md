# **Dashboard do Projeto Integrador do 1° SEM.**<br/>
*&nbsp;&nbsp;&nbsp;&nbsp;Grupo: João Victor Fernandes, Flávio Ricardo Santos e Eduardo Furlanetto Nagashima.*

<p align="center">
  <br/>
  <br/>
  <img width="728" height="525" alt="image" src="https://github.com/user-attachments/assets/84fc7ca3-fb55-4557-9f4f-8d0820444804" />
</p>

---

# Sumário

- [Objetivo do Sistema](#objetivo-do-sistema)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Instruções Básicas de Instalação](#instalação-de-dependências)

---

# Objetivo do Sistema

Este dashboard foi desenvolvido para análise dos dados oferecidos pelo banco de dados do Projeto Integrador do primeiro semestre, gerando gráficos, nuvem de palavras e mapa de calor.

---

# Tecnologias Utilizadas

| Dependência | Função no Projeto |
|---|---|
| `PyQt5` | Biblioteca utilizada para criar a interface gráfica da aplicação. Também foi utilizada em conjunto com o Qt Designer para construção de elementos visuais mais simples (arquivo `dashboard.ui`), enquanto funcionalidades mais complexas foram implementadas diretamente no código. |
| `matplotlib` | Biblioteca responsável pela criação dos gráficos utilizados no dashboard, incluindo gráficos de colunas, barras, linhas e setores. |
| `seaborn` | Biblioteca utilizada para estilização e melhoria visual dos gráficos gerados com `matplotlib`. |
| `folium` | Biblioteca utilizada para criação do mapa de calor, em conjunto com um arquivo GeoJSON do estado de São Paulo para desenhar os contornos geográficos. |
| `Figma` | Utilizado para prototipagem e estilização do visual do aplicativo. |

---

# Funcionalidades Principais

- Geração de gráficos estatísticos
- Visualização geográfica com mapa de calor
- Interface gráfica interativa
- Análise visual de dados

---

# Figma

> Segue o anexo de uma imagem do protótipo criado no Figma

<br/>
<img width="775" height="245" alt="image" src="https://github.com/user-attachments/assets/b07d0dd6-1388-4a5a-8ffb-b78dc83554ff" />

<br/>

# Arquitetura do Sistema

> O sistema foi organizado de forma modular para separar interface gráfica, processamento de dados, geração de gráficos e recursos auxiliares.

| Diretório / Arquivo | Responsabilidade |
|---|---|
| `main.py` | Arquivo principal responsável por iniciar a aplicação. |
| `dashboard.ui` | Interface gráfica desenvolvida no Qt Designer. |
| `data/` | Armazena bases de dados experimentais utilizadas pelo dashboard. |
| `widgets/` | Componentes visuais e widgets personalizados da interface. |
| `assets/` | Recursos estáticos como imagens, ícones e estilos. |
| `charts/` | Responsável pela geração e configuração dos gráficos. |
| `controllers\` | Funções como implementação de gráficos e funcionalidade do Nav no UI. |
| `heatmap/` | Geração do mapa de calor com Folium. |

---

# Endpoints

> Ainda em desenvolvimento, será feito pelo João Victor.
---

# Instalação de Dependências

### Windows:

```bash
pip install pyqtwebengine folium seaborn
```

### Linux:

```bash
sudo apt update

sudo apt install -y \
    python3-pip \
    python3-pyqt5 \
    python3-pyqt5.qtwebengine

pip install folium seaborn
```

Instalação alternativa via pip:

```bash
pip install pyqtwebengine folium seaborn
```
