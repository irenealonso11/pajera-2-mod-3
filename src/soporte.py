import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

df = pd.read_csv("files/ventas.csv", index_col=0)
df2 = pd.read_csv("files/productos.csv", sep=";", index_col=0)
df3 = pd.read_csv("files/clientes.csv", index_col=0)

def explorar_dataframe(df):

    print("Primeras 5 filas del DataFrame:")
    print(df.head(), "\n")

    print("Últimas 5 filas del DataFrame:")
    print(df.tail(), "\n")

    print("Información general del DataFrame:")
    print(df.info(), "\n")
    
    print("Estadísticas descriptivas (solo para columnas numéricas):")
    print(df.describe(), "\n")
    
    print("Valores nulos por columna:")
    print(df.isnull().sum(), "\n")
    
    print("Número de filas y columnas (shape):")
    print(df.shape, "\n")
    
    print("Nombres de las columnas:")
    print(df.columns, "\n")
    
    print("Tipos de datos de cada columna:")
    print(df.dtypes, "\n")

    