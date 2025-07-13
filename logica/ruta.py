import csv
import os

rutas = {}
archivo = 'rutas.csv'

def cargar_rutas():
    if os.path.exists(archivo):  #si el archivo existe
        with open(archivo, 'r') as f:
            lector = csv.reader(f) #lee linea a linea y lo convierte en una lista
            for linea in lector:
                id_ruta = linea[0]  #id
                datos = linea[1:]  #origen,destino,longitud
                rutas[id_ruta] = datos   #guarda en el diccionario
    else:
        open(archivo, 'w').close()  #crea el archivo si no existe

def guardar_rutas():
    with open(archivo, 'w') as f:
        for id_ruta, datos in rutas.items():
            linea = ",".join([id_ruta] + datos) + "\n"
            f.write(linea)

def ingresar_ruta(id_ruta, origen, destino, longitud):
    cargar_rutas()  #cargar diccionario
    if id_ruta in rutas:
        return "La ruta ya existe"
    try:
        longitud = float(longitud)
    except ValueError:
        return "La longitud debe ser un número"

    if longitud <= 0:
        return "La longitud debe ser mayor a 0"

    rutas[id_ruta] = [origen, destino, str(longitud)] #se guardan como: rutas["01"] = ["Santiago", "Valparaíso", "115"]
    guardar_rutas()
    return "Ruta agregada correctamente"

def modificar_ruta(anterior, nuevo, origen, destino, longitud):
    cargar_rutas()
    if anterior not in rutas:
        return "La ruta no existe"
    try:
        longitud = float(longitud)
    except ValueError:
        return "La longitud debe ser un número"
    if longitud <= 0:
        return "La longitud debe ser mayor a 0"

    if nuevo != anterior and nuevo in rutas:
        return "El nuevo ID ya existe"
    rutas.pop(anterior)
    rutas[nuevo] = [origen, destino, str(longitud)]
    guardar_rutas()
    return "Ruta modificada correctamente"
