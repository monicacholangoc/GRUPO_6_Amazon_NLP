# Datos Procesados

## Archivo principal
reviews_limpias.parquet — 66,982 filas, 20 columnas

## Cómo generarlo
Ejecutar 03_cuadernos/01_preparacion_datos.ipynb en Google Colab.

## Columnas nuevas
- helpfulness_ratio: votos utiles / total votos
- es_util: variable objetivo (1=util, 0=no util)
- word_count: palabras en el texto
- sentence_count: numero de oraciones
- summary_word_count: palabras en el resumen
- vader_compound: score sentimiento VADER
- coherencia_sentimiento: texto coherente con estrellas
- Year, Month, DayOfWeek: extraidas de Time
