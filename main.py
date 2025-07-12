import tkinter as tk
from tkinter import ttk
from gestor_estaciones import *
from gestor_rutas import *
from gestor_trenes import *


# configuración ventana principal
root = tk.Tk()
root.title("Sistema de Simulación de Tráfico Ferroviario")
root.geometry("1022x574")
root.resizable(False, False) 

## crear label con imagen de fondo
bg = tk.PhotoImage(file="bg.png")
tk.Label(root, image=bg).place(x=-3, y=-3)

def gestionar_estaciones():
	GestorEstaciones()

def gestionar_rutas():
	GestorRutas()

def controlar_simulacion():
	pass

def gestionar_trenes():
	GestorTrenes()

def estado_simulacion():
	popup = tk.Toplevel()
	popup.title("Estado Simulación")
	popup.resizable(False, False)
	tk.Label(popup, image=bg).place(x=-3, y=-3)

	scrollbar = tk.Scrollbar(popup)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	list_estaciones = tk.Listbox(popup, yscrollcommand=scrollbar.set)

	for estacion in datos.estaciones:
		list_estaciones.insert(tk.END, f"{estacion}: {estacion}")
	    
	list_estaciones.pack(side=tk.TOP, fill=tk.BOTH)
	scrollbar.config(command=list_estaciones.yview)

def monitoreo_indicadores():
	pass

def generar_demanda():
	popup = tk.Toplevel()
	popup.title("Generar Demanda")
	popup.resizable(False, False)
	tk.Label(popup, image=bg).place(x=-3, y=-3)

	tk.Button(popup, text="Generar Demanda Aleatoria", command=None, padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)
	tk.Button(popup, text="Generar Demanda Fin de Semana Largo", command=None, padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)


def gestion_estado_timeline():
	pass

def guardar_simulacion():
	popup = tk.Toplevel()
	popup.title("Guardar Simulación")
	popup.resizable(False, False)
	frame = ttk.LabelFrame(popup, text="Nombre del Archivo donde se Guardara la Simulación")
	tk.Label(frame, image=bg).place(x=-3, y=-3)
	
	entry_file = tk.Entry(frame)
	entry_file.pack(side=tk.LEFT, padx=10, pady=20)
	
	def cmd_guardar():
		print(entry_file.get())
	
	tk.Button(frame, text="Guardar", command=cmd_guardar).pack(side=tk.LEFT, padx=10, pady=20)
	frame.pack()

def cargar_simulación():
	popup = tk.Toplevel()
	popup.title("Cargar Simulación")
	popup.resizable(False, False)
	frame = ttk.LabelFrame(popup, text="Nombre del Archivo desde donde Cargar la Simulación")
	tk.Label(frame, image=bg).place(x=-3, y=-3)
	
	entry_file = tk.Entry(frame)
	entry_file.pack(side=tk.LEFT, padx=10, pady=20)
	
	def cmd_cargar():
		print(entry_file.get())
	
	tk.Button(frame, text="Cargar", command=cmd_cargar).pack(side=tk.LEFT, padx=10, pady=20)
	frame.pack()

# botones
tk.Button(root, text='Gestionar Estaciones', command=gestionar_estaciones, padx=15, pady=10).grid(column=0, row=0, padx=70, pady=30)
tk.Button(root, text='Gestionar Rutas', command=gestionar_rutas, padx=15, pady=10).grid(column=1, row=0, padx=70, pady=30)
tk.Button(root, text='Controlar Simulación', command=controlar_simulacion, padx=15, pady=10).grid(column=0, row=1, padx=70, pady=30)
tk.Button(root, text='Gestionar Trenes', command=gestionar_trenes, padx=15, pady=10).grid(column=1, row=1, padx=70, pady=30)
tk.Button(root, text='Estado de Simulación', command=estado_simulacion, padx=15, pady=10).grid(column=0, row=2, padx=70, pady=30)
tk.Button(root, text='Monitorear Indicadores', command=monitoreo_indicadores, padx=15, pady=10).grid(column=1, row=2, padx=70, pady=30)
tk.Button(root, text='Generacion de Demanda', command=generar_demanda, padx=15, pady=10).grid(column=0, row=3, padx=70, pady=30)
tk.Button(root, text='Gestión de Estados y Lineas Temporales', command=gestion_estado_timeline, padx=15, pady=10).grid(column=1, row=3, padx=70, pady=30)
tk.Button(root, text='Guardar Simulación', command=guardar_simulacion, padx=15, pady=10).grid(column=0, row=4, padx=70, pady=30)
tk.Button(root, text='Cargar Simulación', command=cargar_simulación, padx=15, pady=10).grid(column=1, row=4, padx=70, pady=30)

# configurar pesos
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


root.mainloop()