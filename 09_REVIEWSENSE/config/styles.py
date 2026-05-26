import streamlit as st

COLORS = ['#232f3e', '#37475a', '#ff9900', '#febd69', '#f3a847']

COLOR_SCALE = [[0, '#232f3e'], [0.5, '#febd69'], [1, '#ff9900']]

COLOR_MAP_UTIL = {0: '#232f3e', 1: '#ff9900'}

AMAZON_NAVY   = '#232f3e'
AMAZON_STEEL  = '#37475a'
AMAZON_ORANGE = '#ff9900'
AMAZON_GOLD   = '#febd69'
AMAZON_AMBER  = '#f3a847'
BG_APP        = '#f8f9fa'
BG_CARD       = '#ffffff'
BG_INFO       = '#fff8ee'


def apply_styles():
    """Aplica todos los estilos CSS globales del dashboard."""
    st.markdown("""
        <style>
        /* ── App base ──────────────────────────────────── */
        .stApp { background-color: #f8f9fa; }

        /* ── Header principal ──────────────────────────── */
        .main-header {
            background: linear-gradient(135deg, #232f3e 0%, #37475a 100%);
            padding: 2rem; border-radius: 12px;
            margin-bottom: 1.5rem; text-align: center;
        }
        .main-header h1 {
            color: #ff9900; font-size: 2.5rem;
            font-weight: 800; margin: 0;
        }
        .main-header p {
            color: #ffffff; font-size: 1rem;
            margin: 0.5rem 0 0 0; opacity: 0.85;
        }

        /* ── Tarjetas KPI ──────────────────────────────── */
        .kpi-card {
            background: white; border-radius: 12px;
            padding: 1.2rem 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07);
            border-left: 5px solid #ff9900;
            margin-bottom: 1rem;
        }
        .kpi-label {
            color: #666; font-size: 0.8rem; font-weight: 600;
            text-transform: uppercase; letter-spacing: 1px;
        }
        .kpi-value {
            color: #232f3e; font-size: 2rem;
            font-weight: 800; line-height: 1.2;
        }

        /* ── Tarjetas de gráfico ───────────────────────── */
        .chart-card {
            background: white; border-radius: 12px; padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.07); margin-bottom: 1rem;
        }
        .chart-title {
            color: #232f3e; font-size: 1rem; font-weight: 700;
            margin-bottom: 1rem; padding-bottom: 0.5rem;
            border-bottom: 2px solid #ff9900;
        }

        /* ── Sidebar ───────────────────────────────────── */
        [data-testid="stSidebar"] { background-color: #232f3e; }
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stRadio label,
        [data-testid="stSidebar"] p { color: white !important; }
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 { color: #ff9900 !important; }

        /* ── Info box interactivo ──────────────────────── */
        .info-box {
            background: #fff8ee; border-left: 4px solid #ff9900;
            padding: 0.8rem 1rem; border-radius: 6px;
            margin-top: 0.5rem; color: #232f3e; font-size: 0.9rem;
        }

        /* ── Badge de producto ─────────────────────────── */
        .product-badge {
            background: #232f3e; color: #ff9900;
            padding: 0.2rem 0.6rem; border-radius: 20px;
            font-size: 0.75rem; font-weight: 700;
            display: inline-block; margin: 0.1rem;
        }

        /* ── Predicción resultado ──────────────────────── */
        .pred-util {
            background: #fff8ee; border-left: 4px solid #ff9900;
            padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.5rem;
            color: #232f3e; font-size: 0.9rem;
        }
        .pred-no-util {
            background: #f0f2f5; border-left: 4px solid #232f3e;
            padding: 0.8rem 1rem; border-radius: 6px; margin-top: 0.5rem;
            color: #232f3e; font-size: 0.9rem;
        }

        /* ── Divisor ───────────────────────────────────── */
        hr { border: none; border-top: 1px solid #e9ecef; margin: 1.5rem 0; }

        /* ── Footer ────────────────────────────────────── */
        .footer {
            text-align: center; color: #999;
            font-size: 0.8rem; padding: 2rem 0 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)


def plotly_layout_base():
    """Retorna el dict base de layout para gráficos Plotly."""
    return dict(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=30, b=10, l=10, r=10)
    )