import csv
import os

# Diccionario con estaciones base (completo y en string)
estaciones_base = {
    "Estación Central": {
        "region": "Región Metropolitana",
        "descripcion": "Principal nodo ferroviario del país",
        "conexiones": ["Rancagua", "Chillán"],
        "poblacion": "8242459",
        "vias": "2",
        "orientacion": "Norte-Sur"
    },
    "Rancagua": {
        "region": "Región de O’Higgins",
        "distancia_desde_santiago": 87,
        "conexiones": ["Talca", "Estación Central"],
        "poblacion": "274407",
        "vias": "2",
        "orientacion": "Norte-Sur"
    },
    "Talca": {
        "region": "Región del Maule",
        "distancia_desde_rancagua": 200,
        "tiempo_estimado": "2 h 30 min",
        "conexiones": ["Chillán", "Rancagua"],
        "poblacion": "242344",
        "vias": "2",
        "orientacion": "Norte-Sur"
    },
    "Chillán": {
        "region": "Región de Ñuble",
        "distancia_desde_talca": 180,
        "conexiones": ["Talca", "Estación Central"],
        "poblacion": "204091",
        "vias": "2",
        "orientacion": "Norte-Sur"
    }
}

estaciones = {}
archivo = 'estaciones.csv'

def cargar_estaciones():
    estaciones.clear()  # limpia el diccionario antes de cargar

    if os.path.exists(archivo):  # si el archivo existe
        with open(archivo, 'r') as a:
            arch = csv.reader(a)
            datos_cargados = False
            for linea in arch:
                if len(linea) < 4:
                    continue  # ignora líneas incompletas
                nombre = linea[0]
                datos = linea[1:]  # poblacion, vias, orientacion
                estaciones[nombre] = datos
                datos_cargados = True

            # Si el archivo existe pero está vacío o inválido, cargar base
            if not datos_cargados:
                for nombre, datos in estaciones_base.items():
                    estaciones[nombre] = [datos["poblacion"], datos["vias"], datos["orientacion"]]
                guardar_estaciones()
    else:
        # si el archivo no existe, lo crea y carga datos base
        open(archivo, 'w').close()
        for nombre, datos in estaciones_base.items():
            estaciones[nombre] = [datos["poblacion"], datos["vias"], datos["orientacion"]]
        guardar_estaciones()

def guardar_estaciones():
    with open(archivo, 'w') as a:
        for nombre, datos in estaciones.items():
            linea = ",".join([nombre] + datos) + "\n"
            a.write(linea)

def ingresar_estacion(nombre, poblacion, vias, orientacion_vias):
    cargar_estaciones()  # cargar diccionario
    if nombre in estaciones:
        return "La estación ya existe"
    try:
        vias = int(vias)
    except ValueError:
        return "La cantidad de vías debe ser un número entero"

    if vias == 1 and orientacion_vias not in ["Norte", "Sur"]:
        return "La orientación debe ser 'Norte' o 'Sur'"
    if vias == 2 and orientacion_vias not in ["Norte-Sur", "Sur-Norte"]:
        return "La orientación debe ser 'Norte-Sur' o 'Sur-Norte'"

    estaciones[nombre] = [poblacion, str(vias), orientacion_vias]  # csv debe ser todo en str 
    guardar_estaciones()
    return "Estación agregada correctamente"

def modificar_estacion(anterior, nuevo, poblacion, vias, orientacion_vias):
    cargar_estaciones()  # datos actualizados
    if nuevo != anterior and nuevo in estaciones:
        return "El nuevo nombre de estación ya existe"
    try:
        vias = int(vias)
    except ValueError:
        return "La cantidad de vías debe ser un número entero"

    if vias == 1 and orientacion_vias not in ["Norte", "Sur"]:
        return "La orientación debe ser 'Norte' o 'Sur'"
    if vias == 2 and orientacion_vias not in ["Norte-Sur", "Sur-Norte"]:
        return "La orientación debe ser 'Norte-Sur' o 'Sur-Norte'"

    estaciones.pop(anterior, None)
    estaciones[nuevo] = [poblacion, str(vias), orientacion_vias]
    guardar_estaciones()
    return "Estación modificada correctamente"

class Estacion:
    def __init__(self, nombre, poblacion, vias=None, flujo_acumulado=0):
        self.nombre = nombre
        self.poblacion = poblacion
        self.vias = vias if vias is not None else []
        self.flujo_acumulado = flujo_acumulado

    def __str__(self):
        return f"{self.nombre} (Población: {self.poblacion})"
