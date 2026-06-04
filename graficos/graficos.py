import os
import matplotlib.pyplot as plt

def crear_carpeta_graficos():
    """
    Crea la carpeta graficos/ si no existe.
    """
    if not os.path.exists("graficos"):
        os.mkdir("graficos")


def grafico_sensacion_por_wing(df):
    """
    Genera un gráfico de barras con la sensación promedio por wing.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    crear_carpeta_graficos()
    promedio = df.groupby("wing")["sensacion"].mean()
    fig, ax = plt.subplots(figsize=(9, 5))
    promedio.plot(kind="bar", color="#1e3a8a", edgecolor="black", alpha=0.8, ax=ax)
    ax.set_title("Sensación promedio por wing", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Wing", fontsize=11)
    ax.set_ylabel("Sensación promedio (1-10)", fontsize=11)
    plt.xticks(rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
    plt.savefig("graficos/sensacion_por_wing.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/sensacion_por_wing.png")


def grafico_sensacion_por_ubicacion(df):
    """
    Genera un gráfico de barras con la sensación promedio por ubicación.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    crear_carpeta_graficos()
    promedio = df.groupby("ubicacion")["sensacion"].mean()
    fig, ax = plt.subplots(figsize=(9, 5))
    promedio.plot(kind="bar", color="#0f6e56", edgecolor="black", alpha=0.8, ax=ax)
    ax.set_title("Sensación promedio por ubicación", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Ubicación", fontsize=11)
    ax.set_ylabel("Sensación promedio (1-10)", fontsize=11)
    plt.xticks(rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
    plt.savefig("graficos/sensacion_por_ubicacion.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/sensacion_por_ubicacion.png")


def grafico_viento_vs_sensacion(df):
    """
    Genera un gráfico de dispersión entre velocidad del viento y sensación.

    Parámetros:
        df (DataFrame): historial completo de sesiones.
    """
    crear_carpeta_graficos()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(df["vel_viento_kn"], df["sensacion"], color="#b45309", alpha=0.7)
    ax.set_title("Viento vs Sensación", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Velocidad del viento (nudos)", fontsize=11)
    ax.set_ylabel("Sensación (1-10)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graficos/viento_vs_sensacion.png", dpi=300)
    plt.close()
    print("Gráfico guardado: graficos/viento_vs_sensacion.png")