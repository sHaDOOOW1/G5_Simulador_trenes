import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import random

from logica.estaciones import estaciones, cargar_estaciones

class GeneradorDemanda:
    def __init__(self, estaciones_nombres, semilla=None):
        self.estaciones_nombres = estaciones_nombres
        self.semilla = semilla or 12345
        random.seed(self.semilla)
        self.personas = []

    def generar_aleatoria(self, hora_inicio, duracion_horas):
        self.personas.clear()
        for nombre in self.estaciones_nombres:
            try:
                poblacion = int(estaciones[nombre][0])  # ← [0] es la población
            except (KeyError, ValueError, IndexError):
                continue
            cantidad = int(poblacion * 0.20)
            for i in range(cantidad):
                minutos = random.randint(0, duracion_horas * 60)
                self.personas.append({
                    'id': f"{nombre}-{i}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones_nombres if e != nombre]),
                    'hora': hora_inicio + timedelta(minutes=minutos),
                    'tipo': 'normal'
                })

    def generar_finde_largo(self, hora_inicio, duracion_horas):
        self.personas.clear()
        for nombre in self.estaciones_nombres:
            try:
                poblacion = int(estaciones[nombre][0])
            except (KeyError, ValueError, IndexError):
                continue
            cantidad = int(poblacion * 0.25)
            for i in range(cantidad):
                hora = max(6, min(20, int(random.normalvariate(12, 3))))
                minutos = random.randint(0, 59)
                self.personas.append({
                    'id': f"{nombre}-FL-{i}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones_nombres if e != nombre]),
                    'hora': hora_inicio + timedelta(hours=hora, minutes=minutos),
                    'tipo': 'finde_largo'
                })

def GestorDemanda():
    cargar_estaciones()
    estaciones_disponibles = list(estaciones.keys())
    generador = GeneradorDemanda(estaciones_nombres=estaciones_disponibles)

    popup = tk.Toplevel()
    popup.title("Generar Demanda")
    popup.geometry("500x200")
    popup.resizable(False, False)

    try:
        bg = tk.PhotoImage(file="bg.png")
        tk.Label(popup, image=bg).place(x=-3, y=-3)
        popup.bg = bg
    except:
        pass

    def cmd_generar_aleatoria():
        generador.generar_aleatoria(datetime.now(), 24)
        messagebox.showinfo("Éxito", f"{len(generador.personas)} personas generadas (aleatoria)")
        popup.destroy()

    def cmd_generar_finde():
        generador.generar_finde_largo(datetime.now(), 48)
        messagebox.showinfo("Éxito", f"{len(generador.personas)} personas generadas (finde largo)")
        popup.destroy()

    tk.Button(popup, text="Generar Demanda Aleatoria", command=cmd_generar_aleatoria, padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)
    tk.Button(popup, text="Generar Fin de Semana Largo", command=cmd_generar_finde, padx=15, pady=10).pack(side=tk.LEFT, padx=20, pady=50)
