# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:41:10 2026

@author: usuario
"""

import matplotlib.pyplot as plt


def grafico_wing(df):

    datos = (
        df.groupby("Wing")["Sensación"]
        .mean()
    )

    datos.plot(kind="bar")

    plt.title(
        "Sensación promedio por Wing"
    )

    plt.ylabel("Sensación")

    plt.show()


def grafico_viento_vs_sensacion(df):

    plt.scatter(
        df["Vel. Viento (kn)"],
        df["Sensación"]
    )

    plt.xlabel("Viento")

    plt.ylabel("Sensación")

    plt.title(
        "Viento vs Sensación"
    )

    plt.show()


def grafico_sesiones_por_ubicacion(df):

    datos = (
        df["Ubicación"]
        .value_counts()
    )

    datos.plot(kind="bar")

    plt.title(
        "Sesiones por ubicación"
    )

    plt.ylabel("Cantidad")

    plt.show()