# Resumen del Caso — Amazon Fine Food Reviews

## Descripción
Amazon cuenta con millones de reseñas de productos alimenticios escritas
por usuarios reales entre 1999 y 2012. El objetivo es extraer insights
accionables sobre qué factores determinan la satisfacción del cliente
y construir un modelo que clasifique automáticamente el sentimiento.

## Contexto del dominio
Amazon opera el marketplace de alimentos más grande del mundo.
Los category managers toman decisiones de listing/deslisting basándose
en ratings. Una reseña negativa viral puede hundir un producto.
Las reseñas "útiles" tienen mayor peso en el algoritmo de visibilidad.

## Fuentes externas
1. Stanford SNAP Dataset - https://snap.stanford.edu/data/web-FineFoods.html
2. Pang & Lee (2008) - Opinion Mining and Sentiment Analysis
3. Amazon Seller Central - Políticas de reseñas 2024

## Pregunta de negocio principal
¿Qué características del texto y del usuario predicen si una reseña
será positiva (≥4 estrellas) o negativa (≤2 estrellas)?

## Preguntas secundarias
1. ¿Los productos con más reseñas tienen mejor o peor rating promedio?
2. ¿Las reseñas más largas tienden a ser más útiles?
3. ¿Hay patrones temporales en la cantidad o calidad de reseñas?

## Métrica de éxito
F1-Score ≥ 0.80 en clasificación positivo/negativo

## Diccionario de variables
| Variable | Tipo | Descripción | % Nulos |
|----------|------|-------------|---------|
| Id | int | Identificador único | 0% |
| ProductId | str | ID del producto | 0% |
| UserId | str | ID del usuario | 0% |
| ProfileName | str | Nombre del perfil | ~0.1% |
| HelpfulnessNumerator | int | Votos útiles recibidos | 0% |
| HelpfulnessDenominator | int | Total votos recibidos | 0% |
| Score | int | Rating 1-5 estrellas | 0% |
| Time | int | Unix timestamp | 0% |
| Summary | str | Resumen corto | ~0% |
| Text | str | Texto completo reseña | ~0% |

## Hipótesis iniciales
1. Las reseñas con Score=1 contienen palabras negativas con mayor frecuencia.
2. Usuarios con más de 50 reseñas tienen ratings más extremos.
3. Reseñas con más votos útiles son en promedio más largas.
4. El volumen de reseñas aumentó significativamente después de 2008.
5. Productos con más de 100 reseñas tienen Score promedio más cercano a 4.0.
