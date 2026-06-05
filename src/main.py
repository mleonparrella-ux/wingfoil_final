from src.carga_datos import cargar_datos
from src.recomendador import recomendar_wing
from graficos.graficos import grafico_viento
from graficos.graficos import grafico_wings

df = cargar_datos()

if df is None:
    print("No se pudo cargar el archivo. El programa se detiene.")
else:
    while True:
        print("\nWINGFOIL")
        print("1 - Ver cantidad de sesiones")
        print("2 - Recomendar wing")
        print("3 - Gráfico viento")
        print("4 - Gráfico wings")
        print("0 - Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("\nTotal sesiones:", len(df))

        elif opcion == "2":
            try:
                viento    = float(input("Velocidad del viento (nudos): "))
                direccion = input("Dirección del viento (ej: Norte, Noreste): ")
                ubicacion = input("Ubicación (ej: Rio de la Plata): ")
                recomendar_wing(df, viento, direccion, ubicacion)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            grafico_viento(df)

        elif opcion == "4":
            grafico_wings(df)

        elif opcion == "0":
            break

        else:
            print("Opción inválida")
