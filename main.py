from src.carga_datos import cargar_datos, guardar_sesion
from src.validacion_datos import (validar_ubicacion, validar_direccion,
                                   validar_viento, validar_sensacion, validar_duracion,
                                   UBICACIONES, DIRECCIONES)
from src.recomendacion import recomendar_equipo
from src.graficos import (grafico_sensacion_por_wing, grafico_sensacion_por_ubicacion,
                          grafico_viento_vs_sensacion)

RUTA = "dataset_sesiones.xlsx"


def pedir_ubicacion():
    """Pide y valida la ubicación al usuario."""
    print(f"Ubicaciones disponibles: {UBICACIONES}")
    while True:
        try:
            ubicacion = input("Ingrese ubicación: ")
            validar_ubicacion(ubicacion)
            return ubicacion
        except ValueError as e:
            print(f"Error: {e}")


def pedir_direccion():
    """Pide y valida la dirección del viento al usuario."""
    print(f"Direcciones disponibles: {DIRECCIONES}")
    while True:
        try:
            direccion = input("Ingrese dirección del viento: ")
            validar_direccion(direccion)
            return direccion
        except ValueError as e:
            print(f"Error: {e}")


def pedir_viento():
    """Pide y valida la velocidad del viento al usuario."""
    while True:
        try:
            viento = float(input("Ingrese velocidad del viento (nudos): "))
            validar_viento(viento)
            return viento
        except ValueError as e:
            print(f"Error: {e}")


def registrar_sesion():
    """
    Solicita los datos de una nueva sesión y la guarda en el Excel.
    """
    print("\n=== Registrar nueva sesión ===")
    fecha     = input("Ingrese la fecha (YYYY-MM-DD): ")
    ubicacion = pedir_ubicacion()
    while True:
        try:
            duracion = int(input("Ingrese duración en minutos: "))
            validar_duracion(duracion)
            break
        except ValueError as e:
            print(f"Error: {e}")
    viento    = pedir_viento()
    direccion = pedir_direccion()
    wing      = input("Ingrese wing (ej: 5m): ")
    tabla     = input("Ingrese tabla (ej: 85L): ")
    foil      = input("Ingrese foil (ej: 633): ")
    while True:
        try:
            sensacion = int(input("Ingrese sensación (1-10): "))
            validar_sensacion(sensacion)
            break
        except ValueError as e:
            print(f"Error: {e}")

    sesion = {
        "fecha":         fecha,
        "ubicacion":     ubicacion,
        "duracion_min":  duracion,
        "vel_viento_kn": viento,
        "dir_viento":    direccion,
        "wing":          wing,
        "tabla":         tabla,
        "foil":          foil,
        "sensacion":     sensacion
    }
    guardar_sesion(RUTA, sesion)
    print("Sesión registrada correctamente.")


def obtener_recomendacion(df):
    """
    Pide las condiciones del día y muestra la recomendación de equipo.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    print("\n=== Recomendación de equipo ===")
    ubicacion = pedir_ubicacion()
    direccion = pedir_direccion()
    viento    = pedir_viento()
    recomendar_equipo(df, ubicacion, direccion, viento)


def ver_graficos(df):
    """
    Genera y guarda los tres gráficos del historial.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    print("\n=== Generando gráficos ===")
    grafico_sensacion_por_wing(df)
    grafico_sensacion_por_ubicacion(df)
    grafico_viento_vs_sensacion(df)
    print("Gráficos generados en la carpeta graficos/")


# Programa principal
try:
    df = cargar_datos(RUTA)
except (FileNotFoundError, ValueError) as e:
    print(f"Error al cargar datos: {e}")
    df = None

if df is not None:
    while True:
        print("\n=== WingfoilTracker ===")
        print("1. Registrar nueva sesión")
        print("2. Obtener recomendación de equipo")
        print("3. Ver estadísticas y gráficos")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_sesion()
            df = cargar_datos(RUTA)
        elif opcion == "2":
            obtener_recomendacion(df)
        elif opcion == "3":
            ver_graficos(df)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Ingrese 1, 2, 3 o 4.")

