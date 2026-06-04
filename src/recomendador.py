

def sesiones_similares(df, viento, direccion, ubicacion):
    """
    Busca sesiones similares según viento, dirección y ubicación.

    Una sesión es similar si tiene la misma ubicación, la misma dirección
    de viento y una velocidad de viento dentro de ±3 nudos.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
        viento (float): velocidad del viento en nudos.
        direccion (str): dirección del viento.
        ubicacion (str): ubicación de la sesión.

    Retorna:
        DataFrame: sesiones similares.
    """
    similares = df[
        (abs(df["Vel. Viento (kn)"] - viento) <= 3) &
        (df["Dirección"] == direccion) &
        (df["Ubicación"] == ubicacion)
    ]
    return similares


def recomendar_wing(df, viento, direccion, ubicacion):
    """
    Recomienda el wing más adecuado según condiciones similares.

    Busca sesiones similares y recomienda el wing más usado
    con sensación promedio.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
        viento (float): velocidad del viento en nudos.
        direccion (str): dirección del viento.
        ubicacion (str): ubicación de la sesión.

    Lanza:
        ValueError: si el viento es negativo o cero.
    """
    if viento <= 0:
        raise ValueError("La velocidad del viento debe ser mayor a 0")

    similares = sesiones_similares(df, viento, direccion, ubicacion)

    if len(similares) == 0:
        print("No hay sesiones similares")
        return

    wing = similares["Wing"].mode()[0]
    print("\nWing recomendado:")
    print(wing)
    print(
        "Sensación promedio:",
        round(similares["Sensación"].mean(), 2)
    )
