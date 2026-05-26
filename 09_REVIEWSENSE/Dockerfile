FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import nltk; nltk.download('vader_lexicon', quiet=True)"

COPY . .

EXPOSE 8000 8501

CMD uvicorn api_app:app --host 0.0.0.0 --port 8000 & \
    streamlit run dashboard_app.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    --server.headless true