import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ReviewSense — Amazon Fine Food",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-header {
        background: linear-gradient(135deg, #232f3e 0%, #37475a 100%);
        padding: 2rem; border-radius: 12px;
        margin-bottom: 1.5rem; text-align: center;
    }
    .main-header h1 { color: #ff9900; font-size: 2.5rem; font-weight: 800; margin: 0; }
    .main-header p { color: #ffffff; font-size: 1rem; margin: 0.5rem 0 0 0; opacity: 0.85; }
    .kpi-card {
        background: white; border-radius: 12px; padding: 1.2rem 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-left: 5px solid #ff9900;
        margin-bottom: 1rem;
    }
    .kpi-label { color: #666; font-size: 0.8rem; font-weight: 600;
        text-transform: uppercase; letter-spacing: 1px; }
    .kpi-value { color: #232f3e; font-size: 2rem; font-weight: 800; line-height: 1.2; }
    .chart-card {
        background: white; border-radius: 12px; padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 1rem;
    }
    .chart-title {
        color: #232f3e; font-size: 1rem; font-weight: 700;
        margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #ff9900;
    }
    [data-testid="stSidebar"] { background-color: #232f3e; }
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] p { color: white !important; }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 { color: #ff9900 !important; }
    .footer { text-align: center; color: #999; font-size: 0.8rem; padding: 2rem 0 1rem 0; }
    hr { border: none; border-top: 1px solid #e9ecef; margin: 1.5rem 0; }
    .info-box {
        background: #fff8ee; border-left: 4px solid #ff9900;
        padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.5rem;
        color: #232f3e; font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# ── Cargar datos ─────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    return pd.read_parquet("data/processed/reviews_limpias.parquet")

df = cargar_datos()
df['Time'] = pd.to_datetime(df['Time'])

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ReviewSense")
    st.markdown("---")
    st.markdown("### Filtros")

    fecha_min = df['Time'].min().date()
    fecha_max = df['Time'].max().date()

    st.markdown("**Rango de fechas**")
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        fecha_inicio = st.date_input(
            "Desde", value=fecha_min,
            min_value=fecha_min, max_value=fecha_max
        )
    with col_f2:
        fecha_fin = st.date_input(
            "Hasta", value=fecha_max,
            min_value=fecha_min, max_value=fecha_max
        )

    st.markdown("---")

    scores = st.multiselect(
        "Calificacion (Score)",
        options=[1, 2, 3, 4, 5],
        default=[1, 2, 3, 4, 5]
    )

    st.markdown("---")

    utilidad = st.radio(
        "Utilidad de resena",
        options=["Todas", "Utiles", "No utiles"]
    )

    st.markdown("---")

    st.markdown("**Longitud de resena (palabras)**")
    max_words = int(df['word_count'].quantile(0.95))
    rango_palabras = st.slider(
        "Rango", min_value=0, max_value=max_words,
        value=(0, max_words)
    )

    st.markdown("---")
    st.markdown("### Acerca de")
    st.markdown("""
    **Grupo 6**  
    Jose Arevalo  
    Monica Cholango  
    Byron Torres  
    """)

# ── Aplicar filtros ───────────────────────────────────────────
df_f = df[
    (df['Time'].dt.date >= fecha_inicio) &
    (df['Time'].dt.date <= fecha_fin) &
    (df['Score'].isin(scores)) &
    (df['word_count'] >= rango_palabras[0]) &
    (df['word_count'] <= rango_palabras[1])
]

if utilidad == "Utiles":
    df_f = df_f[df_f['es_util'] == 1]
elif utilidad == "No utiles":
    df_f = df_f[df_f['es_util'] == 0]

# ── Header ────────────────────────────────────────────────────
st.markdown("""
    <div class="main-header">
        <h1>ReviewSense</h1>
        <p>Analisis Inteligente de Resenas — Amazon Fine Food Reviews</p>
    </div>
""", unsafe_allow_html=True)

# ── KPIs ──────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Total Resenas</div>
        <div class="kpi-value">{len(df_f):,}</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Score Promedio</div>
        <div class="kpi-value">{df_f['Score'].mean():.2f} / 5</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Resenas Utiles</div>
        <div class="kpi-value">{df_f['es_util'].mean()*100:.1f}%</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-label">Sentimiento VADER</div>
        <div class="kpi-value">{df_f['vader_compound'].mean():.2f}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

COLORS = ['#232f3e', '#37475a', '#ff9900', '#febd69', '#f3a847']

# ── Pestanas ──────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Calificaciones",
    "Tendencia Temporal",
    "Sentimiento",
    "Longitud y Utilidad",
    "Explorador"
])

# ── Tab 1: Calificaciones ─────────────────────────────────────
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Distribucion de Calificaciones — Click para ver detalle</div>', unsafe_allow_html=True)

        score_counts = df_f['Score'].value_counts().sort_index().reset_index()
        score_counts.columns = ['Score', 'Cantidad']

        fig = px.bar(
            score_counts, x='Score', y='Cantidad',
            color='Score',
            color_discrete_sequence=COLORS,
            text='Cantidad'
        )
        fig.update_traces(textposition='outside')
        fig.update_layout(
            showlegend=False, plot_bgcolor='white',
            paper_bgcolor='white', margin=dict(t=30, b=10, l=10, r=10),
            xaxis_title="Estrellas", yaxis_title="Cantidad"
        )

        selected = st.plotly_chart(
            fig, use_container_width=True,
            on_select="rerun", key="bar_score"
        )

        if selected and selected.get("selection", {}).get("points"):
            score_sel = int(selected["selection"]["points"][0]["x"])
            df_sel = df_f[df_f['Score'] == score_sel]
            st.markdown(f"""
            <div class="info-box">
                <b>Score {score_sel} seleccionado</b><br>
                Resenas: {len(df_sel):,} &nbsp;|&nbsp;
                Sentimiento promedio: {df_sel['vader_compound'].mean():.2f} &nbsp;|&nbsp;
                Utiles: {df_sel['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
                Palabras promedio: {df_sel['word_count'].mean():.0f}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Resenas Utiles vs No Utiles — Click para ver detalle</div>', unsafe_allow_html=True)

        util_count = df_f['es_util'].value_counts().reset_index()
        util_count.columns = ['es_util', 'count']
        util_count['label'] = util_count['es_util'].map({1: 'Util', 0: 'No util'})

        fig2 = px.pie(
            util_count, values='count', names='label',
            color_discrete_sequence=['#ff9900', '#232f3e'],
            hole=0.4
        )
        fig2.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=10, b=10, l=10, r=10)
        )

        selected2 = st.plotly_chart(
            fig2, use_container_width=True,
            on_select="rerun", key="pie_util"
        )

        if selected2 and selected2.get("selection", {}).get("points"):
            label_sel = selected2["selection"]["points"][0]["label"]
            val_sel = 1 if label_sel == "Util" else 0
            df_sel2 = df_f[df_f['es_util'] == val_sel]
            st.markdown(f"""
            <div class="info-box">
                <b>{label_sel} seleccionado</b><br>
                Resenas: {len(df_sel2):,} &nbsp;|&nbsp;
                Score promedio: {df_sel2['Score'].mean():.2f} &nbsp;|&nbsp;
                Sentimiento: {df_sel2['vader_compound'].mean():.2f} &nbsp;|&nbsp;
                Palabras promedio: {df_sel2['word_count'].mean():.0f}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ── Tab 2: Tendencia Temporal ─────────────────────────────────
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Volumen de Resenas por Ano — Click para ver detalle</div>', unsafe_allow_html=True)

        vol = df_f.groupby('Year').size().reset_index(name='count')
        fig3 = px.area(vol, x='Year', y='count',
                       color_discrete_sequence=['#ff9900'], markers=True)
        fig3.update_traces(fill='tozeroy', fillcolor='rgba(255,153,0,0.15)')
        fig3.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=10, b=10, l=10, r=10),
            xaxis_title="Ano", yaxis_title="Resenas"
        )

        selected3 = st.plotly_chart(
            fig3, use_container_width=True,
            on_select="rerun", key="area_vol"
        )

        if selected3 and selected3.get("selection", {}).get("points"):
            anio_sel = int(selected3["selection"]["points"][0]["x"])
            df_sel3 = df_f[df_f['Year'] == anio_sel]
            st.markdown(f"""
            <div class="info-box">
                <b>Ano {anio_sel}</b><br>
                Resenas: {len(df_sel3):,} &nbsp;|&nbsp;
                Score promedio: {df_sel3['Score'].mean():.2f} &nbsp;|&nbsp;
                Utiles: {df_sel3['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
                Sentimiento: {df_sel3['vader_compound'].mean():.2f}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Score Promedio por Ano</div>', unsafe_allow_html=True)
        score_anio = df_f.groupby('Year')['Score'].mean().reset_index()
        fig6 = px.line(score_anio, x='Year', y='Score',
                       markers=True, color_discrete_sequence=['#232f3e'])
        fig6.add_hline(
            y=df_f['Score'].mean(), line_dash='dash', line_color='#ff9900',
            annotation_text=f"Promedio: {df_f['Score'].mean():.2f}",
            annotation_font_color='#ff9900'
        )
        fig6.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=10, b=10, l=10, r=10),
            xaxis_title="Ano", yaxis_title="Score promedio"
        )
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-card"><div class="chart-title">Resenas por Mes del Ano — Click para ver detalle</div>', unsafe_allow_html=True)
    meses = {1:'Ene',2:'Feb',3:'Mar',4:'Abr',5:'May',6:'Jun',
             7:'Jul',8:'Ago',9:'Sep',10:'Oct',11:'Nov',12:'Dic'}
    vol_mes = df_f.groupby('Month').size().reset_index(name='count')
    vol_mes['mes_nombre'] = vol_mes['Month'].map(meses)
    fig_mes = px.bar(vol_mes, x='mes_nombre', y='count',
                     color_discrete_sequence=['#ff9900'], text='count')
    fig_mes.update_traces(textposition='outside')
    fig_mes.update_layout(
        plot_bgcolor='white', paper_bgcolor='white',
        margin=dict(t=30, b=10, l=10, r=10),
        xaxis_title="Mes", yaxis_title="Resenas"
    )

    selected_mes = st.plotly_chart(
        fig_mes, use_container_width=True,
        on_select="rerun", key="bar_mes"
    )

    if selected_mes and selected_mes.get("selection", {}).get("points"):
        mes_sel_nombre = selected_mes["selection"]["points"][0]["x"]
        mes_num = {v: k for k, v in meses.items()}[mes_sel_nombre]
        df_mes = df_f[df_f['Month'] == mes_num]
        st.markdown(f"""
        <div class="info-box">
            <b>{mes_sel_nombre} seleccionado</b><br>
            Resenas: {len(df_mes):,} &nbsp;|&nbsp;
            Score promedio: {df_mes['Score'].mean():.2f} &nbsp;|&nbsp;
            Utiles: {df_mes['es_util'].mean()*100:.1f}% &nbsp;|&nbsp;
            Sentimiento: {df_mes['vader_compound'].mean():.2f}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Tab 3: Sentimiento ────────────────────────────────────────
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Sentimiento VADER por Score — Click para ver detalle</div>', unsafe_allow_html=True)
        vader_score = df_f.groupby('Score')['vader_compound'].mean().reset_index()
        fig4 = px.bar(
            vader_score, x='Score', y='vader_compound',
            color='vader_compound', text=vader_score['vader_compound'].round(2),
            color_continuous_scale=[[0, '#232f3e'], [0.5, '#febd69'], [1, '#ff9900']]
        )
        fig4.update_traces(textposition='outside')
        fig4.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            xaxis_title="Estrellas", yaxis_title="Sentimiento promedio"
        )

        selected4 = st.plotly_chart(
            fig4, use_container_width=True,
            on_select="rerun", key="bar_vader"
        )

        if selected4 and selected4.get("selection", {}).get("points"):
            score_vader = int(selected4["selection"]["points"][0]["x"])
            df_vader = df_f[df_f['Score'] == score_vader]
            st.markdown(f"""
            <div class="info-box">
                <b>Score {score_vader} — Sentimiento</b><br>
                VADER promedio: {df_vader['vader_compound'].mean():.3f} &nbsp;|&nbsp;
                Resenas positivas VADER: {(df_vader['vader_compound'] > 0).mean()*100:.1f}% &nbsp;|&nbsp;
                Resenas: {len(df_vader):,}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Distribucion de Sentimiento VADER</div>', unsafe_allow_html=True)
        fig_vader = px.histogram(df_f, x='vader_compound', nbins=50,
                                 color_discrete_sequence=['#232f3e'])
        fig_vader.add_vline(x=0, line_dash='dash', line_color='#ff9900',
                            annotation_text="Neutro", annotation_font_color='#ff9900')
        fig_vader.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=10, b=10, l=10, r=10),
            xaxis_title="Score VADER", yaxis_title="Frecuencia"
        )
        st.plotly_chart(fig_vader, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ── Tab 4: Longitud y Utilidad ────────────────────────────────
with tab4:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-card"><div class="chart-title">Longitud de Resena vs Utilidad</div>', unsafe_allow_html=True)
        fig5 = px.box(
            df_f[df_f['word_count'] < 500],
            x='es_util', y='word_count', color='es_util',
            color_discrete_map={0: '#232f3e', 1: '#ff9900'}
        )
        fig5.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=10, b=10, l=10, r=10),
            xaxis_title="0 = No util | 1 = Util",
            yaxis_title="Palabras", showlegend=False
        )
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card"><div class="chart-title">Palabras Promedio por Score — Click para ver detalle</div>', unsafe_allow_html=True)
        words_score = df_f.groupby('Score')['word_count'].mean().reset_index()
        words_score['word_count'] = words_score['word_count'].round(0)
        fig_ws = px.bar(
            words_score, x='Score', y='word_count',
            color_discrete_sequence=['#37475a'],
            text='word_count'
        )
        fig_ws.update_traces(textposition='outside')
        fig_ws.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            xaxis_title="Estrellas", yaxis_title="Palabras promedio"
        )

        selected_ws = st.plotly_chart(
            fig_ws, use_container_width=True,
            on_select="rerun", key="bar_words"
        )

        if selected_ws and selected_ws.get("selection", {}).get("points"):
            score_ws = int(selected_ws["selection"]["points"][0]["x"])
            df_ws = df_f[df_f['Score'] == score_ws]
            st.markdown(f"""
            <div class="info-box">
                <b>Score {score_ws} — Longitud</b><br>
                Palabras promedio: {df_ws['word_count'].mean():.0f} &nbsp;|&nbsp;
                Resenas largas (>200 palabras): {(df_ws['word_count'] > 200).mean()*100:.1f}% &nbsp;|&nbsp;
                Utiles: {df_ws['es_util'].mean()*100:.1f}%
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ── Tab 5: Explorador ─────────────────────────────────────────
with tab5:
    st.markdown('<div class="chart-card"><div class="chart-title">Explorador de Resenas</div>', unsafe_allow_html=True)
    st.markdown("""
    Usa el buscador para encontrar resenas por palabra clave.
    Combina con los filtros del panel izquierdo para refinar resultados.
    """)

    col_b1, col_b2, col_b3 = st.columns([3, 1, 1])
    with col_b1:
        busqueda = st.text_input(
            "Buscar en el texto de las resenas",
            placeholder="Ej: delicious, terrible, packaging..."
        )
    with col_b2:
        score_filtro = st.selectbox(
            "Score", options=["Todos", 1, 2, 3, 4, 5]
        )
    with col_b3:
        util_filtro = st.selectbox(
            "Utilidad", options=["Todos", "Util", "No util"]
        )

    df_busq = df_f.copy()

    if busqueda:
        df_busq = df_busq[df_busq['Text'].str.contains(busqueda, case=False, na=False)]

    if score_filtro != "Todos":
        df_busq = df_busq[df_busq['Score'] == score_filtro]

    if util_filtro == "Util":
        df_busq = df_busq[df_busq['es_util'] == 1]
    elif util_filtro == "No util":
        df_busq = df_busq[df_busq['es_util'] == 0]

    st.markdown(f"""
    <div class="info-box">
        Se encontraron <b>{len(df_busq):,}</b> resenas &nbsp;|&nbsp;
        Score promedio: <b>{df_busq['Score'].mean():.2f}</b> &nbsp;|&nbsp;
        Utiles: <b>{df_busq['es_util'].mean()*100:.1f}%</b> &nbsp;|&nbsp;
        Sentimiento: <b>{df_busq['vader_compound'].mean():.2f}</b>
    </div>
    """, unsafe_allow_html=True)

    muestra = df_busq[['Score', 'Summary', 'Text', 'word_count',
                        'vader_compound', 'es_util']].head(100)
    muestra.columns = ['Score', 'Resumen', 'Texto', 'Palabras', 'Sentimiento', 'Es Util']
    st.dataframe(muestra, use_container_width=True, height=400)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
""", unsafe_allow_html=True)