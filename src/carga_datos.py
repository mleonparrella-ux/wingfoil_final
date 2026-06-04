# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:39:35 2026

@author: usuario
"""

import pandas as pd

def cargar_sesiones():
    try:
        sesiones = pd.read_excel(
            "datos/dataset_sesiones.xlsx",
            sheet_name="Sesiones"
        )

        resumen = pd.read_excel(
            "datos/dataset_sesiones.xlsx",
            sheet_name="Resumen por Ubicación"
        )

        return sesiones, resumen

    except Exception as e:
        print("Error al cargar datos:", e)
        return None, None


def unir_datos(sesiones, resumen):

    df = pd.merge(
        sesiones,
        resumen,
        on="Ubicación",
        how="left"
    )

    return df