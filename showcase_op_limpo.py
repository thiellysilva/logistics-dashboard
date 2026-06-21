"""
SHOWCASE — Operacional (Light Theme)
Receita Individual + Combustível
Rodar: python showcase_op_limpo.py
Abrir: http://127.0.0.1:8061
"""

import dash
from dash import html, dcc, dash_table, callback, Input, Output
import plotly.graph_objects as go
import pandas as pd

# Cores
WHITE = "#FFFFFF"
BG_GRAY = "#F5F6FA"
TEXT = "#1A1A2E"
SEC = "#6B7280"
GREEN = "#149157"
GREEN_DARK = "#0B5C36"
ORANGE = "#E87722"
RED = "#DC2626"
BLUE = "#2563EB"
PURPLE = "#7C3AED"
BORDER = "#E5E7EB"


def kpi_card(icon, value, label, sub=None, sub_color=None):
    children = [
        html.Div(icon, style={"fontSize": "26px", "marginBottom": "6px"}),
        html.Div(value, style={"fontSize": "26px", "fontWeight": "700", "color": TEXT}),
        html.Div(label, style={"fontSize": "12px", "color": SEC, "marginTop": "4px"}),
    ]
    if sub:
        children.append(html.Div(sub, style={
            "fontSize": "12px",
            "color": sub_color if sub_color else GREEN,
            "fontWeight": "600",
            "marginTop": "4px",
        }))
    return html.Div(style={
        "backgroundColor": WHITE,
        "border": "1px solid " + BORDER,
        "borderRadius": "8px",
        "padding": "18px",
        "textAlign": "center",
        "flex": "1",
        "minWidth": "155px",
    }, children=children)


def chart_card(title, fig, min_width="400px"):
    return html.Div(style={
        "backgroundColor": WHITE,
        "border": "1px solid " + BORDER,
        "borderRadius": "8px",
        "padding": "20px",
        "flex": "1",
        "minWidth": min_width,
    }, children=[
        html.P(title, style={
            "fontSize": "14px",
            "fontWeight": "600",
            "color": TEXT,
            "margin": "0 0 12px 0",
        }),
        dcc.Graph(figure=fig, config={"displayModeBar": False}),
    ])


def row(children, mb="16px"):
    return html.Div(style={
        "display": "flex",
        "gap": "16px",
        "marginBottom": mb,
        "flexWrap": "wrap",
    }, children=children)


# =============================================================
# ABA RECEITA INDIVIDUAL
# =============================================================

def tab_receita():
    # Top 7 cavalos
    cavalos_placas = ["508", "471", "523", "496", "462", "531", "484"]
    cavalos_receita = [241000, 237000, 228000, 225000, 218000, 204000, 198000]
    cavalos_pct = ["114%", "112%", "108%", "107%", "103%", "97%", "94%"]

    fig_cavalos = go.Figure()
    fig_cavalos.add_trace(go.Bar(
        y=cavalos_placas[::-1],
        x=cavalos_receita[::-1],
        orientation="h",
        marker_color=GREEN,
        text=["R$ " + str(v // 1000) + "k  " + p for v, p in zip(cavalos_receita[::-1], cavalos_pct[::-1])],
        textposition="outside",
        textfont=dict(color=TEXT, size=10),
    ))
    fig_cavalos.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=SEC,
        height=200,
        margin=dict(l=70, r=100, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False),
        showlegend=False,
    )

    # Top 8 motoristas
    mot_nomes = ["Ricardo Alves", "Fernando Braga", "Gustavo Pires", "Leandro Nunes",
                 "Diego Mendonca", "Paulo Ribeiro", "Sergio Campos", "Henrique Duarte"]
    mot_receita = [128000, 124000, 121000, 117000, 112000, 108000, 103000, 98000]
    mot_pct = ["61%", "59%", "57%", "55%", "53%", "51%", "49%", "46%"]

    fig_mot = go.Figure()
    fig_mot.add_trace(go.Bar(
        y=mot_nomes[::-1],
        x=mot_receita[::-1],
        orientation="h",
        marker_color=BLUE,
        text=["R$ " + str(v // 1000) + "k  " + p for v, p in zip(mot_receita[::-1], mot_pct[::-1])],
        textposition="outside",
        textfont=dict(color=TEXT, size=10),
    ))
    fig_mot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=SEC,
        height=230,
        margin=dict(l=120, r=100, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False),
        showlegend=False,
    )

    # Distribuicao por faixa
    fig_dist = go.Figure()
    fig_dist.add_trace(go.Bar(
        x=["<R$100k", "R$100-200k", "R$200-250k", ">R$250k"],
        y=[3, 8, 12, 4],
        marker_color=[RED, ORANGE, GREEN, GREEN],
        text=[3, 8, 12, 4],
        textposition="outside",
        textfont=dict(size=12),
    ))
    fig_dist.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=SEC,
        height=180,
        margin=dict(l=20, r=20, t=10, b=50),
        yaxis=dict(showgrid=False, showticklabels=False),
        showlegend=False,
    )
    fig_dist.add_annotation(
        text="3 cavalos abaixo de R$100k - investigar ociosidade",
        x=0.5, y=-0.4, xref="paper", yref="paper",
        font=dict(size=11, color=RED), showarrow=False,
    )

    # Bottom 5 tabela
    bottom = pd.DataFrame({
        "PLACA": ["527", "414", "469", "502", "438"],
        "RECEITA": ["R$ 18k", "R$ 67k", "R$ 82k", "R$ 91k", "R$ 114k"],
        "% META": ["8,5%", "31,8%", "38,9%", "43,1%", "54,0%"],
        "STATUS": ["Critico", "Critico", "Atencao", "Atencao", "Atencao"],
    })

    return html.Div([
        row([
            kpi_card("🚛", "R$ 39k", "Receita Media / Cavalo"),
            kpi_card("📦", "R$ 33k", "Receita Media / Carreta"),
            kpi_card("👤", "R$ 36k", "Receita Media / Motorista"),
            kpi_card("⬆", "R$ 241k", "Melhor Cavalo (508)", "114,2%", GREEN),
            kpi_card("⬇", "R$ 18k", "Pior Cavalo (527)", "8,5%", RED),
        ]),
        row([
            chart_card("🚛 Receita por Cavalo (Placa) - Top 7", fig_cavalos),
            chart_card("👤 Receita por Motorista - Top 8", fig_mot),
        ]),
        row([
            chart_card("📊 Distribuicao de Receita por Faixa (Cavalos)", fig_dist),
            html.Div(style={
                "backgroundColor": WHITE,
                "border": "1px solid " + BORDER,
                "borderRadius": "8px",
                "padding": "20px",
                "flex": "1",
                "minWidth": "400px",
            }, children=[
                html.P("📉 Bottom 5 - Cavalos com menor receita", style={
                    "fontSize": "14px", "fontWeight": "600", "color": TEXT, "margin": "0 0 12px 0",
                }),
                dash_table.DataTable(
                    data=bottom.to_dict("records"),
                    columns=[{"name": c, "id": c} for c in bottom.columns],
                    style_header={
                        "backgroundColor": BG_GRAY, "color": SEC, "fontWeight": "600",
                        "fontSize": "11px", "border": "none",
                        "borderBottom": "1px solid " + BORDER,
                        "textAlign": "left", "padding": "8px 12px",
                    },
                    style_cell={
                        "backgroundColor": WHITE, "color": TEXT, "fontSize": "12px",
                        "border": "none", "borderBottom": "1px solid " + BORDER,
                        "textAlign": "left", "padding": "10px 12px",
                    },
                    style_data_conditional=[
                        {"if": {"column_id": "STATUS", "filter_query": '{STATUS} = "Critico"'},
                         "color": RED, "fontWeight": "600"},
                        {"if": {"column_id": "STATUS", "filter_query": '{STATUS} = "Atencao"'},
                         "color": ORANGE, "fontWeight": "600"},
                    ],
                    style_as_list_view=True,
                ),
            ]),
        ]),
    ])


# =============================================================
# ABA COMBUSTIVEL
# =============================================================

def tab_combustivel():
    # Tendencias mensais (mini graficos de linha)
    meses = ["Jan", "Fev", "Mar"]

    def mini_line(y_vals, color, suffix=""):
        labels = [f"{v}{suffix}" for v in y_vals]
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=meses, y=y_vals,
            mode="lines+markers+text",
            text=labels,
            textposition="top center",
            textfont=dict(color=TEXT, size=10),
            line=dict(color=color, width=2),
            marker=dict(color=color, size=7),
            fill="tozeroy",
        ))
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color=SEC,
            height=120,
            margin=dict(l=10, r=10, t=25, b=25),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            showlegend=False,
        )
        return fig

    fig_litros = mini_line([28.4, 31.7, 36.2], BLUE, " Mil")
    fig_km = mini_line([82, 91, 108], GREEN, " Mil")
    fig_vlitro = mini_line([5.71, 5.84, 5.96], ORANGE)
    fig_vtotal = mini_line([162, 185, 215], PURPLE, "K")

    # Media km/l por veiculo
    veic_placas = ["47", "108", "115", "122", "418", "439", "441"]
    veic_kml = [22.4, 16.8, 14.3, 12.7, 10.1, 8.9, 4.2]
    veic_cores = [GREEN, GREEN, GREEN, GREEN, ORANGE, ORANGE, RED]

    fig_veic = go.Figure()
    fig_veic.add_trace(go.Bar(
        y=veic_placas[::-1],
        x=veic_kml[::-1],
        orientation="h",
        marker_color=veic_cores[::-1],
        text=[f"{v}" for v in veic_kml[::-1]],
        textposition="outside",
        textfont=dict(color=TEXT, size=11),
    ))
    fig_veic.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=SEC,
        height=220,
        margin=dict(l=60, r=60, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False),
        showlegend=False,
    )

    # Media km/l por motorista
    mot_nomes = ["Carlos Silveira", "Vinicius Aragao", "Bruno Tavares",
                 "Eduardo Lopes", "Jose Mendes", "Ronaldo Castro",
                 "Pedro Henrique", "Mario Pinto", "Felipe Rocha", "Joao Damiao"]
    mot_kml = [4.5, 4.1, 3.7, 3.4, 3.2, 3.0, 2.6, 2.4, 2.1, 1.6]
    mot_cores = [GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, ORANGE, ORANGE, ORANGE, RED]

    fig_mot = go.Figure()
    fig_mot.add_trace(go.Bar(
        y=mot_nomes[::-1],
        x=mot_kml[::-1],
        orientation="h",
        marker_color=mot_cores[::-1],
        text=[f"{v}" for v in mot_kml[::-1]],
        textposition="outside",
        textfont=dict(color=TEXT, size=11),
    ))
    fig_mot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color=SEC,
        height=280,
        margin=dict(l=130, r=60, t=10, b=10),
        xaxis=dict(showgrid=False, showticklabels=False),
        yaxis=dict(showgrid=False),
        showlegend=False,
    )

    return html.Div([
        # KPIs
        row([
            kpi_card("⛽", "2,38", "Media Geral km/l"),
            kpi_card("💲", "R$ 14,72", "Ticket Medio por KM"),
            kpi_card("📊", "R$ 215k", "Gasto Total (Mar)", "▲ +16% vs Fev", ORANGE),
            kpi_card("🏆", "4,5 km/l", "Melhor: Carlos Silveira"),
            kpi_card("⚠", "1,6 km/l", "Pior: Joao Damiao", "Critico", RED),
        ]),

        # Tendencias agregadas - titulo
        html.P("TENDENCIAS AGREGADAS", style={
            "color": ORANGE,
            "fontSize": "12px",
            "fontWeight": "700",
            "letterSpacing": "1px",
            "margin": "20px 0 12px 0",
        }),

        # Linha de mini graficos
        row([
            chart_card("⛽ Quant. Litros", fig_litros, "180px"),
            chart_card("🚛 KM Total", fig_km, "180px"),
            chart_card("💲 Valor do Litro", fig_vlitro, "180px"),
            chart_card("💰 Valor Total", fig_vtotal, "180px"),
        ]),

        # Rankings
        row([
            chart_card("🚛 Media km/l por Veiculo (Placa)", fig_veic),
            chart_card("👤 Media km/l por Motorista", fig_mot),
        ]),
    ])


# =============================================================
# APP
# =============================================================

app = dash.Dash(__name__)

tab_style = {
    "padding": "10px 20px",
    "fontSize": "13px",
    "fontWeight": "500",
    "color": SEC,
    "backgroundColor": "transparent",
    "border": "none",
    "borderBottom": "2px solid transparent",
}
tab_sel_style = {
    "padding": "10px 20px",
    "fontSize": "13px",
    "fontWeight": "600",
    "color": ORANGE,
    "backgroundColor": "transparent",
    "border": "none",
    "borderBottom": "2px solid " + ORANGE,
}

app.layout = html.Div(style={
    "backgroundColor": BG_GRAY,
    "minHeight": "100vh",
    "padding": "24px 32px",
    "fontFamily": "'Segoe UI', 'Inter', sans-serif",
}, children=[
    # Header
    html.P("SHOWCASE - OPERATIONAL SECTOR", style={
        "color": ORANGE, "fontSize": "11px", "fontWeight": "700",
        "letterSpacing": "1.5px", "margin": "0",
    }),
    html.H1("🚛 Operational - Management Dashboard", style={
        "color": TEXT, "fontSize": "22px", "fontWeight": "700", "margin": "4px 0",
    }),
    html.P("Monthly review - 9 consolidated tabs (from 13 original sources)", style={
        "color": SEC, "fontSize": "13px", "margin": "0 0 12px 0",
    }),

    # Green banner
    html.Div(style={
        "backgroundColor": GREEN_DARK,
        "borderRadius": "8px",
        "padding": "14px 24px",
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center",
        "margin": "0 0 16px 0",
    }, children=[
        html.Span("🚛 Operational Management", style={
            "color": "#FFF", "fontWeight": "700", "fontSize": "15px",
        }),
        html.Div(style={"display": "flex", "gap": "8px"}, children=[
            html.Span(t, style={
                "backgroundColor": "rgba(255,255,255,0.15)",
                "color": "#FFF",
                "padding": "6px 14px",
                "borderRadius": "6px",
                "fontSize": "12px",
            }) for t in ["📅 Year: 2026", "📅 Month: All", "🔄 Refresh", "← Back"]
        ]),
    ]),

    # Tabs
    dcc.Tabs(id="op-tab", value="receita", children=[
        dcc.Tab(label="Operational Panel", value="painel", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Executive Summary", value="resumo", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Individual Revenue", value="receita", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Fuel", value="comb", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Productivity", value="prod", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Equipment Analysis", value="equip", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Route Analysis", value="rotas", style=tab_style, selected_style=tab_sel_style),
        dcc.Tab(label="Driver Analysis", value="mot", style=tab_style, selected_style=tab_sel_style),
    ], style={"marginBottom": "20px"}),

    html.Div(id="op-content"),
])


@callback(Output("op-content", "children"), Input("op-tab", "value"))
def render(tab):
    if tab == "receita":
        return tab_receita()
    elif tab == "comb":
        return tab_combustivel()
    else:
        return html.Div(style={
            "backgroundColor": WHITE,
            "border": "1px solid " + BORDER,
            "borderRadius": "8px",
            "padding": "60px",
            "textAlign": "center",
            "marginTop": "20px",
        }, children=[
            html.P("📊", style={"fontSize": "48px", "margin": "0"}),
            html.P("Tab under development", style={
                "color": TEXT, "fontSize": "18px", "fontWeight": "600",
            }),
            html.P("This tab is part of the full operational dashboard.", style={
                "color": SEC, "fontSize": "14px",
            }),
        ])


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  SHOWCASE - Operational (Receita + Combustivel)")
    print("  http://127.0.0.1:8061")
    print("=" * 50 + "\n")
    app.run(debug=False, port=8061)
