[← Día 13](../Dia%2013%20-%202026-05-11%20-%20M%C3%A9tricas%20y%20comparaci%C3%B3n%20de%20modelos%20-%20ENTREGA%20SEMANA%203/) · [🏠 Índice](../README.md) · [Día 15 →](../Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/clase_14.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/clase_14.ipynb)

---

# Día 14 · Dashboards interactivos con Streamlit

**Fecha:** Martes 12 de mayo de 2026  
**Módulo:** Módulo 4 · Ciencia de datos aplicada y escalabilidad  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## 🗓️ Plan de la Semana 4

| Día | Fecha | Tema |
|-----|-------|------|
| 14 | Mar 12 may | Dashboards con Streamlit |
| 15 | Mié 13 may | APIs con FastAPI |
| 16 | Jue 14 may | Buenas prácticas y portafolio |
| **17** | **Vie 15 may** | **Presentaciones finales — ENTREGA FINAL** |

### Entregable de cierre: Semana 4 – Producto de Software Analítico

Al cierre del **Día 17 (viernes 15 de mayo)** cada equipo presenta y entrega:

- Comparación de al menos dos modelos con justificación del seleccionado y métricas finales (Precision, Recall, F1, ROC).
- Dashboard en Streamlit con visualizaciones clave, predicciones e interpretación de hallazgos.
- API en FastAPI con endpoints documentados (Swagger).
- Repositorio GitHub: código modularizado, documentación interna, `README` con instrucciones y `requirements.txt`.

---

## Introducción

Streamlit permite construir interfaces de datos en Python puro. En unas pocas líneas tendrás una app web para presentar tu análisis a usuarios no técnicos y exponer tu modelo en vivo.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Construir una app Streamlit con múltiples páginas.
- Usar widgets para que el usuario explore los datos.
- Integrar tu modelo entrenado para hacer predicciones.

## Contenidos de la sesión

### 1. Cómo corre Streamlit

El script se ejecuta de arriba a abajo cada vez que el usuario interactúa. `st.session_state` para persistir. `@st.cache_data` y `@st.cache_resource` para evitar recomputar.

### 2. Widgets

`st.sidebar`, `st.selectbox`, `st.slider`, `st.multiselect`, `st.text_input`, `st.number_input`, `st.file_uploader`, `st.date_input`.

### 3. Layouts

`st.columns`, `st.tabs`, `st.expander`, `st.container`. Estructura visual del dashboard.

### 4. Gráficos

`st.plotly_chart(fig)`, `st.pyplot(fig)`, `st.altair_chart(...)`. Plotly es la opción más interactiva.

### 5. Predicción en vivo

Cargar el modelo con `joblib.load` dentro de una función con `@st.cache_resource`. Widgets para los features → `model.predict(X)` → mostrar resultado.

### 6. Multi-página

Crear carpeta `pages/` junto a `app.py`. Streamlit detecta cada `.py` como una página.

### 7. Despliegue

Streamlit Community Cloud: gratis, conecta con GitHub y publica con un clic. Alternativa: Docker + servicio cloud.

## Actividad práctica

Plantilla inicial en `app.py` con 3 páginas:

- **Visión general**: KPIs principales del dataset.
- **EDA**: gráficos interactivos con filtros.
- **Predicción**: widgets para ingresar features y ver salida del modelo.

Ejecútalo localmente con `streamlit run app.py`.

## Trabajo en grupo sobre el caso asignado

Inicien el dashboard del caso. Al menos una página debe estar **conectada** al pipeline y al modelo serializado del grupo.

## Entregable del día

`app.py` corriendo localmente + captura del dashboard en el repo.

## Recursos recomendados

- Streamlit Docs: https://docs.streamlit.io/
- Streamlit Community Cloud: https://streamlit.io/cloud

---

---

[← Día 13](../Dia%2013%20-%202026-05-11%20-%20M%C3%A9tricas%20y%20comparaci%C3%B3n%20de%20modelos%20-%20ENTREGA%20SEMANA%203/) · [🏠 Índice](../README.md) · [Día 15 →](../Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
