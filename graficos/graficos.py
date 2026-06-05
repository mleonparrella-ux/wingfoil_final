# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:41:10 2026

@author: usuario
"""
# MANU
import matplotlib.pyplot as plt

def grafico_viento(df):

    plt.scatter(
        df["Vel. Viento (kn)"],
        df["Sensación"]
    )

    plt.xlabel("Viento")
    plt.ylabel("Sensación")

    plt.title("Viento vs Sensación")

    plt.show()


def grafico_wings(df):

    datos = df["Wing"].value_counts()

    plt.bar(
        datos.index,
        datos.values
    )

    plt.title("Uso de Wings")

    plt.show()



# FREY 

import matplotlib.pyplot as plt
import os

def crear_carpeta_graficos():
    """Crea la carpeta graficos/ si no existe."""
    if not os.path.exists("graficos"):
        os.mkdir("graficos")

def grafico_viento(df):
    """
    Genera un gráfico de dispersión entre velocidad del viento y sensación.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    crear_carpeta_graficos()
    plt.figure(figsize=(9, 5))
    plt.scatter(df["Vel. Viento (kn)"], df["Sensación"], color="#b45309", alpha=0.7)
    plt.xlabel("Viento (nudos)", fontsize=11)
    plt.ylabel("Sensación", fontsize=11)
    plt.title("Viento vs Sensación", fontsize=13, fontweight="bold")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()
    print("Gráfico guardado: graficos/viento_vs_sensacion.png")


def grafico_wings(df):
    """
    Genera un gráfico de barras con la cantidad de sesiones por wing.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    crear_carpeta_graficos()
    datos = df["Wing"].value_counts()
    plt.figure(figsize=(9, 5))
    plt.bar(datos.index, datos.values, color="#1e3a8a", edgecolor="black", alpha=0.8)
    plt.title("Uso de Wings", fontsize=13, fontweight="bold")
    plt.xlabel("Wing", fontsize=11)
    plt.ylabel("Cantidad de sesiones", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.show()
    print("Gráfico guardado: graficos/uso_wings.png")
