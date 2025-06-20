import tkinter as tk
from estaciones import *

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

#btn - gestionar estaciones"
btn_gestionar = tk.Button(root, text="Gestionar estaciones", command=mostrar_ingreso_estacion)
btn_gestionar.pack()

root.mainloop()