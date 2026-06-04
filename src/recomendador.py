# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:40:20 2026

@author: usuario
"""

def buscar_similares(df, ubicacion, viento, direccion):

    similares = df[
        (df["Ubicación"] == ubicacion)
        &
        (abs(df["Vel. Viento (kn)"] - viento) <= 3)
        &
        (df["Dir. Viento"] == direccion)
    ]

    return similares


def recomendar_equipo(df, ubicacion, viento, direccion):

    similares = buscar_similares(
        df,
        ubicacion,
        viento,
        direccion
    )

    if len(similares) == 0:

        print("No hay sesiones similares.")
        return

    top3 = similares.nlargest(
        3,
        "Sensación"
    )

    wing = top3["Wing"].mode()[0]
    tabla = top3["Tabla"].mode()[0]
    foil = top3["Foil"].mode()[0]

    print("\nEquipo recomendado")

    print("Wing:", wing)
    print("Tabla:", tabla)
    print("Foil:", foil)

    print(
        "Sensación promedio:",
        round(top3["Sensación"].mean(), 2)
    )