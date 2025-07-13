import tkinter as tk
from logica.estaciones import *
from logica.ruta import *
from gestiones.gestor_estaciones import GestorEstaciones
from gestiones.gestor_rutas import GestorRutas
from gestiones.gestor_trenes import GestorTrenes
from gestiones.gestor_demanda import GestorDemanda

#configuración ventana principal
root = tk.Tk()
root.title("Sistema de Simulación de Tráfico Ferroviario")
root.geometry("1022x574")
root.resizable(False, False) #evita que se pueda agrandar o achicar la ventana

#imagen de fondo
bg = tk.PhotoImage(file="bg.png")
tk.Label(root, image=bg).place(x=-3, y=-3)

def gestionar_estaciones():
	GestorEstaciones()

def gestionar_rutas():
	GestorRutas()

def gestionar_trenes():
	GestorTrenes()

def generar_demanda():
    GestorDemanda()

#cuadro
cuadro = tk.Frame(root, bg="#f0f0f0", width=350, height=420)
cuadro.place(x=610, y=50)
label_dia = tk.Label(cuadro, text="Día:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_dia.place(x=10, y=10)

#btn
tk.Button(root, text="Gestionar Estaciones", command=gestionar_estaciones, padx=15, pady=10).place(x=100, y=50)
tk.Button(root, text="Gestionar Rutas", command=gestionar_rutas, padx=28, pady=10).place(x=100, y=120)
tk.Button(root, text='Gestionar Trenes', command=gestionar_trenes, padx=27, pady=10).place(x=100, y=200)
tk.Button(root, text="Generación de Demanda", command=generar_demanda, padx=15, pady=10).place(x=350, y=50)
tk.Button(root, text="Guardar Simulación", command=None, padx=15, pady=10).place(x=820, y=480)

root.mainloop()