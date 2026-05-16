# Plan de Preparación de Datos

## Pasos en orden

### 1. Carga y auditoría inicial
Cargar Reviews.csv y revisar shape, dtypes, nulos y duplicados.

### 2. Eliminar duplicados
- Por Id (duplicados exactos)
- Por UserId + Text (reseñas spam copiadas)

### 3. Manejo de nulos
- ProfileName nulo → rellenar con "Anonimo"
- Text o Summary nulo → eliminar fila (sin texto no hay NLP)

### 4. Conversión de tipos
- Time (unix) → datetime con pd.to_datetime(unit='s')
- Extraer: Year, Month, DayOfWeek

### 5. Filtrar inconsistencias
- HelpfulnessNumerator > HelpfulnessDenominator → eliminar
- Score fuera de rango 1-5 → eliminar

### 6. Feature engineering
- text_length: longitud del texto
- summary_length: longitud del resumen
- helpfulness_ratio: votos útiles / total votos
- sentiment_label: 1 si Score>=4, 0 si Score<=2, NaN si Score==3

### 7. Variables descartadas
- ProfileName: no aporta al modelo predictivo
- Id: solo índice, no informativo

### 8. Exportar
- Guardar en 01_datos_procesados/reviews_limpias.parquet
