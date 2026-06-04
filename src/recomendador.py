# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:40:20 2026

@author: usuario
"""

def sesiones_similares(df, viento):

    similares = df[
        abs(df["Vel. Viento (kn)"] - viento) <= 3
    ]

    return similares


def recomendar_wing(df, viento):

    similares = sesiones_similares(df, viento)

    if len(similares) == 0:
        print("No hay sesiones similares")
        return

    wing = similares["Wing"].mode()[0]

    print("\nWing recomendado:")
    print(wing)

    print(
        "Sensación promedio:",
        round(similares["Sensación"].mean(),2)
    )