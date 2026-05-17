import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración
st.set_page_config(
    page_title="ReviewSense — Amazon Fine Food",
    page_icon="🛒",
    layout="wide"
)

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_parquet("data/processed/reviews_limpias.parquet")

df = cargar_datos()

# Sidebar
st.sidebar.title("🔍 Filtros")

anios = sorted(df['Year'].dropna().unique().tolist())
slider_anios = st.sidebar.slider(
    "Rango de años",
    min_value=int(min(anios)),
    max_value=int(max(anios)),
    value=(int(min(anios)), int(max(anios)))
)

scores = st.sidebar.multiselect(
    "Calificación (Score)",
    options=[1, 2, 3, 4, 5],
    default=[1, 2, 3, 4, 5]
)

utilidad = st.sidebar.radio(
    "Utilidad de reseña",
    options=["Todas", "Útiles", "No útiles"]
)

# Filtros
df_f = df[
    (df['Year'] >= slider_anios[0]) &
    (df['Year'] <= slider_anios[1]) &
    (df['Score'].isin(scores))
]

if utilidad == "Útiles":
    df_f = df_f[df_f['es_util'] == 1]
elif utilidad == "No útiles":
    df_f = df_f[df_f['es_util'] == 0]

# Header
st.title("🛒 ReviewSense — Análisis de Reseñas Amazon")
st.markdown("**Grupo 6 | Jose Arevalo · Monica Cholango · Byron Torres**")
st.markdown("---")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reseñas", f"{len(df_f):,}")
col2.metric("Score Promedio", f"{df_f['Score'].mean():.2f} ⭐")
col3.metric("% Reseñas Útiles", f"{df_f['es_util'].mean()*100:.1f}%")
col4.metric("Sentimiento Promedio", f"{df_f['vader_compound'].mean():.2f}")

st.markdown("---")

# Fila 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribución de Calificaciones")
    fig = px.histogram(df_f, x='Score', color='Score',
                       color_discrete_sequence=px.colors.sequential.Blues)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("✅ Reseñas Útiles vs No Útiles")
    util_count = df_f['es_util'].value_counts().reset_index()
    util_count.columns = ['es_util', 'count']
    util_count['label'] = util_count['es_util'].map({1: 'Útil', 0: 'No útil'})
    fig2 = px.pie(util_count, values='count', names='label',
                  color_discrete_sequence=['#2ecc71', '#e74c3c'])
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Fila 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Volumen de Reseñas por Año")
    vol = df_f.groupby('Year').size().reset_index(name='count')
    fig3 = px.line(vol, x='Year', y='count', markers=True,
                   color_discrete_sequence=['#3498db'])
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("😊 Sentimiento VADER por Score")
    vader_score = df_f.groupby('Score')['vader_compound'].mean().reset_index()
    fig4 = px.bar(vader_score, x='Score', y='vader_compound',
                  color='vader_compound', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Fila 3
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Longitud de Reseña vs Utilidad")
    fig5 = px.box(df_f[df_f['word_count'] < 500],
                  x='es_util', y='word_count', color='es_util',
                  color_discrete_map={0: '#e74c3c', 1: '#2ecc71'})
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    st.subheader("🔥 Score Promedio por Año")
    score_anio = df_f.groupby('Year')['Score'].mean().reset_index()
    fig6 = px.line(score_anio, x='Year', y='Score', markers=True,
                   color_discrete_sequence=['#9b59b6'])
    fig6.add_hline(y=df_f['Score'].mean(), line_dash='dash',
                   line_color='red', annotation_text="Promedio global")
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# Tabla
st.subheader("🔎 Explorador de Reseñas")
muestra = df_f[['Score', 'Summary', 'Text', 'word_count',
                'vader_compound', 'es_util']].head(50)
st.dataframe(muestra, use_container_width=True)