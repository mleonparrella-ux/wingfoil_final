
import pandas as pd

def cargar_datos():
    """
    Lee el archivo Excel de sesiones y devuelve un DataFrame.

    Retorna:
        DataFrame: sesiones cargadas en un DataFrame de Pandas.
        None: si el archivo no existe.

    Lanza:
        FileNotFoundError: si el archivo no existe en la ruta indicada.
    """
    try:
        df = pd.read_excel("datos/dataset_sesiones.xlsx")
        return df
    except FileNotFoundError:
        print("Error: no se encontró el archivo datos/dataset_sesiones.xlsx")
        return None
