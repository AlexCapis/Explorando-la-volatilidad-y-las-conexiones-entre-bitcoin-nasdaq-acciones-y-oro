# Importamos las librerías necesarias
import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import nbformat

# Importamos las variables que vamos a utilizar
from variables import *


# Agrupamos la limpieza de datos en funciones para que sea más sencillo escalar los datos

# Creamos la función insertar_columna_acronimo() para insertar columnas distintas en cada DataFrame
def insertar_columna_acronimo(df, nombre_columna, acronimo, posicion):
    df.insert(posicion, nombre_columna, acronimo)
    return df



# Creamos la función de rename_columns() para renombrar todas las columnas de nuestros DataFrames, ya que todas se llaman igual
def rename_columns(df):
    df = df.rename(columns={"Último": "Cierre", "Vol.": "Volumen.M", "% var.": "Var.%"})
    return df


# eliminamos la columna de Volumen
# Recuerda que es una columna que hemos usado en la función de renombrar para así en un futuro si queremos podemos no eliminar esta columna fácilmente

def eliminar_columna_volumen(df):
    if "Volumen.M" in df.columns:
        del df["Volumen.M"]
    return df


# usamos la función de eliminar_simbolo_porcentaje() para quitar de la columna "Var.%" todos los "%" y así luego poder pasar a float
def eliminar_simbolo_porcentaje(df, columna):
    df[columna] = df[columna].replace("%", "", regex=True)
    return df


# Usamos la función limpiar_convertir_columnas_numericas() para 3 cosas:
    # Limpiamos las columnas cambiando los "." por "" para aquellos valos que tienen miles y decimales
    # Limpiamos las columnas y cambiamos las "," por "." para poder marcar los decimales correctamente y así poder pasar a tipo float
    # Pasamos esas columnas que deseamos a tipo float
def limpiar_convertir_columnas_numericas(df, columnas_numericas):
    df[columnas_numericas] = df[columnas_numericas].apply(lambda x: x.str.replace('.', ''))
    df[columnas_numericas] = df[columnas_numericas].apply(lambda x: x.str.replace(',', '.'))
    df[columnas_numericas] = df[columnas_numericas].astype(float)
    return df


# Cambiamos la columna 'Fecha' de tipo string a tipo datetime usando la funcion cambiar_tipo_fecha()
# Usamos el formato de d-m-y (día-mes-año)
def cambiar_tipo_fecha(df):
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d.%m.%Y')
    return df


# Invertimos el orden de las filas para que el primer valor sea el de la fecha más antigua y el último valor de la fecha más reciente
# Usando iloc[]
def invertir_orden_filas(df):
    df = df.iloc[::-1].reset_index(drop=True)
    return df


# Usamos la función unir_dataframes() con un bucle for i in range(1, len(dataframes)).
    # DataFrames es una lista que tiene los dataframes que quiero unir
    # La función len(dataframes) es para que nos diga la cantidad de dataframes que hay que unir
    # El uso de range(1, len(dataframes)) es para que genere una secuencia de números desde 1 hsta su longitud.
    # Dentro del bucle usamor el método merge() para unir los DataFrames 
    # Es necesario destacar que usamos el DataFrame de tesla en primer lugar para que tome de referencia a través de how="inner" las fechas de referencia para los demás DataFrames, ya que tesla es la que menos filas tiene junto con Nasdaq
    # Añadimos los sufijos a través de una lista debido a que las columnas son comunes
def unir_dataframes(dataframes, sufijos):
    df_merged = dataframes[0]
    for i in range(1, len(dataframes)):
        df_merged = df_merged.merge(dataframes[i], on='Fecha', how='inner', suffixes=('', '_' + sufijos[i]))

    return df_merged


# Realizamos una función para generar cada uno de los gráficos debido a que cada DataFrame tiene las mismas columnas
def generar_grafico_velas(dataframe, titulo):
    fig = go.Figure(data=go.Candlestick(open=dataframe['Apertura'],
                                       high=dataframe['Máximo'],
                                       low=dataframe['Mínimo'],
                                       close=dataframe['Cierre']))

    fig.update_layout(title=titulo,
                      xaxis_title='Fecha',
                      yaxis_title='Precio')

    fig.show()

def generar_grafico_distribucion(dataframe, titulo):
    fig = ff.create_distplot(
        [dataframe['Var.%'].dropna()],
        [titulo],
        bin_size=0.1,
        curve_type='kde',
        show_rug=False,
        histnorm='probability',
        show_curve=False,
        colors=['dodgerblue']
    )
    fig.update_layout(
        template='plotly_dark',
        xaxis_title='Var %',
        yaxis_title='Probabilidad',
        title_text=titulo,
        xaxis=dict(
            range=[-10, 10]  # Establecer el rango del eje X
        )
    )
    fig.show()


def generar_grafico_distribucion_conjunta(dataframes, titulos, colores):
    fig = make_subplots(rows=1, cols=1)

    for dataframe, titulo, color in zip(dataframes, titulos, colores):
        distplfig = ff.create_distplot([dataframe['Var.%'].dropna()], [titulo], bin_size=0.1, curve_type='kde', show_rug=False, colors=[color])
        fig.add_trace(distplfig.data[0], row=1, col=1)

    fig.update_layout(height=800, width=1200, title_text="Comparación de distribuciones", template="plotly_dark")
    fig.update_xaxes(title_text='Var %')
    fig.update_yaxes(title_text='Probabilidad')
    fig.update_xaxes(range=[-25, 25])  
    fig.update_yaxes(range=[0, 1.1])   
    fig.show()

# Primero realizamos la función de add_dias_semana_column() para añadir la columna pertinente a los Dataframes que no la tienen
def add_dias_semana_column(dataframes):
    for df in dataframes:
        # Extraemos la fecha del índice
        df['Fecha'] = df.index

        # Añadimos la columna 'DiasSemana' en la posición deseada en este caso la columna 2 que pertenece al índice 1
        df.insert(1, 'DiasSemana', df['Fecha'].dt.day_name())
