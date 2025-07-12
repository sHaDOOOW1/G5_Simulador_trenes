import tkinter as tk
from o.estaciones import *
from o.ruta import *

#ventana principal
root = tk.Tk()
root.title("Hola")
root.geometry("300x300")

def mostrar_ingreso_estacion():
    root.title("Ingresar Estación")

    #falta borrar para que aparezca lo demas 

    #nombre estacion
    nombre_estacion = tk.Label(root, text="Ingrese el nombre de la estación:")
    nombre_estacion.pack()
    entrada_nombre = tk.Entry(root, width=20) #box para ingresar 
    entrada_nombre.pack()

    #poblacion
    poblacion = tk.Label(root, text="Población total:")
    poblacion.pack()
    entrada_poblacion = tk.Entry(root, width=20)
    entrada_poblacion.pack()

    #cantidad de vias
    cant_vias = tk.Label(root, text="Cantidad de vias:")
    cant_vias.pack()
    entrada_cantVias = tk.Entry(root, width=20)
    entrada_cantVias.pack() 

    #orientacion de vias
    orientacion_vias = tk.Label(root, text="orientacion de vias:")
    orientacion_vias.pack()
    entrada_orientacion = tk.Entry(root, width=20)
    entrada_orientacion.pack() 

    mensaje = tk.Label(root, text="")
    mensaje.pack()

    def guardar_datos():
        nombre = entrada_nombre.get()
        poblacion = entrada_poblacion.get()
        vias = entrada_cantVias.get()
        orientacion_vias = entrada_orientacion.get()

        resultado = ingresar_estacion(nombre, poblacion, vias, orientacion_vias)

        mensaje.config(text=resultado)

    #btn - guardar
    btn_guardar = tk.Button(root, text="guardar", command=guardar_datos)
    btn_guardar.pack()

def mostrar_ingreso_ruta():
    root.title("Ingresar Ruta")

    #id ruta
    label_id = tk.Label(root, text="ID de la ruta:")
    label_id.pack()
    entrada_id = tk.Entry(root, width=20)
    entrada_id.pack()

    #estacion origen 
    label_origen = tk.Label(root, text="Estación de origen:")
    label_origen.pack()
    entrada_origen = tk.Entry(root, width=20)
    entrada_origen.pack()

    #estacion destino -> aqui podria mostrar las estaciones disponibles en vez de ingresarla
    label_destino = tk.Label(root, text="Estación de destino:")
    label_destino.pack()
    entrada_destino = tk.Entry(root, width=20)
    entrada_destino.pack()

    #longitud
    label_longitud = tk.Label(root, text="Longitud (km):")
    label_longitud.pack()
    entrada_longitud = tk.Entry(root, width=20)
    entrada_longitud.pack()

    mensaje = tk.Label(root, text="")
    mensaje.pack()

    def guardar_ruta():
        id_ruta = entrada_id.get()
        origen = entrada_origen.get()
        destino = entrada_destino.get()
        longitud = entrada_longitud.get()

        resultado = ingresar_ruta(id_ruta, origen, destino, longitud)
        mensaje.config(text=resultado)

    btn_guardar = tk.Button(root, text="Guardar Ruta", command=guardar_ruta)
    btn_guardar.pack(pady=5)

#btn - gestionar estaciones
btn_gestionar = tk.Button(root, text="Gestionar estaciones", command=mostrar_ingreso_estacion)
btn_gestionar.pack()

#btn - gestionar rutas"
btn_rutas = tk.Button(root, text="Gestionar Rutas", command=mostrar_ingreso_ruta)
btn_rutas.pack(pady=20)

root.mainloop()