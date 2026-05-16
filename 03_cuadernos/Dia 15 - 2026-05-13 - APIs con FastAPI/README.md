[← Día 14](../Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/) · [🏠 Índice](../README.md) · [Día 16 →](../Dia%2016%20-%202026-05-14%20-%20Buenas%20pr%C3%A1cticas%20y%20portafolio/)

<a href="https://colab.research.google.com/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/clase_15.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/we-human-centric/CursoPythonDatos_2026/blob/main/Dia%2015%20-%202026-05-13%20-%20APIs%20con%20FastAPI/clase_15.ipynb)

---

# Día 15 · APIs con FastAPI

**Fecha:** Miércoles 13 de mayo de 2026  
**Módulo:** Módulo 4 · Ciencia de datos aplicada y escalabilidad  
**Duración:** 2 horas 30 minutos sincrónicas  

---

## Introducción

Un dashboard es una forma de consumir tu modelo; una API es la otra. FastAPI es rápido de escribir, rápido al correr y tiene documentación automática. Hoy exponemos el modelo como un servicio REST que cualquier cliente puede consumir.

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Crear una API REST con FastAPI.
- Definir modelos de request/response con Pydantic.
- Cargar el modelo entrenado y servir predicciones.

## Contenidos de la sesión

### 1. Instalación y corrida

`pip install fastapi uvicorn[standard]`. Ejecutar con `uvicorn api.main:app --reload`.

### 2. Primer endpoint

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### 3. Path vs. query parameters

Path: `/items/{id}`. Query: `/items?limit=10`. FastAPI los distingue por la firma de la función.

### 4. Pydantic

Modelos para validar entrada y salida:
```python
from pydantic import BaseModel
class Features(BaseModel):
    edad: int
    ingreso: float
```

### 5. Cargar el modelo

En el evento de startup, cargar con `joblib.load` y guardarlo en estado de la app o variable global. Evita recargar por request.

### 6. Códigos de estado y errores

`HTTPException(status_code=400, detail="mensaje")`. `status_code=201` para creación, `422` para validación fallida (automático con Pydantic).

### 7. Documentación automática

Swagger UI en `/docs`, ReDoc en `/redoc`. Generadas a partir de los tipos.

### 8. Pruebas

Desde Swagger, con `httpx`/`requests`, o automatizadas con `TestClient` de FastAPI.

## Actividad práctica

Crea `api/main.py` con dos endpoints:

- `GET /health` → devuelve `{"status": "ok"}`.
- `POST /predict` → recibe features (Pydantic) y devuelve predicción + probabilidad.

Prueba desde Swagger UI.

## Trabajo en grupo sobre el caso asignado

Estructuren la API del caso con al menos 2 endpoints. Al menos uno debe conectar con el modelo real del grupo. Documenten ejemplos de uso en el README.

## Entregable del día

`api/main.py` funcional con documentación Swagger en `/docs`.

## Recursos recomendados

- FastAPI – Tutorial: https://fastapi.tiangolo.com/tutorial/
- Pydantic Docs: https://docs.pydantic.dev/

---

---

[← Día 14](../Dia%2014%20-%202026-05-12%20-%20Dashboards%20con%20Streamlit/) · [🏠 Índice](../README.md) · [Día 16 →](../Dia%2016%20-%202026-05-14%20-%20Buenas%20pr%C3%A1cticas%20y%20portafolio/)

> *Seminario EDA · Abril–Mayo 2026 · [we-human-centric](https://github.com/we-human-centric)*
