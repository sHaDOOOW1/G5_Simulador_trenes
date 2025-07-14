import csv
import os

class Tren:
    def __init__(self, nombre, velocidad, vagones, flujo_acumulado=0, accion="detenido"):
        self.nombre = nombre
        self.velocidad = velocidad  # km/h
        self.vagones = vagones      # lista de dicts: [{"capacidad": int}]
        self.flujo_acumulado = flujo_acumulado
        self.accion = accion        # acción actual del tren

    def __str__(self):
        return f"{self.nombre} ({self.velocidad} km/h, {len(self.vagones)} vagones)"

trenes_base = {
    "BMU (Bimodal)": {
        "energia": ["Eléctrico", "Diésel"],
        "velocidad_max": 160,
        "capacidad_pasajeros": 236
    },
    "EMU - EFE SUR": {
        "energia": ["Eléctrico"],
        "velocidad_max": 120,
        "capacidad_pasajeros": None 
    }
}

trenes = {}
archivo = 'trenes.csv'

def cargar_trenes():
    trenes.clear()
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            datos_cargados = False
            for linea in lector:
                if len(linea) < 3:
                    continue
                nombre = linea[0]
                datos = linea[1:]
                trenes[nombre] = datos
                datos_cargados = True
            # Si el archivo existe pero está vacío o inválido, cargar trenes base
            if not datos_cargados:
                for nombre, info in trenes_base.items():
                    trenes[nombre] = ["0", "0"]
                guardar_trenes()
    else:
        open(archivo, 'w').close()
        for nombre, info in trenes_base.items():
            trenes[nombre] = ["0", "0"]
        guardar_trenes()

def guardar_trenes():
    with open(archivo, 'w') as f:
        for nombre, datos in trenes.items():
            linea = ",".join([nombre] + datos) + "\n"
            f.write(linea)

def ingresar_tren(nombre, cantidad_vagones, capacidad_por_vagon, energia, velocidad, ruta):
    cargar_trenes()
    if nombre in trenes:
        return "El tren ya existe"
    try:
        cantidad_vagones = int(cantidad_vagones)
        capacidad_por_vagon = int(capacidad_por_vagon)
        velocidad = int(velocidad)
    except ValueError:
        return "Vagones, capacidad y velocidad deben ser números enteros"
    
    if cantidad_vagones <= 0 or capacidad_por_vagon <= 0 or velocidad <= 0:
        return "Todos los valores deben ser mayores a 0"

    trenes[nombre] = [
        str(cantidad_vagones),
        str(capacidad_por_vagon),
        energia,
        str(velocidad),
        ruta
    ]
    guardar_trenes()
    return "Tren agregado correctamente"

def modificar_tren(anterior, nuevo, cantidad_vagones, capacidad_por_vagon, energia, velocidad, ruta):
    cargar_trenes()
    if anterior not in trenes:
        return "El tren no existe"
    if nuevo != anterior and nuevo in trenes:
        return "El nuevo nombre ya existe"
    try:
        cantidad_vagones = int(cantidad_vagones)
        capacidad_por_vagon = int(capacidad_por_vagon)
        velocidad = int(velocidad)
    except ValueError:
        return "Vagones, capacidad y velocidad deben ser números enteros"

    if cantidad_vagones <= 0 or capacidad_por_vagon <= 0 or velocidad <= 0:
        return "Todos los valores deben ser mayores a 0"

    trenes.pop(anterior)
    trenes[nuevo] = [
        str(cantidad_vagones),
        str(capacidad_por_vagon),
        energia,
        str(velocidad),
        ruta
    ]
    guardar_trenes()
    return "Tren modificado correctamente"

def eliminar_tren(nombre):
    cargar_trenes()
    if nombre not in trenes:
        return "El tren no existe"
    trenes.pop(nombre)
    guardar_trenes()
    return "Tren eliminado correctamente"
