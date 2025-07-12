import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import random  # Importación faltante
from gestor_estaciones import *
from gestor_rutas import *
from gestor_trenes import *
import datos

# configuración ventana principal
root = tk.Tk()
root.title("Sistema de Simulación de Tráfico Ferroviario")
root.geometry("1022x574")
root.resizable(False, False) 

# crear label con imagen de fondo
bg = tk.PhotoImage(file="bg.png")
tk.Label(root, image=bg).place(x=-3, y=-3)

class GeneradorDemanda:
    def __init__(self, estaciones, semilla=None):
        self.estaciones = estaciones
        self.semilla = semilla or 12345
        random.seed(self.semilla)
        self.personas = []
    
    def generar_aleatoria(self, hora_inicio, duracion_horas):
        for nombre in self.estaciones:
            poblacion = 10000  # Valor por defecto
            cantidad = int(poblacion * 0.20)
            
            for i in range(cantidad):
                minutos = random.randint(0, duracion_horas * 60)
                self.personas.append({
                    'id': f"{nombre}-{i}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones if e != nombre]),
                    'hora': hora_inicio + timedelta(minutes=minutos),
                    'tipo': 'normal'
                })
    
    def generar_finde_largo(self, hora_inicio, duracion_horas):
        for nombre in self.estaciones:
            poblacion = 10000
            cantidad = int(poblacion * 0.25)
            
            for i in range(cantidad):
                hora = max(6, min(20, int(random.normalvariate(12, 3))))
                minutos = random.randint(0, 59)
                self.personas.append({
                    'id': f"{nombre}-FL-{i}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones if e != nombre]),
                    'hora': hora_inicio + timedelta(hours=hora, minutes=minutos),
                    'tipo': 'finde_largo'
                })

# Crear instancia del generador
generador = GeneradorDemanda(estaciones=datos.estaciones)

# Funciones de la interfaz
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

    def cmd_generar_aleatoria():
        generador.generar_aleatoria(datetime.now(), 24)
        messagebox.showinfo("Éxito", "Demanda aleatoria generada")
        popup.destroy()

    def cmd_generar_finde():
        generador.generar_finde_largo(datetime.now(), 48)
        messagebox.showinfo("Éxito", "Demanda fin de semana generada")
        popup.destroy()

    tk.Button(popup, text="Generar Demanda Aleatoria", command=cmd_generar_aleatoria, 
             padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)
    tk.Button(popup, text="Generar Fin de Semana Largo", command=cmd_generar_finde, 
             padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)

def gestion_estado_timeline():
    pass

def guardar_simulacion():
    popup = tk.Toplevel()
    popup.title("Guardar Simulación")
    popup.resizable(False, False)
    frame = ttk.LabelFrame(popup, text="Nombre del archivo para guardar")
    tk.Label(frame, image=bg).place(x=-3, y=-3)
    
    entry_file = tk.Entry(frame)
    entry_file.pack(side=tk.LEFT, padx=10, pady=20)
    
    def cmd_guardar():
        print(entry_file.get())
    
    tk.Button(frame, text="Guardar", command=cmd_guardar).pack(side=tk.LEFT, padx=10, pady=20)
    frame.pack()

def cargar_simulacion():
    popup = tk.Toplevel()
    popup.title("Cargar Simulación")
    popup.resizable(False, False)
    frame = ttk.LabelFrame(popup, text="Nombre del archivo para cargar")
    tk.Label(frame, image=bg).place(x=-3, y=-3)
    
    entry_file = tk.Entry(frame)
    entry_file.pack(side=tk.LEFT, padx=10, pady=20)
    
    def cmd_cargar():
        print(entry_file.get())
    
    tk.Button(frame, text="Cargar", command=cmd_cargar).pack(side=tk.LEFT, padx=10, pady=20)
    frame.pack()

# Configuración de botones
botones = [
    ("Gestionar Estaciones", gestionar_estaciones),
    ("Gestionar Rutas", gestionar_rutas),
    ("Controlar Simulación", controlar_simulacion),
    ("Gestionar Trenes", gestionar_trenes),
    ("Estado de Simulación", estado_simulacion),
    ("Monitorear Indicadores", monitoreo_indicadores),
    ("Generación de Demanda", generar_demanda),
    ("Gestión de Estados", gestion_estado_timeline),
    ("Guardar Simulación", guardar_simulacion),
    ("Cargar Simulación", cargar_simulacion)
]

for i, (texto, comando) in enumerate(botones):
    row = i // 2
    col = i % 2
    tk.Button(root, text=texto, command=comando, padx=15, pady=10).grid(
        column=col, row=row, padx=70, pady=30)

# Configuración de grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop() 