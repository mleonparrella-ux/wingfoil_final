
def buscar_sesiones_similares(df, ubicacion, direccion, viento):
    """
    Busca sesiones similares en el historial según ubicación, dirección y viento.

    Una sesión es similar si tiene la misma ubicación, la misma dirección
    de viento y una velocidad de viento dentro de ±3 nudos.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
        ubicacion (str): ubicación ingresada por el usuario.
        direccion (str): dirección del viento ingresada por el usuario.
        viento (float): velocidad del viento en nudos.

    Retorna:
        DataFrame: sesiones similares ordenadas por sensación descendente.
    """
    similares = df[
        (df["ubicacion"]     == ubicacion) &
        (df["dir_viento"]    == direccion) &
        (df["vel_viento_kn"] >= viento - 3) &
        (df["vel_viento_kn"] <= viento + 3)
    ]
    return similares.sort_values("sensacion", ascending=False)


def recomendar_equipo(df, ubicacion, direccion, viento):
    """
    Recomienda el equipo más adecuado según condiciones similares con sensación >= 8.

    Busca sesiones similares y filtra las que tuvieron sensación >= 8.
    Si no hay ninguna, muestra las mejores disponibles.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
        ubicacion (str): ubicación ingresada por el usuario.
        direccion (str): dirección del viento ingresada por el usuario.
        viento (float): velocidad del viento en nudos.
    """
    similares = buscar_sesiones_similares(df, ubicacion, direccion, viento)

    if len(similares) == 0:
        print("No se encontraron sesiones similares en el historial.")
        return

    buenas = similares[similares["sensacion"] >= 8]

    if len(buenas) == 0:
        print("No hay sesiones con sensación >= 8 en esas condiciones.")
        print("Las mejores sesiones similares fueron:")
        top = similares.head(3)
    else:
        print("=== Sesiones similares con sensación >= 8 ===")
        top = buenas.head(3)

    for i in range(len(top)):
        fila = top.iloc[i]
        print(f"{i+1}. Fecha: {fila['fecha']} | Wing: {fila['wing']} | "
              f"Tabla: {fila['tabla']} | Foil: {fila['foil']} | "
              f"Sensación: {fila['sensacion']}/10")

    print("\n=== Recomendación ===")
    mejor = top.iloc[0]
    print(f"Wing: {mejor['wing']} | Tabla: {mejor['tabla']} | Foil: {mejor['foil']}")
    print(f"Sensación promedio: {top['sensacion'].mean():.1f}/10")