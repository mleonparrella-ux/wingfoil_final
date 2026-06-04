# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:39:05 2026

@author: usuario
"""

from src.carga_datos import cargar_sesiones, unir_datos
from src.recomendador import recomendar_equipo
from src.metricas import mostrar_estadisticas
from graficos.graficos import grafico_wing, grafico_sesiones_por_ubicacion, grafico_viento_vs_sensacion
from src.comparador import comparar_sesiones

sesiones, resumen = cargar_sesiones()

df = unir_datos(
    sesiones,
    resumen
)

while True:

    print("\n--- WINGFOIL APP ---")

    print("1. Estadísticas")
    print("2. Recomendar equipo")
    print("3. Comparar sesiones")
    print("4. Gráfico Wing")
    print("5. Viento vs Sensación")
    print("6. Sesiones por ubicación")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        mostrar_estadisticas(df)

    elif opcion == "2":

        ubicacion = input("Ubicación: ")

        viento = float(
            input("Viento: ")
        )

        direccion = input(
            "Dirección: "
        )

        recomendar_equipo(
            df,
            ubicacion,
            viento,
            direccion
        )

    elif opcion == "3":

        id1 = int(input("ID sesión 1: "))
        id2 = int(input("ID sesión 2: "))

        comparar_sesiones(
            df,
            id1,
            id2
        )

    elif opcion == "4":

        grafico_wing(df)

    elif opcion == "5":

        grafico_viento_vs_sensacion(df)

    elif opcion == "6":

        grafico_sesiones_por_ubicacion(df)

    elif opcion == "0":

        break

    else:

        print("Opción inválida")