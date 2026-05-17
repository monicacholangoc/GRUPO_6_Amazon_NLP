# api_app.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle, os

app = FastAPI(title="ReviewSense API", version="1.0")

BASE = os.path.dirname(os.path.abspath(__file__))
MODELO_PATH = os.path.join(BASE, "models", "modelo_rf.pkl")

with open(MODELO_PATH, "rb") as f:
    modelo = pickle.load(f)

class ResenaInput(BaseModel):
    word_count: float
    sentence_count: float
    summary_word_count: float
    vader_compound: float
    coherencia_sentimiento: int
    Score: int
    helpfulness_ratio: float

class PrediccionOutput(BaseModel):
    es_util: int
    etiqueta: str
    probabilidad_util: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predecir", response_model=PrediccionOutput)
def predecir(datos: ResenaInput):
    X = [[
        datos.word_count, datos.sentence_count, datos.summary_word_count,
        datos.vader_compound, datos.coherencia_sentimiento,
        datos.Score, datos.helpfulness_ratio
    ]]
    pred  = int(modelo.predict(X)[0])
    proba = float(modelo.predict_proba(X)[0][1])
    return PrediccionOutput(
        es_util=pred,
        etiqueta="Útil" if pred == 1 else "No útil",
        probabilidad_util=round(proba, 3)
    )