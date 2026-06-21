"""
SHOWCASE — Painéis de Gestão (Dark Theme)
Manutenção + RH | Dados 100% fictícios
Rodar: python showcase_dark_v3.py → http://127.0.0.1:8050
"""

import dash
from dash import html, dcc, callback, Input, Output
import plotly.graph_objects as go

C = {
    "bg": "#0B1120", "card": "#111B2E", "border": "#1E2D45",
    "text": "#FFFFFF", "sec": "#8896AA",
    "green": "#2ECC71", "red": "#E74C3C", "orange": "#E87722",
    "blue": "#3498DB", "teal": "#1ABC9C", "purple": "#9B59B6", "yellow": "#F1C40F",
}

def BG(): return dict(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color=C["sec"])

def card(children, flex="1", min_w="140px", extra=None):
    s = {"backgroundColor": C["card"], "border": f"1px solid {C['border']}",
         "borderRadius": "8px", "padding": "20px", "flex": flex, "minWidth": min_w}
    if extra: s.update(extra)
    return html.Div(style=s, children=children)

def kpi(title, val, unit, trend, tc, meta):
    return card([
        html.P(title, style={"color":C["sec"],"fontSize":"11px","fontWeight":"600","letterSpacing":"0.5px","margin":"0 0 6px 0"}),
        html.Div(style={"display":"flex","alignItems":"baseline","gap":"4px"}, children=[
            html.Span(val, style={"color":C["text"],"fontSize":"30px","fontWeight":"700"}),
            html.Span(unit, style={"color":C["sec"],"fontSize":"13px"}),
        ]),
        html.P(trend, style={"color":tc,"fontSize":"11px","margin":"6px 0 3px 0"}),
        html.P(meta, style={"color":C["sec"],"fontSize":"10px","margin":"0"}),
    ])

def row(*ch, mb="14px"):
    return html.Div(style={"display":"flex","gap":"14px","marginBottom":mb,"flexWrap":"wrap"}, children=list(ch))

def sem(icon, label, desc, status):
    sc = {"OK":C["green"],"Atenção":C["orange"],"Crítico":C["red"]}
    bg = {"OK":"rgba(46,204,113,0.15)","Atenção":"rgba(232,119,34,0.15)","Crítico":"rgba(231,76,60,0.15)"}
    return html.Div(style={"backgroundColor":C["card"],"border":f"1px solid {C['border']}",
        "borderRadius":"8px","padding":"12px 16px","display":"flex","justifyContent":"space-between","alignItems":"center"}, children=[
        html.Div(style={"display":"flex","alignItems":"center","gap":"10px"}, children=[
            html.Span(icon, style={"fontSize":"17px"}),
            html.Div([
                html.P(label, style={"color":C["text"],"fontSize":"12px","fontWeight":"600","margin":"0"}),
                html.P(desc, style={"color":C["sec"],"fontSize":"10px","margin":"2px 0 0 0"}),
            ]),
        ]),
        html.Span(status, style={"backgroundColor":bg[status],"color":sc[status],
            "padding":"3px 10px","borderRadius":"10px","fontSize":"11px","fontWeight":"600"}),
    ])

def gauge(val, label, meta, color):
    return html.Div(style={"textAlign":"center","flex":"1"}, children=[
        html.Div(val, style={"fontSize":"26px","fontWeight":"700","color":color}),
        html.P(label, style={"color":C["sec"],"fontSize":"10px","margin":"4px 0 2px 0"}),
        html.P(meta, style={"color":C["sec"],"fontSize":"9px","margin":"0"}),
    ])

def header(title, filters):
    return html.Div(style={"display":"flex","justifyContent":"space-between","alignItems":"center","marginBottom":"18px"}, children=[
        html.H2(title, style={"color":C["text"],"fontSize":"16px","fontWeight":"700","letterSpacing":"1px","margin":"0"}),
        html.Div(style={"display":"flex","gap":"8px"}, children=[
            html.Span(f, style={"backgroundColor":C["card"],"color":C["text"],"padding":"5px 12px",
                "borderRadius":"6px","fontSize":"11px","border":f"1px solid {C['border']}"}) for f in filters
        ]),
    ])

def sec_label(txt):
    return html.P(txt, style={"color":C["sec"],"fontSize":"11px","fontWeight":"600","letterSpacing":"0.5px","margin":"0 0 10px 0"})

# ── MANUTENÇÃO ──────────────────────────────────────────────

def tab_manutencao():
    meses = ["Dez","Jan","Fev","Mar","Abr","Mai"]

    fig_fat = go.Figure()
    fig_fat.add_trace(go.Bar(x=meses, y=[185,210,195,230,248,218], name="Custo Manut.",
        marker_color=C["orange"], opacity=0.85,
        text=["185K","210K","195K","230K","248K","218K"], textposition="outside", textfont=dict(color=C["orange"],size=9)))
    fig_fat.add_trace(go.Scatter(x=meses, y=[950,1020,980,1100,1150,1070], name="Faturamento",
        mode="lines+markers", line=dict(color=C["green"],width=2), marker=dict(size=5)))
    fig_fat.update_layout(**BG(), height=220, margin=dict(l=20,r=20,t=10,b=30),
        showlegend=True, legend=dict(orientation="h",y=1.12,font=dict(size=9,color=C["sec"])),
        yaxis=dict(showgrid=True,gridcolor="rgba(255,255,255,0.05)"), xaxis=dict(showgrid=False))

    fig_frota = go.Figure(go.Pie(
        labels=["Liberado","Restritivo","Em Manut.","Impeditivo"],
        values=[108,16,14,10], hole=0.65,
        marker_colors=[C["green"],C["orange"],C["blue"],C["red"]],
        textinfo="percent", textfont=dict(color=C["text"],size=10)))
    fig_frota.update_layout(**BG(), height=220, margin=dict(l=20,r=20,t=10,b=10),
        showlegend=True, legend=dict(orientation="v",x=1.05,y=0.5,font=dict(size=10,color=C["sec"])),
        annotations=[dict(text="<b>148</b><br><span style='font-size:9px'>VEÍCULOS</span>",
            x=0.5,y=0.5,font_size=20,font_color=C["text"],showarrow=False)])

    fig_custos = go.Figure(go.Bar(
        y=["Reforma","Socorro","Pneus","Corretiva","Prev+ITR"],
        x=[31,42,89,107,128], orientation="h",
        marker_color=[C["purple"],C["yellow"],C["red"],C["orange"],C["blue"]],
        text=["R$31K","R$42K","R$89K","R$107K","R$128K"], textposition="outside",
        textfont=dict(color=C["text"],size=10)))
    fig_custos.update_layout(**BG(), height=220, margin=dict(l=110,r=60,t=10,b=10),
        showlegend=False, xaxis=dict(showgrid=False,showticklabels=False), yaxis=dict(showgrid=False))

    return html.Div([
        header("RESUMO — MANUTENÇÃO (GESTÃO)", ["2026","Jan – Mai","Todas as Frotas"]),
        row(
            kpi("DISPONIBILIDADE","91.7","%","▲ 0.9% vs mês ant.",C["green"],"Meta: ≥ 92%"),
            kpi("IMPEDITIVOS","8","","▼ 2 vs mês ant.",C["green"],"Veículos parados"),
            kpi("CUSTO / KM","0.92","R$","▲ R$0.06 vs mês ant.",C["red"],"Meta: ≤ R$0.85"),
            kpi("CMF","7.1","%","▲ 0.3% vs mês ant.",C["orange"],"Meta: ≤ 7%"),
            kpi("% SOCORRO","4.3","%","▼ 0.8% vs mês ant.",C["green"],"Meta: ≤ 5%"),
            kpi("KM RODADO","2.1","M","▲ 8% vs mês ant.",C["green"],"148 veículos ativos"),
        ),
        row(
            card([sec_label("FATURAMENTO VS CUSTO MANUTENÇÃO"), dcc.Graph(figure=fig_fat,config={"displayModeBar":False})], flex="1.2", min_w="300px"),
            card([sec_label("COMPOSIÇÃO DA FROTA"), dcc.Graph(figure=fig_frota,config={"displayModeBar":False})], min_w="280px"),
            card([sec_label("CUSTO POR TIPO DE OS"), dcc.Graph(figure=fig_custos,config={"displayModeBar":False})], min_w="280px"),
        ),
        row(
            card([
                sec_label("SEMÁFORO OPERACIONAL"),
                html.Div(style={"display":"grid","gridTemplateColumns":"1fr 1fr","gap":"10px"}, children=[
                    sem("🚛","Disponibilidade","91.7% — próximo da meta (92%)","Atenção"),
                    sem("💰","CMF (Custo/Fat.)","7.1% — acima do limite (7%)","Crítico"),
                    sem("🚨","Socorro","4.3% — dentro do limite (5%)","OK"),
                    sem("🔧","Pneus","87% seguros — 0 críticos","OK"),
                ]),
            ], min_w="400px"),
            card([
                sec_label("INDICADORES FINANCEIROS"),
                html.Div(style={"display":"flex","justifyContent":"space-around","padding":"20px 0"}, children=[
                    gauge("R$0.92","Custo / KM","Meta: ≤ R$0.85",C["orange"]),
                    gauge("7.1%","CMF","Meta: ≤ 7%",C["red"]),
                    gauge("R$1.18","Custo KM + M.O","Meta: ≤ R$1.10",C["red"]),
                ]),
            ], min_w="400px"),
        ),
    ])

# ── RH ──────────────────────────────────────────────────────

def tab_rh():
    meses = ["Dez","Jan","Fev","Mar","Abr","Mai"]

    fig_fopag = go.Figure()
    fig_fopag.add_trace(go.Bar(x=meses, y=[598,612,645,631,658,683], name="Fopag",
        marker_color=C["blue"], opacity=0.8,
        text=["598K","612K","645K","631K","658K","683K"], textposition="outside", textfont=dict(color=C["blue"],size=9)))
    fig_fopag.add_trace(go.Bar(x=meses, y=[28,35,42,38,41,37], name="Hora Extra", marker_color=C["orange"], opacity=0.8))
    fig_fopag.add_hline(y=720, line_dash="dash", line_color=C["red"], opacity=0.6,
        annotation_text="Meta 720K", annotation_font_color=C["red"], annotation_font_size=10)
    fig_fopag.update_layout(**BG(), height=220, margin=dict(l=20,r=20,t=10,b=30),
        barmode="stack", showlegend=True, legend=dict(orientation="h",y=1.12,font=dict(size=9,color=C["sec"])),
        yaxis=dict(showgrid=True,gridcolor="rgba(255,255,255,0.05)"), xaxis=dict(showgrid=False))

    fig_folha = go.Figure(go.Pie(
        labels=["Salário Base","Hora Extra","Benefícios","Rescisões","Outros"],
        values=[358,37,79,52,157], hole=0.65,
        marker_colors=[C["blue"],C["orange"],C["green"],C["red"],C["sec"]],
        textinfo="percent", textfont=dict(color=C["text"],size=10)))
    fig_folha.update_layout(**BG(), height=220, margin=dict(l=20,r=20,t=10,b=10),
        showlegend=True, legend=dict(orientation="v",x=1.05,y=0.5,font=dict(size=10,color=C["sec"])),
        annotations=[dict(text="<b>R$683K</b><br><span style='font-size:9px'>FOPAG</span>",
            x=0.5,y=0.5,font_size=17,font_color=C["text"],showarrow=False)])

    fig_punicao = go.Figure(go.Bar(
        y=["Irreg. Ponto","Falta/Atraso","Quebra Interst.","Uso Celular","Exc. Velocidade"],
        x=[2,3,3,4,6], orientation="h",
        marker_color=[C["yellow"],C["yellow"],C["orange"],C["orange"],C["red"]],
        text=[2,3,3,4,6], textposition="outside", textfont=dict(color=C["text"],size=11)))
    fig_punicao.update_layout(**BG(), height=220, margin=dict(l=120,r=40,t=10,b=10),
        showlegend=False, xaxis=dict(showgrid=False,showticklabels=False), yaxis=dict(showgrid=False))

    return html.Div([
        header("RESUMO — RH (GESTÃO)", ["2026","Jan – Mai"]),
        row(
            kpi("FOPAG TOTAL","683","K","▼ 2% vs mês ant.",C["green"],"Meta: ≤ R$720K"),
            kpi("HORA EXTRA","37","K","▼ 10% vs mês ant.",C["green"],"5.4% da Fopag (meta ≤5%)"),
            kpi("% PREMIADOS","74","%","▲ 3% vs mês ant.",C["green"],"Meta: ≥ 60% | Ticket R$1.6K"),
            kpi("PUNIÇÕES","18","","▼ 4 vs mês ant.",C["green"],"14 advert. | 4 suspensões"),
            kpi("ABSENTEÍSMO","385","h","▼ 9% vs mês ant.",C["green"],"Meta: ≤ 450h/mês"),
            kpi("SLA CONTRATAÇÃO","28","dias","▼ 3d vs mês ant.",C["green"],"Meta: ≤ 30 dias | 2 vagas"),
        ),
        row(
            card([sec_label("FOPAG + HORA EXTRA (6 MESES)"), dcc.Graph(figure=fig_fopag,config={"displayModeBar":False})], flex="1.2", min_w="300px"),
            card([sec_label("COMPOSIÇÃO DA FOLHA"), dcc.Graph(figure=fig_folha,config={"displayModeBar":False})], min_w="280px"),
            card([sec_label("TOP 5 MOTIVOS DE PUNIÇÃO"), dcc.Graph(figure=fig_punicao,config={"displayModeBar":False})], min_w="280px"),
        ),
        row(
            card([
                sec_label("SEMÁFORO POR ÁREA"),
                html.Div(style={"display":"grid","gridTemplateColumns":"1fr 1fr 1fr","gap":"10px"}, children=[
                    sem("💰","Folha","R$683K — abaixo de R$720K","OK"),
                    sem("⏰","Hora Extra","5.4% da Fopag — meta ≤5%","Atenção"),
                    sem("🏆","Premiação","74% premiados — acima de 60%","OK"),
                    sem("⚠","Disciplina","18 punições — abaixo do limite 20","OK"),
                    sem("📋","Absenteísmo","385h — abaixo de 450h","OK"),
                    sem("📝","SLA Contratação","28 dias — meta ≤30 dias","Atenção"),
                ]),
            ], min_w="400px"),
            card([
                sec_label("INDICADORES % SOBRE FATURAMENTO"),
                html.Div(style={"display":"flex","justifyContent":"space-around","padding":"20px 0"}, children=[
                    gauge("16.8%","Fopag / Fat.","Meta: ≤ 18%",C["green"]),
                    gauge("5.4%","HE / Fopag","Meta: ≤ 5%",C["orange"]),
                    gauge("0.9%","HE / Fat.","Meta: ≤ 1.5%",C["green"]),
                ]),
            ], min_w="400px"),
        ),
    ])

# ── APP ─────────────────────────────────────────────────────

app = dash.Dash(__name__)

ts = {"padding":"10px 20px","fontSize":"13px","fontWeight":"500","color":C["sec"],
      "backgroundColor":"transparent","border":"none","borderBottom":"2px solid transparent"}
tsel = {**ts, "color":C["orange"], "borderBottom":f"2px solid {C['orange']}", "fontWeight":"600"}

app.layout = html.Div(style={"backgroundColor":C["bg"],"minHeight":"100vh","padding":"24px 32px",
    "fontFamily":"'Segoe UI','Inter',sans-serif"}, children=[
    dcc.Tabs(id="tab", value="manutencao", children=[
        dcc.Tab(label="🔧  Manutenção", value="manutencao", style=ts, selected_style=tsel),
        dcc.Tab(label="👥  RH",          value="rh",          style=ts, selected_style=tsel),
    ], style={"marginBottom":"24px"}),
    html.Div(id="content"),
])

@callback(Output("content","children"), Input("tab","value"))
def render(t):
    return tab_manutencao() if t == "manutencao" else tab_rh()

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  SHOWCASE — Dark Panels (Manutenção + RH)")
    print("  http://127.0.0.1:8050")
    print("="*50 + "\n")
    app.run(debug=False, port=8060)
