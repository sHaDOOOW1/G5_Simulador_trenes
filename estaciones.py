import csv
import os

estaciones = {}
archivo = 'estaciones.csv'

def cargar_estaciones():
    if os.path.exists(archivo): #si el archivo existe
        with open(archivo, 'r') as a:
            arch = csv.reader(a) #lee linea a linea y lo convierte en una lista
            for x in arch:
                nombre = x[0] #nombre de la estacion
                datos = x[1:]  #poblacion,vias,orientacion
                estaciones[nombre] = datos #los guarda en el diccionario
    else:
        open(archivo, 'w').close()  # crea el archivo si no existe

def guardar_estaciones():
    with open(archivo, 'w') as a:
        for nombre, datos in estaciones.items():
            linea = ",".join([nombre] + datos) + "\n"
            a.write(linea)

def ingresar_estacion(nombre, poblacion, vias, orientacion_vias):
    cargar_estaciones()  #cargar diccionario

    if nombre in estaciones:
        return "La estación ya existe"

    try:
        vias = int(vias)
    except ValueError:
        return "La cantidad de vías debe ser un número"

    if vias < 1 or vias > 2:
        return "La cantidad de vías debe ser 1 o 2"

    estaciones[nombre] = [poblacion, str(vias), orientacion_vias] #csv debe ser todo en str 
    guardar_estaciones()
    return "Estación agregada correctamente"