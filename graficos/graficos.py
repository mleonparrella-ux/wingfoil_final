# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:41:10 2026

@author: usuario
"""

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