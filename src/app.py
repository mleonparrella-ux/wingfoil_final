"""
APP.PY - Interfaz Principal Unificada (Dashboard + Recomendador Inteligente)
"""
from src.carga_datos import cargar_datos
from graficos.graficos import grafico_wings
from graficos.graficos import grafico_viento

# Importamos los nuevos módulos de la API y de la lógica del recomendador
import api_clima
import recomendador

# Cargamos el dataset al iniciar la aplicación
df = cargar_datos()

# Ocultamos la clave real usando la constante de ejemplo solicitada por la cátedra
API_KEY = "TU_API_KEY"

print("\n====================")
print(" DASHBOARD WINGFOIL ")
print("====================")

print("\nRESUMEN GENERAL")
print("Total sesiones:", len(df))
print("Viento promedio:", round(df["Vel. Viento (kn)"].mean(), 2))
print("Sensación promedio:", round(df["Sensación"].mean(), 2))
print("Cantidad de wings:", df["Wing"].nunique())


while True:
    print("\n--- DASHBOARD ---")
    print("1 - Ver Gráfico de Uso de Wings")
    print("2 - Ver Gráfico de Viento")
    print("3 - Obtener Recomendación de Equipo para hoy (API Clima)")
    print("0 - Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        grafico_wings(df)

    elif opcion == "2":
        grafico_viento(df)

    elif opcion == "3":
        ## --- NUEVA FUNCIONALIDAD: RECOMENDACIÓN INTELIGENTE ---
        print("\n=== Asistente de Recomendación Inteligente ===")
        ubicacion_actual = input("¿Dónde vas a navegar hoy?: ").strip()
        condicion_agua_actual = input("¿Cómo está el agua? (flat/chop moderado/chop fuerte): ").strip()
        
        # Iniciamos variables de control para el plan de contingencia
        viento_vel_hoy = None
        viento_dir_hoy = None

        # ESTRUCTURA EXIGIDA POR LA CÁTEDRA: try/except para capturar los raise de la API
        try:
            print("Conectando con OpenWeatherMap...")
            
            # 1. Consultamos el servicio meteorológico externo
            datos_clima = api_clima.consultar_clima(ubicacion_actual, API_KEY)
            
            # 2. Procesamos las variables del viento
            viento_vel_hoy, viento_dir_hoy = api_clima.procesar_datos_viento(datos_clima)
            print(f"¡Clima obtenido con éxito! Viento: {viento_vel_hoy} kn | Dirección: {viento_dir_hoy}°")

        except ValueError as e:
            print(f"\n[Error de Entrada]: {e}")
        except NameError as e:
            print(f"\n[Error de Ubicación]: {e}")
        except (ConnectionError, RuntimeError) as e:
            print(f"\n[Error de Red]: {e}")
        except Exception as e:
            print(f"\n[Error Inesperado]: {e}")
            
        # --- PLAN DE CONTINGENCIA PARA ROBUSTEZ ---
        # Si la API falló por cualquier motivo, las variables quedan en None.
        # El programa no se interrumpe y activa el ingreso manual.
        if viento_vel_hoy is None or viento_dir_hoy is None:
            print("\n--> Activando ingreso manual de datos climáticos para continuar:")
            viento_vel_hoy = float(input("Ingresa la velocidad del viento estimada (en nudos): "))
            viento_dir_hoy = int(input("Ingresa la dirección del viento estimada (en grados): "))

        # 3. Armamos el diccionario estructurado. 
        # ATENCIÓN: Las claves internas coinciden con las columnas de tu DataFrame
        condiciones_hoy = {
            'Ubicación': ubicacion_actual,
            'Vel. Viento (kn)': viento_vel_hoy,
            'Dirección Viento': viento_dir_hoy,
            'Condición Agua': condicion_agua_actual
        }
        
        # 4. Ejecutamos el algoritmo de similitud con Pandas
        top_3, recomendacion = recomendador.generar_recomendacion(df, condiciones_hoy)
        
        # 5. Mostramos los resultados en pantalla controlando el caso de borde
        if top_3 is None:
            print(f"\n[Aviso]: {recomendacion}")
        else:
            print("\n--> Las 3 sesiones más similares encontradas en tu historial:")
            # Mostramos un resumen limpio de las columnas clave de las 3 sesiones
            print(top_3[['Ubicación', 'Vel. Viento (kn)', 'Sensación']])
            print("\n==================================================")
            print(f" SUGERENCIA DE EQUIPO BASADA EN TU HISTORIAL:")
            print(f" {recomendacion}")
            print("==================================================")

    elif opcion == "0":
        print("\n¡Buenas navegadas! Cerrando el sistema...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")