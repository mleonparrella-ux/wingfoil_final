

from src.carga_datos import cargar_datos
from graficos.graficos import grafico_wings
from graficos.graficos import grafico_viento

df = cargar_datos()

print("\n====================")
print(" DASHBOARD WINGFOIL ")
print("====================")

print("\nRESUMEN GENERAL")

print("Total sesiones:", len(df))

print(
    "Viento promedio:",
    round(df["Vel. Viento (kn)"].mean(),2)
)

print(
    "Sensación promedio:",
    round(df["Sensación"].mean(),2)
)

print(
    "Cantidad de wings:",
    df["Wing"].nunique()
)

while True:

    print("\n--- DASHBOARD ---")

    print("1 - Uso de Wings")
    print("2 - Viento")
    print("0 - Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":

        grafico_wings(df)

    elif opcion == "2":

        grafico_viento(df)

    elif opcion == "0":

        break

    else:

        print("Opción inválida")