# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:40:34 2026

@author: usuario
"""

def comparar_sesiones(df, id1, id2):

    try:

        s1 = df.iloc[id1]
        s2 = df.iloc[id2]

        print("\n--- Sesión 1 ---")
        print(s1)

        print("\n--- Sesión 2 ---")
        print(s2)

        diferencia = (
            s1["Sensación"]
            - s2["Sensación"]
        )

        print(
            "\nDiferencia de sensación:",
            diferencia
        )

    except:
        print("Índices inválidos")