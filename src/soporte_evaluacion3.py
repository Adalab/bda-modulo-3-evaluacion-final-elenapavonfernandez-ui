import pandas as pd
import numpy as np

def eda(dataframe):
    """
    Función para hacer un análisis exploratorio rápido de un DataFrame.
    
    Devuelve:
    - shape
    - info
    - estadísticas descriptivas transpuestas
    - % de valores nulos por columna
    - número de duplicados totales
    """
    
    print("🔹 SHAPE:")
    print(dataframe.shape)
    print("\n🔹 INFO:")
    print(dataframe.info())
    print("\n🔹 DESCRIBE:")
    print(dataframe.describe().T)
    
    # Porcentaje de nulos
    print("\n🔹 % NULOS POR COLUMNA:")
    nulos_pct = (dataframe.isna().sum() / dataframe.shape[0] * 100).round(2)
    print(nulos_pct)
    
    # Duplicados
    print("\n🔹 DUPLICADOS TOTALES:")
    print(dataframe.duplicated().sum())
    
    return dataframe.shape, dataframe.info(), dataframe.describe().T, nulos_pct, dataframe.duplicated().sum()