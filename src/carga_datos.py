# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:39:35 2026

@author: usuario
"""

import pandas as pd

def cargar_datos():

    try:
        df = pd.read_excel("datos/dataset_sesiones.xlsx")
        return df

    except Exception as e:
        print("Error al cargar el archivo")
        print(e)
        return None