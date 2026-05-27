import os
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from styles import (
    apply_styles, COLORS, COLOR_SCALE, COLOR_MAP_UTIL,
    AMAZON_NAVY, AMAZON_ORANGE, plotly_layout_base
)

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="ReviewSense — Amazon Fine Food",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_styles()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def cargar_datos():
    ruta = os.path.join(BASE_DIR, "data", "processed", "reviews_limpias.parquet")
    return pd.read_parquet(ruta)

df = cargar_datos()
df['Time'] = pd.to_datetime(df['Time'])

# ── Mapa ProductId → nombre legible ──────────────────────────────────
# nombre_producto viene del parquet; se usa el primero registrado por producto
id_a_nombre = (
    df[['ProductId', 'nombre_producto']]
    .drop_duplicates('ProductId')
    .set_index('ProductId')['nombre_producto']
    .str.strip()
    .str[:60]   # truncar nombres muy largos para que quepan en graficos
)

def nombre_producto(pid):
    """Retorna nombre legible de un ProductId, o el codigo si no existe."""
    return id_a_nombre.get(pid, pid)

# ── Categorias de producto por palabras clave ────────────────────────
_CATEGORIAS_KW = {
    'Bebidas y Cafe':      ['coffee','tea','drink','beverage','juice','water','soda','espresso','latte','chai','cocoa','smoothie','energy drink'],
    'Snacks y Dulces':     ['chip','cookie','candy','chocolate','gummy','snack','cracker','popcorn','pretzel','bar','brownie','twizzler','gum'],
    'Cereales y Granos':   ['oatmeal','cereal','granola','grain','rice','pasta','flour','oat','wheat','quinoa','barley'],
    'Condimentos y Salsas':['sauce','salsa','dressing','vinegar','mustard','ketchup','mayo','seasoning','spice','pepper','salt','soy sauce','hot sauce'],
    'Salud y Suplementos': ['vitamin','supplement','protein','organic','natural','health','probiotic','omega','fiber','antioxidant'],
    'Mascotas':            ['cat','dog','pet','kitten','puppy','animal','feline','canine'],
    'Lacteos y Huevos':    ['cheese','milk','butter','cream','yogurt','egg','dairy'],
    'Carnes y Mariscos':   ['meat','fish','chicken','beef','tuna','salmon','shrimp','turkey','pork'],
    'Frutas y Verduras':   ['fruit','vegetable','apple','berry','dried','nut','almond','cashew','raisin'],
    'Panaderia':           ['bread','cake','muffin','biscuit','pastry','bagel','roll'],
}

@st.cache_data
def agregar_categoria(df_):
    """Agrega columna 'categoria' al dataframe basandose en texto de resena."""
    prod_texto = (
        df_[['ProductId','nombre_producto','Text']]
        .drop_duplicates('ProductId')
        .copy()
    )
    def _cat(row):
        texto = (str(row['nombre_producto']) + ' ' + str(row['Text'])).lower()
        for cat, words in _CATEGORIAS_KW.items():
            if any(w in texto for w in words):
                return cat
        return 'Otros Alimentos'
    prod_texto['categoria'] = prod_texto.apply(_cat, axis=1)
    return df_.merge(prod_texto[['ProductId','categoria']], on='ProductId', how='left')

df = agregar_categoria(df)

# ── Sidebar ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ReviewSense")
    st.markdown("---")

    # Rango de años con slider
    anio_min = int(df['Time'].dt.year.min())
    anio_max = int(df['Time'].dt.year.max())
    st.markdown("#### Periodo")
    rango_anios = st.slider(
        "Años", min_value=anio_min, max_value=anio_max,
        value=(anio_min, anio_max), step=1,
        format="%d"
    )

    st.markdown("#### Calificacion")
    scores = st.multiselect(
        "Estrellas", options=[1, 2, 3, 4, 5], default=[1, 2, 3, 4, 5],
        help="Filtra por calificacion de la resena"
    )

    st.markdown("#### Utilidad")
    utilidad = st.radio(
        "Mostrar", options=["Todas", "Utiles", "No utiles"],
        horizontal=False
    )

    st.markdown("#### Longitud")
    max_words = int(df['word_count'].quantile(0.95))
    rango_palabras = st.slider(
        "Palabras en resena", min_value=0, max_value=max_words,
        value=(0, max_words)
    )

    st.markdown("#### Tipo de Producto")
    usar_filtro_producto = st.checkbox("Filtrar por tipo", value=False)
    cats_sel_sidebar = []
    if usar_filtro_producto:
        cats_disponibles = sorted(df['categoria'].dropna().unique().tolist())
        cats_sel_sidebar = st.multiselect(
            "Categoria", options=cats_disponibles,
            default=cats_disponibles[:3]
        )

    st.markdown("---")
    st.markdown("""
        <div style='color:#febd69; font-size:0.85rem; font-weight:700; margin-bottom:0.3rem'>Grupo 06</div>
        <div style='color:white; font-size:0.78rem; line-height:1.8'>
            Byron Torres<br>
            Jose Arevalo<br>
            Monica Cholango
        </div>
        <div style='color:#666; font-size:0.72rem; margin-top:0.5rem'>UniAndes 2026</div>
    """, unsafe_allow_html=True)

# ── Aplicar filtros ──────────────────────────────────────────────────
fecha_inicio = pd.Timestamp(f"{rango_anios[0]}-01-01")
fecha_fin    = pd.Timestamp(f"{rango_anios[1]}-12-31")

df_f = df[
    (df['Time'] >= fecha_inicio) &
    (df['Time'] <= fecha_fin) &
    (df['Score'].isin(scores)) &
    (df['word_count'] >= rango_palabras[0]) &
    (df['word_count'] <= rango_palabras[1])
]

if utilidad == "Utiles":
    df_f = df_f[df_f['es_util'] == 1]
elif utilidad == "No utiles":
    df_f = df_f[df_f['es_util'] == 0]

if usar_filtro_producto and cats_sel_sidebar:
    df_f = df_f[df_f['categoria'].isin(cats_sel_sidebar)]

if df_f.empty:
    st.warning("Los filtros no arrojan resultados. Ajusta los filtros en el panel lateral.")
    st.stop()

# ── Contexto de seleccion interactiva ────────────────────────────────
# Permite que los graficos filtren los KPIs al hacer clic
if "kpi_filter" not in st.session_state:
    st.session_state["kpi_filter"] = None   # None = sin filtro adicional

# df para KPIs: aplica filtro interactivo si existe
kpi_filter = st.session_state["kpi_filter"]
if kpi_filter:
    df_kpi = df_f[df_f[kpi_filter["col"]] == kpi_filter["val"]]
    kpi_label = kpi_filter["label"]
else:
    df_kpi = df_f
    kpi_label = None

# ── Header ───────────────────────────────────────────────────────────
st.markdown("""
    <div class="main-header">
        <h1>ReviewSense</h1>
        <p>Analisis Inteligente de Resenas — Amazon Fine Food Reviews</p>
    </div>
""", unsafe_allow_html=True)

if usar_filtro_producto and cats_sel_sidebar:
    badges = " ".join([f"<span class='product-badge'>{c}</span>" for c in cats_sel_sidebar])
    st.markdown(f"<div style='margin-bottom:1rem'>Tipos: {badges}</div>", unsafe_allow_html=True)

# ── KPIs — reaccionan al filtro interactivo ──────────────────────────
if kpi_label:
    st.markdown(
        f"<div class='info-box' style='margin-bottom:1rem'>Metricas para: <b>{kpi_label}</b> "
        f"&nbsp;·&nbsp; <a href='?reset=1' style='color:{AMAZON_ORANGE}'>Ver todo</a></div>",
        unsafe_allow_html=True
    )
    # Boton para limpiar seleccion
    if st.button("Limpiar seleccion", key="clear_kpi"):
        st.session_state["kpi_filter"] = None
        st.rerun()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Total Resenas</div>
        <div class="kpi-value">{len(df_kpi):,}</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Score Promedio</div>
        <div class="kpi-value">{df_kpi['Score'].mean():.2f} / 5</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Resenas Utiles</div>
        <div class="kpi-value">{df_kpi['es_util'].mean()*100:.1f}%</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Sentimiento VADER</div>
        <div class="kpi-value">{df_kpi['vader_compound'].mean():.2f}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── 4 Pestanas ───────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Calificaciones y Sentimiento",
    "Tendencia y Longitud",
    "Productos",
    "Prediccion",
])

# ════════════════════════════════════════════════════════════════════
# TAB 1: Calificaciones + Sentimiento
# ════════════════════════════════════════════════════════════════════
with tab1:
    col1, col2 = st.columns(2)

    # ── Distribucion de Calificaciones ──
    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Distribucion de Calificaciones</div>', unsafe_allow_html=True)
        score_counts = df_f['Score'].value_counts().sort_index().reset_index()
        score_counts.columns = ['Score', 'Cantidad']
        fig = px.bar(score_counts, x='Score', y='Cantidad',
                     color='Score', color_discrete_sequence=COLORS, text='Cantidad')
        fig.update_traces(textposition='outside')
        fig.update_layout(**plotly_layout_base(), showlegend=False,
                          xaxis_title="Estrellas", yaxis_title="Cantidad")
        selected = st.plotly_chart(fig, use_container_width=True, on_select="rerun", key="bar_score")
        if selected and selected.get("selection", {}).get("points"):
            score_sel = int(selected["selection"]["points"][0]["x"])
            st.session_state["kpi_filter"] = {"col": "Score", "val": score_sel, "label": f"Score {score_sel}"}
            df_sel = df_f[df_f['Score'] == score_sel]
            st.markdown(f"""<div class="info-box">
                <b>Score {score_sel} seleccionado</b><br>
                Resenas: {len(df_sel):,} &nbsp;|&nbsp;
                Sentimiento: {df_sel['vader_compound'].mean():.2f} &nbsp;|&nbsp;
                Utiles: {df_sel['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
                Palabras prom.: {df_sel['word_count'].mean():.0f}
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Utiles vs No Utiles ──
    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Resenas Utiles vs No Utiles</div>', unsafe_allow_html=True)
        util_count = df_f['es_util'].value_counts().reset_index()
        util_count.columns = ['es_util', 'count']
        util_count['label'] = util_count['es_util'].map({1: 'Util', 0: 'No util'})
        fig2 = px.pie(util_count, values='count', names='label',
                      color_discrete_sequence=[AMAZON_ORANGE, AMAZON_NAVY], hole=0.4)
        fig2.update_layout(**plotly_layout_base())
        selected2 = st.plotly_chart(fig2, use_container_width=True, on_select="rerun", key="pie_util")
        if selected2 and selected2.get("selection", {}).get("points"):
            label_sel = selected2["selection"]["points"][0]["label"]
            val_sel = 1 if label_sel == "Util" else 0
            st.session_state["kpi_filter"] = {"col": "es_util", "val": val_sel, "label": label_sel}
            df_sel2 = df_f[df_f['es_util'] == val_sel]
            st.markdown(f"""<div class="info-box">
                <b>{label_sel} seleccionado</b><br>
                Resenas: {len(df_sel2):,} &nbsp;|&nbsp;
                Score prom.: {df_sel2['Score'].mean():.2f} &nbsp;|&nbsp;
                Sentimiento: {df_sel2['vader_compound'].mean():.2f} &nbsp;|&nbsp;
                Palabras prom.: {df_sel2['word_count'].mean():.0f}
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Segunda fila: Sentimiento ──
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="chart-card"><div class="chart-title">Sentimiento VADER por Calificacion</div>', unsafe_allow_html=True)
        vader_score = df_f.groupby('Score')['vader_compound'].mean().reset_index()
        fig4 = px.bar(vader_score, x='Score', y='vader_compound',
                      color='vader_compound', text=vader_score['vader_compound'].round(2),
                      color_continuous_scale=COLOR_SCALE)
        fig4.update_traces(textposition='outside')
        fig4.update_layout(**plotly_layout_base(), xaxis_title="Estrellas", yaxis_title="Sentimiento promedio")
        selected4 = st.plotly_chart(fig4, use_container_width=True, on_select="rerun", key="bar_vader")
        if selected4 and selected4.get("selection", {}).get("points"):
            score_vader = int(selected4["selection"]["points"][0]["x"])
            st.session_state["kpi_filter"] = {"col": "Score", "val": score_vader, "label": f"Score {score_vader} — Sentimiento"}
            df_vader = df_f[df_f['Score'] == score_vader]
            st.markdown(f"""<div class="info-box">
                <b>Score {score_vader}</b><br>
                VADER promedio: {df_vader['vader_compound'].mean():.3f} &nbsp;|&nbsp;
                Positivos: {(df_vader['vader_compound'] > 0).mean()*100:.1f}% &nbsp;|&nbsp;
                Resenas: {len(df_vader):,}
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="chart-card"><div class="chart-title">Distribucion de Sentimiento VADER</div>', unsafe_allow_html=True)
        fig_vader = px.histogram(df_f, x='vader_compound', nbins=50, color_discrete_sequence=[AMAZON_NAVY])
        fig_vader.add_vline(x=0, line_dash='dash', line_color=AMAZON_ORANGE,
                            annotation_text="Neutro", annotation_font_color=AMAZON_ORANGE)
        fig_vader.update_layout(**plotly_layout_base(), xaxis_title="Score VADER", yaxis_title="Frecuencia")
        st.plotly_chart(fig_vader, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# TAB 2: Tendencia Temporal + Longitud y Utilidad
# ════════════════════════════════════════════════════════════════════
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Volumen de Resenas por Ano</div>', unsafe_allow_html=True)
        vol = df_f.groupby('Year').size().reset_index(name='count')
        fig3 = px.area(vol, x='Year', y='count', color_discrete_sequence=[AMAZON_ORANGE], markers=True)
        fig3.update_traces(fill='tozeroy', fillcolor='rgba(255,153,0,0.15)')
        fig3.update_layout(**plotly_layout_base(), xaxis_title="Ano", yaxis_title="Resenas")
        selected3 = st.plotly_chart(fig3, use_container_width=True, on_select="rerun", key="area_vol")
        if selected3 and selected3.get("selection", {}).get("points"):
            anio_sel = int(selected3["selection"]["points"][0]["x"])
            st.session_state["kpi_filter"] = {"col": "Year", "val": anio_sel, "label": f"Ano {anio_sel}"}
            df_sel3 = df_f[df_f['Year'] == anio_sel]
            st.markdown(f"""<div class="info-box">
                <b>Ano {anio_sel}</b><br>
                Resenas: {len(df_sel3):,} &nbsp;|&nbsp;
                Score prom.: {df_sel3['Score'].mean():.2f} &nbsp;|&nbsp;
                Utiles: {df_sel3['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
                Sentimiento: {df_sel3['vader_compound'].mean():.2f}
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Score Promedio por Ano</div>', unsafe_allow_html=True)
        score_anio = df_f.groupby('Year')['Score'].mean().reset_index()
        fig6 = px.line(score_anio, x='Year', y='Score', markers=True, color_discrete_sequence=[AMAZON_NAVY])
        fig6.add_hline(y=df_f['Score'].mean(), line_dash='dash', line_color=AMAZON_ORANGE,
                       annotation_text=f"Promedio: {df_f['Score'].mean():.2f}",
                       annotation_font_color=AMAZON_ORANGE)
        fig6.update_layout(**plotly_layout_base(), xaxis_title="Ano", yaxis_title="Score promedio")
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-card"><div class="chart-title">Resenas por Mes del Ano</div>', unsafe_allow_html=True)
    meses = {1:'Ene',2:'Feb',3:'Mar',4:'Abr',5:'May',6:'Jun',
             7:'Jul',8:'Ago',9:'Sep',10:'Oct',11:'Nov',12:'Dic'}
    vol_mes = df_f.groupby('Month').size().reset_index(name='count')
    vol_mes['mes_nombre'] = vol_mes['Month'].map(meses)
    fig_mes = px.bar(vol_mes, x='mes_nombre', y='count',
                     color_discrete_sequence=[AMAZON_ORANGE], text='count')
    fig_mes.update_traces(textposition='outside')
    fig_mes.update_layout(**plotly_layout_base(), xaxis_title="Mes", yaxis_title="Resenas")
    selected_mes = st.plotly_chart(fig_mes, use_container_width=True, on_select="rerun", key="bar_mes")
    if selected_mes and selected_mes.get("selection", {}).get("points"):
        mes_sel_nombre = selected_mes["selection"]["points"][0]["x"]
        mes_num = {v: k for k, v in meses.items()}[mes_sel_nombre]
        st.session_state["kpi_filter"] = {"col": "Month", "val": mes_num, "label": f"Mes {mes_sel_nombre}"}
        df_mes_sel = df_f[df_f['Month'] == mes_num]
        st.markdown(f"""<div class="info-box">
            <b>{mes_sel_nombre} seleccionado</b><br>
            Resenas: {len(df_mes_sel):,} &nbsp;|&nbsp;
            Score prom.: {df_mes_sel['Score'].mean():.2f} &nbsp;|&nbsp;
            Utiles: {df_mes_sel['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
            Sentimiento: {df_mes_sel['vader_compound'].mean():.2f}
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Longitud y Utilidad ──
    st.markdown("<hr>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="chart-card"><div class="chart-title">Longitud de Resena vs Utilidad</div>', unsafe_allow_html=True)
        fig5 = px.box(df_f[df_f['word_count'] < 500], x='es_util', y='word_count',
                      color='es_util', color_discrete_map=COLOR_MAP_UTIL)
        fig5.update_layout(**plotly_layout_base(),
                           xaxis_title="0 = No util | 1 = Util",
                           yaxis_title="Palabras", showlegend=False)
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="chart-card"><div class="chart-title">Palabras Promedio por Calificacion</div>', unsafe_allow_html=True)
        words_score = df_f.groupby('Score')['word_count'].mean().reset_index()
        words_score['word_count'] = words_score['word_count'].round(0)
        fig_ws = px.bar(words_score, x='Score', y='word_count',
                        color_discrete_sequence=['#37475a'], text='word_count')
        fig_ws.update_traces(textposition='outside')
        fig_ws.update_layout(**plotly_layout_base(), xaxis_title="Estrellas", yaxis_title="Palabras promedio")
        selected_ws = st.plotly_chart(fig_ws, use_container_width=True, on_select="rerun", key="bar_words")
        if selected_ws and selected_ws.get("selection", {}).get("points"):
            score_ws = int(selected_ws["selection"]["points"][0]["x"])
            st.session_state["kpi_filter"] = {"col": "Score", "val": score_ws, "label": f"Score {score_ws} — Longitud"}
            df_ws = df_f[df_f['Score'] == score_ws]
            st.markdown(f"""<div class="info-box">
                <b>Score {score_ws}</b><br>
                Palabras prom.: {df_ws['word_count'].mean():.0f} &nbsp;|&nbsp;
                Largas (>200): {(df_ws['word_count'] > 200).mean()*100:.1f}% &nbsp;|&nbsp;
                Utiles: {df_ws['es_util'].mean()*100:.1f}%
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# TAB 3: Productos + Explorador
# ════════════════════════════════════════════════════════════════════
with tab3:
    # ── Graficos de Categoria ──
    cat_resumen = (
        df_f.groupby('categoria').agg(
            Resenas=('Score','count'),
            Score_Prom=('Score','mean'),
            Pct_Util=('es_util','mean'),
            VADER_Prom=('vader_compound','mean')
        ).reset_index()
    )
    cat_resumen['Score_Prom'] = cat_resumen['Score_Prom'].round(2)
    cat_resumen['Pct_Util']   = (cat_resumen['Pct_Util'] * 100).round(1)
    cat_resumen['VADER_Prom'] = cat_resumen['VADER_Prom'].round(3)

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown('<div class="chart-card"><div class="chart-title">Resenas por Categoria de Producto</div>', unsafe_allow_html=True)
        fig_cat = px.bar(cat_resumen.sort_values('Resenas'),
                         x='Resenas', y='categoria', orientation='h',
                         color='Score_Prom', color_continuous_scale=COLOR_SCALE, text='Resenas')
        fig_cat.update_traces(textposition='outside')
        fig_cat.update_layout(**plotly_layout_base(), yaxis_title="", xaxis_title="Numero de resenas")
        selected_cat = st.plotly_chart(fig_cat, use_container_width=True, on_select="rerun", key="bar_cat")
        if selected_cat and selected_cat.get("selection", {}).get("points"):
            cat_sel_val = selected_cat["selection"]["points"][0]["y"]
            st.session_state["kpi_filter"] = {"col": "categoria", "val": cat_sel_val, "label": cat_sel_val}
            df_cat_sel = df_f[df_f['categoria'] == cat_sel_val]
            st.markdown(f"""<div class="info-box">
                <b>{cat_sel_val}</b><br>
                Resenas: {len(df_cat_sel):,} &nbsp;|&nbsp;
                Score prom.: {df_cat_sel['Score'].mean():.2f} &nbsp;|&nbsp;
                Utiles: {df_cat_sel['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
                Sentimiento: {df_cat_sel['vader_compound'].mean():.2f}
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_c2:
        st.markdown('<div class="chart-card"><div class="chart-title">Score Promedio y % Utiles por Categoria</div>', unsafe_allow_html=True)
        fig_cat2 = px.scatter(cat_resumen, x='Score_Prom', y='Pct_Util',
                              size='Resenas', color='categoria',
                              hover_name='categoria',
                              labels={'Score_Prom':'Score promedio','Pct_Util':'% Utiles','Resenas':'Resenas'})
        fig_cat2.update_layout(**plotly_layout_base(), xaxis_title="Score promedio", yaxis_title="% Resenas Utiles")
        st.plotly_chart(fig_cat2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-card"><div class="chart-title">Tabla Resumen por Categoria</div>', unsafe_allow_html=True)
    tabla_cat = cat_resumen.sort_values('Resenas', ascending=False).copy()
    tabla_cat.columns = ['Categoria', 'Resenas', 'Score Prom.', '% Util', 'VADER Prom.']
    tabla_cat.index = range(1, len(tabla_cat)+1)

    # Fila de totales
    fila_total = pd.DataFrame([{
        'Categoria': 'TOTAL',
        'Resenas': tabla_cat['Resenas'].sum(),
        'Score Prom.': (df_f['Score'].mean()).round(2),
        '% Util': (df_f['es_util'].mean() * 100).round(1),
        'VADER Prom.': (df_f['vader_compound'].mean()).round(3),
    }], index=[''])
    tabla_con_total = pd.concat([tabla_cat, fila_total])

    def color_score(val):
        try:
            v = float(val)
            if v >= 4.0:   return 'background-color: #c6efce; color: #276221'
            elif v >= 3.0: return 'background-color: #ffeb9c; color: #9c5700'
            else:          return 'background-color: #ffc7ce; color: #9c0006'
        except: return ''

    st.dataframe(
        tabla_con_total.style
            .format({'Score Prom.': '{:.2f}', '% Util': '{:.1f}%', 'VADER Prom.': '{:.3f}', 'Resenas': '{:,.0f}'})
            .map(color_score, subset=pd.IndexSlice[tabla_cat.index, ['Score Prom.']])
            .apply(lambda x: ['background-color: #232f3e; color: #ff9900; font-weight: bold'
                              if x.name == '' else '' for _ in x], axis=1),
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Detalle por categoria ──
    cats_unicas = sorted(df_f['categoria'].dropna().unique().tolist())

    st.markdown('<div class="chart-card"><div class="chart-title">Detalle de Categoria</div>', unsafe_allow_html=True)
    cat_elegida = st.selectbox("Tipo de categoria:", options=cats_unicas, key="cat_detalle")

    df_cat_prod = df_f[df_f['categoria'] == cat_elegida]
    resumen_productos = (
        df_cat_prod.groupby('ProductId').agg(
            Resenas=('Score', 'count'),
            Score_Prom=('Score', 'mean'),
            VADER_Prom=('vader_compound', 'mean'),
            Pct_Util=('es_util', 'mean')
        )
        .sort_values('Resenas', ascending=False).reset_index()
    )
    resumen_productos['Nombre']     = resumen_productos['ProductId'].map(lambda pid: id_a_nombre.get(pid, pid)[:50])
    resumen_productos['Score_Prom'] = resumen_productos['Score_Prom'].round(2)
    resumen_productos['VADER_Prom'] = resumen_productos['VADER_Prom'].round(3)
    resumen_productos['Pct_Util']   = (resumen_productos['Pct_Util'] * 100).round(1)

    d1, d2, d3, d4 = st.columns(4)
    d1.metric("Resenas", f"{len(df_cat_prod):,}")
    d2.metric("Score promedio", f"{df_cat_prod['Score'].mean():.2f}")
    d3.metric("% Utiles", f"{df_cat_prod['es_util'].mean()*100:.1f}%")
    d4.metric("Sentimiento VADER", f"{df_cat_prod['vader_compound'].mean():.2f}")

    resumen_tabla_cat = resumen_productos[['Nombre', 'Resenas', 'Score_Prom', 'Pct_Util', 'VADER_Prom']].copy()
    resumen_tabla_cat.columns = ['Producto', 'Resenas', 'Score Prom.', '% Util', 'VADER Prom.']
    resumen_tabla_cat.index = range(1, len(resumen_tabla_cat) + 1)
    st.dataframe(
        resumen_tabla_cat.style.format({
            'Score Prom.': '{:.2f}', '% Util': '{:.1f}%', 'VADER Prom.': '{:.3f}'
        }).map(color_score, subset=['Score Prom.']),
        use_container_width=True, height=400
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Explorador ──
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="chart-card"><div class="chart-title">Explorador de Resenas</div>', unsafe_allow_html=True)
    st.markdown("Busca resenas por palabra clave combinando con los filtros del panel izquierdo.")

    col_b1, col_b2, col_b3 = st.columns([3, 1, 1])
    with col_b1:
        busqueda = st.text_input("Buscar en el texto", placeholder="Ej: delicious, terrible, packaging...")
    with col_b2:
        score_filtro = st.selectbox("Score", options=["Todos", 1, 2, 3, 4, 5])
    with col_b3:
        util_filtro = st.selectbox("Utilidad", options=["Todos", "Util", "No util"])

    df_busq = df_f.copy()
    if busqueda:
        df_busq = df_busq[df_busq['Text'].str.contains(busqueda, case=False, na=False)]
    if score_filtro != "Todos":
        df_busq = df_busq[df_busq['Score'] == score_filtro]
    if util_filtro == "Util":
        df_busq = df_busq[df_busq['es_util'] == 1]
    elif util_filtro == "No util":
        df_busq = df_busq[df_busq['es_util'] == 0]

    st.markdown(f"""<div class="info-box">
        Encontradas <b>{len(df_busq):,}</b> resenas &nbsp;|&nbsp;
        Score prom.: <b>{df_busq['Score'].mean():.2f}</b> &nbsp;|&nbsp;
        Utiles: <b>{df_busq['es_util'].mean()*100:.1f}%</b> &nbsp;|&nbsp;
        Sentimiento: <b>{df_busq['vader_compound'].mean():.2f}</b>
    </div>""", unsafe_allow_html=True)

    muestra = df_busq[['Score','Summary','Text','word_count','vader_compound','es_util']].head(100)
    muestra.columns = ['Score','Resumen','Texto','Palabras','Sentimiento','Es Util']
    st.dataframe(muestra, use_container_width=True, height=380)
    st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
# TAB 4: Prediccion individual + Subir CSV
# ════════════════════════════════════════════════════════════════════
with tab4:
    seccion = st.radio(
        "Modo de prediccion", options=["Resena individual", "Subir CSV"],
        horizontal=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Prediccion individual ──
    if seccion == "Resena individual":
        st.markdown('<div class="chart-card"><div class="chart-title">Prediccion de Utilidad para Nueva Resena</div>', unsafe_allow_html=True)
        st.markdown("Ingresa el texto de una resena. El modelo calcula las features automaticamente y predice si sera util o no.")

        col_inp1, col_inp2 = st.columns([2, 1])
        with col_inp1:
            resena_texto   = st.text_area("Texto de la resena", placeholder="Escribe aqui el cuerpo de la resena...", height=160)
            resena_summary = st.text_input("Resumen (Summary)", placeholder="Ej: Great product, would buy again")
        with col_inp2:
            score_input       = st.slider("Calificacion (Score)", min_value=1, max_value=5, value=4)
            helpfulness_ratio = st.number_input("Ratio de utilidad previo", min_value=0.0, max_value=1.0,
                                                value=0.5, step=0.01,
                                                help="Votos utiles / votos totales. Usa 0.5 si no se conoce.")

        if st.button("Predecir utilidad", type="primary"):
            if not resena_texto.strip():
                st.warning("Ingresa el texto de la resena para continuar.")
            else:
                sid            = SentimentIntensityAnalyzer()
                vader_compound = sid.polarity_scores(resena_texto)['compound']
                word_count     = len(resena_texto.split())
                sentence_count = max(1, resena_texto.count('.') + resena_texto.count('!') + resena_texto.count('?'))
                summary_wc     = len(resena_summary.split()) if resena_summary.strip() else 0
                coherencia     = 1 if (score_input >= 4 and vader_compound > 0) or \
                                      (score_input <= 2 and vader_compound < 0) else 0

                payload = {
                    "word_count": float(word_count), "sentence_count": float(sentence_count),
                    "summary_word_count": float(summary_wc), "vader_compound": float(vader_compound),
                    "coherencia_sentimiento": int(coherencia), "Score": int(score_input),
                    "helpfulness_ratio": float(helpfulness_ratio)
                }
                try:
                    resp      = requests.post(f"{API_URL}/predecir", json=payload, timeout=5)
                    resp.raise_for_status()
                    resultado = resp.json()
                    es_util   = resultado["es_util"]
                    etiqueta  = resultado["etiqueta"]
                    prob      = resultado["probabilidad_util"]

                    st.markdown("<hr>", unsafe_allow_html=True)
                    r1, r2, r3, r4 = st.columns(4)
                    r1.metric("Prediccion", etiqueta)
                    r2.metric("Probabilidad util", f"{prob*100:.1f}%")
                    r3.metric("Sentimiento VADER", f"{vader_compound:.3f}")
                    r4.metric("Coherencia", "Si" if coherencia else "No")

                    css_class = "pred-util" if es_util == 1 else "pred-no-util"
                    st.markdown(f"""<div class="{css_class}">
                        <b>{etiqueta}</b> — Palabras: {word_count} | Oraciones: {sentence_count} |
                        Summary words: {summary_wc} | VADER: {vader_compound:.3f}
                    </div>""", unsafe_allow_html=True)
                    st.markdown(f"**Confianza del modelo:** {prob*100:.1f}%")
                    st.progress(prob)

                except requests.exceptions.ConnectionError:
                    st.error("API no disponible. Ejecuta: `uvicorn api_app:app --reload --port 8000`")
                except Exception as e:
                    st.error(f"Error al llamar la API: {e}")

        st.markdown('</div>', unsafe_allow_html=True)

    # ── Subir CSV ──
    else:
        st.markdown('<div class="chart-card"><div class="chart-title">Prediccion por Lote — Subir CSV</div>', unsafe_allow_html=True)
        st.markdown("Sube un CSV con resenas. El sistema calcula las features y predice la utilidad de cada fila.")

        with st.expander("Formato requerido del CSV"):
            st.markdown("Columnas minimas requeridas:")
            st.dataframe(pd.DataFrame({
                "ProductId": ["B001E4KFG0", "B00813GRG4"], "Score": [5, 3],
                "Summary": ["Love it!", "Just OK"],
                "Text": ["This product is absolutely amazing...", "Nothing special..."],
                "helpfulness_ratio": [0.8, 0.5]
            }), use_container_width=True)

        archivo_csv = st.file_uploader("Selecciona tu archivo CSV", type=["csv"])

        if archivo_csv is not None:
            df_nuevo = pd.read_csv(archivo_csv)
            st.success(f"Archivo cargado: **{len(df_nuevo)} filas** · {len(df_nuevo.columns)} columnas")

            faltantes = [c for c in ["ProductId", "Score", "Text"] if c not in df_nuevo.columns]
            if faltantes:
                st.error(f"Faltan columnas: `{'`, `'.join(faltantes)}`")
            else:
                st.dataframe(df_nuevo.head(5), use_container_width=True)

                if st.button("Enviar a la API y predecir", type="primary"):
                    sid        = SentimentIntensityAnalyzer()
                    resultados = []
                    errores    = 0
                    barra      = st.progress(0, text="Procesando resenas...")

                    for i, row in df_nuevo.iterrows():
                        texto   = str(row.get("Text", ""))
                        summary = str(row.get("Summary", ""))
                        wc      = len(texto.split())
                        sc      = max(1, texto.count('.') + texto.count('!') + texto.count('?'))
                        swc     = len(summary.split()) if summary.strip() else 0
                        vc      = sid.polarity_scores(texto)['compound']
                        sc_val  = int(row.get("Score", 3))
                        coh     = 1 if (sc_val >= 4 and vc > 0) or (sc_val <= 2 and vc < 0) else 0
                        hr      = float(row.get("helpfulness_ratio", 0.5))

                        try:
                            r = requests.post(f"{API_URL}/predecir", timeout=5, json={
                                "word_count": float(wc), "sentence_count": float(sc),
                                "summary_word_count": float(swc), "vader_compound": float(vc),
                                "coherencia_sentimiento": coh, "Score": sc_val, "helpfulness_ratio": hr
                            })
                            r.raise_for_status()
                            res = r.json()
                            resultados.append({
                                "ProductId": row.get("ProductId", ""), "Score": sc_val,
                                "Prediccion": res["etiqueta"], "Prob_Util": res["probabilidad_util"],
                                "VADER": round(vc, 3), "Palabras": wc, "Summary": summary[:60]
                            })
                        except Exception:
                            errores += 1
                            resultados.append({
                                "ProductId": row.get("ProductId", ""), "Score": sc_val,
                                "Prediccion": "Error", "Prob_Util": None,
                                "VADER": round(vc, 3), "Palabras": wc, "Summary": summary[:60]
                            })
                        barra.progress((i + 1) / len(df_nuevo), text=f"Fila {i+1} de {len(df_nuevo)}...")

                    barra.empty()
                    df_result = pd.DataFrame(resultados)

                    st.markdown("<hr>", unsafe_allow_html=True)
                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("Total procesadas", len(df_result))
                    m2.metric("Utiles", (df_result["Prediccion"] == "Util").sum())
                    m3.metric("No utiles", (df_result["Prediccion"] == "No util").sum())
                    m4.metric("Errores API", errores)

                    st.dataframe(df_result, use_container_width=True, height=320)

                    df_ok = df_result[df_result["Prediccion"] != "Error"]
                    if not df_ok.empty:
                        resumen_prod = (df_ok.groupby("ProductId")
                                       .agg(Resenas=("Prediccion","count"), Pct_Util=("Prob_Util","mean"))
                                       .reset_index())
                        fig_csv = px.bar(resumen_prod, x="ProductId", y="Pct_Util",
                                         color="Pct_Util", color_continuous_scale=COLOR_SCALE,
                                         text=resumen_prod["Pct_Util"].map(lambda x: f"{x*100:.1f}%"),
                                         title="Probabilidad promedio de utilidad por producto")
                        fig_csv.update_traces(textposition='outside')
                        fig_csv.update_layout(**plotly_layout_base())
                        st.plotly_chart(fig_csv, use_container_width=True)

                    st.download_button("Descargar resultados CSV",
                                       data=df_result.to_csv(index=False).encode("utf-8"),
                                       file_name="predicciones_reviewsense.csv", mime="text/csv")
                    if errores:
                        st.warning(f"{errores} fila(s) fallaron. Verifica que la API este activa.")

        st.markdown('</div>', unsafe_allow_html=True)