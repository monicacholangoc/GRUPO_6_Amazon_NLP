# Datos Crudos

## Fuente
Kaggle - Amazon Fine Food Reviews
https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

## Descarga manual
1. Ir al link de arriba
2. Descargar Reviews.csv
3. Colocarlo en esta carpeta (no se versiona por pesar ~300 MB)

## Descarga con Kaggle CLI
```bash
kaggle datasets download -d snap/amazon-fine-food-reviews
unzip amazon-fine-food-reviews.zip
```

## Archivo principal
- Reviews.csv — 568,454 filas, ~300 MB

## Columnas
Id, ProductId, UserId, ProfileName, HelpfulnessNumerator,
HelpfulnessDenominator, Score, Time, Summary, Text
