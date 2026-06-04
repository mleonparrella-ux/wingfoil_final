# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:40:51 2026

@author: usuario
"""

def mostrar_estadisticas(df):

    print("\nESTADÍSTICAS")

    print(
        "Total sesiones:",
        len(df)
    )

    print(
        "Duración promedio:",
        round(
            df["Duración (min)"].mean(),
            2
        )
    )

    print(
        "Viento promedio:",
        round(
            df["Vel. Viento (kn)"].mean(),
            2
        )
    )

    mejor_wing = (
        df.groupby("Wing")["Sensación"]
        .mean()
        .idxmax()
    )

    print(
        "Wing con mejor sensación:",
        mejor_wing
    )