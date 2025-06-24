"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Encabezados están en las primeras dos líneas
    linea1 = lines[0].strip()
    linea2 = lines[1].strip()
    encabezado_crudo = re.sub(r"\s{2,}", "|", linea1 + " " + linea2)
    columnas = [
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave',
    ]

    datos = []
    bloque = ""
    for linea in lines[4:]:
        if re.match(r"^\s+\d+", linea):  # Nueva fila de cluster
            if bloque:
                datos.append(bloque)
            bloque = linea
        else:
            bloque += linea
    if bloque:
        datos.append(bloque)

    registros = []
    for bloque in datos:
        bloque = bloque.replace("\n", " ")
        partes = re.split(r"\s{2,}", bloque.strip())
        cluster = int(partes[0])
        cantidad = int(partes[1])
        porcentaje = float(partes[2].replace(",", ".").replace("%", ""))
        palabras = " ".join(partes[3:]).strip().rstrip(".")
        palabras = re.sub(r"\s+", " ", palabras)
        registros.append([cluster, cantidad, porcentaje, palabras])

    df = pd.DataFrame(registros, columns=columnas)
    return df