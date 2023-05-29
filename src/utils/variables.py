# Importamos las librerías necesarias
import pandas as pd
import numpy as np

# Importamos las funciones
from funciones import *

# Nombramos a las variables

# Insertamos una columna en cada DataFrame con un nombre y su acrónimo
tesla = insertar_columna_acronimo(tesla, "Tesla", "TSLA", 1)
apple = insertar_columna_acronimo(apple, "Apple", "AAPL", 1)
microsoft = insertar_columna_acronimo(microsoft, "Microsoft", "MSFT", 1)
nasdaq = insertar_columna_acronimo(nasdaq, "Nasdaq", "NASDAQ", 1)
oro = insertar_columna_acronimo(oro, "Oro", "XAU/USD", 1)
bitcoin = insertar_columna_acronimo(bitcoin, "Bitcoin", "BTC", 1)


# Aplicamos la función a cada DataFrame
tesla = rename_columns(tesla)
apple = rename_columns(apple)
microsoft = rename_columns(microsoft)
nasdaq = rename_columns(nasdaq)
oro = rename_columns(oro)
bitcoin = rename_columns(bitcoin)

# Aplicamos la función a cada DataFrame
tesla = eliminar_columna_volumen(tesla)
apple = eliminar_columna_volumen(apple)
microsoft = eliminar_columna_volumen(microsoft)
nasdaq = eliminar_columna_volumen(nasdaq)
oro = eliminar_columna_volumen(oro)
bitcoin = eliminar_columna_volumen(bitcoin)

# Eliminamos el símbolo "%" en cada DataFrame
tesla = eliminar_simbolo_porcentaje(tesla, "Var.%")
apple = eliminar_simbolo_porcentaje(apple, "Var.%")
microsoft = eliminar_simbolo_porcentaje(microsoft, "Var.%")
nasdaq = eliminar_simbolo_porcentaje(nasdaq, "Var.%")
oro = eliminar_simbolo_porcentaje(oro, "Var.%")
bitcoin = eliminar_simbolo_porcentaje(bitcoin, "Var.%")

columnas_numericas = ["Cierre", "Apertura", "Máximo", "Mínimo", "Var.%"]

# Limpiamos y convertimos las columnas numéricas que queremos de la lista en cada DataFrame
tesla = limpiar_convertir_columnas_numericas(tesla, columnas_numericas)
apple = limpiar_convertir_columnas_numericas(apple, columnas_numericas)
microsoft = limpiar_convertir_columnas_numericas(microsoft, columnas_numericas)
nasdaq = limpiar_convertir_columnas_numericas(nasdaq, columnas_numericas)
oro = limpiar_convertir_columnas_numericas(oro, columnas_numericas)
bitcoin = limpiar_convertir_columnas_numericas(bitcoin, columnas_numericas)

# Aplicamos la función a cada DataFrame
tesla = cambiar_tipo_fecha(tesla)
apple = cambiar_tipo_fecha(apple)
microsoft = cambiar_tipo_fecha(microsoft)
nasdaq = cambiar_tipo_fecha(nasdaq)
oro = cambiar_tipo_fecha(oro)
bitcoin = cambiar_tipo_fecha(bitcoin)

# Aplicar la función a cada DataFrame
tesla = invertir_orden_filas(tesla)
apple = invertir_orden_filas(apple)
microsoft = invertir_orden_filas(microsoft)
nasdaq = invertir_orden_filas(nasdaq)
oro = invertir_orden_filas(oro)
bitcoin = invertir_orden_filas(bitcoin)

dataframes = [tesla, apple, microsoft, nasdaq, oro, bitcoin]
sufijos = ["Tesla", "Apple", "Microsoft", "Nasdaq", "Oro", "Bitcoin"]

# Unimos los DataFrames con sufijos usando la unión interna
all_data = unir_dataframes(dataframes, sufijos)

