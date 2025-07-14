
import tkinter as tk
from tkinter import ttk

class GestorMonitoreo(tk.Toplevel):
    def __init__(self, estado_simulacion):
        super().__init__()
        self.estado = estado_simulacion
        self.title("Monitor de Indicadores")
        self.geometry("800x600")
        
        self.create_widgets()
        self.actualizar_datos()

    def create_widgets(self):
        tab_control = ttk.Notebook(self) #pestañas para diferentes vistas
        
        tab_indicadores = ttk.Frame(tab_control) #pestaña de indicadores clave
        self.setup_indicadores_tab(tab_indicadores)
        tab_control.add(tab_indicadores, text="Indicadores")
        
        tab_eventos = ttk.Frame(tab_control) #pestaña de eventos
        self.setup_eventos_tab(tab_eventos)
        tab_control.add(tab_eventos, text="Eventos")
        
        tab_tendencias = ttk.Frame(tab_control) #pestaña de tendencias
        self.setup_tendencias_tab(tab_tendencias)
        tab_control.add(tab_tendencias, text="Tendencias")
        
        tab_control.pack(expand=1, fill="both")

    def setup_indicadores_tab(self, parent):
        pass

    def setup_eventos_tab(self, parent):
        columns = ("dia", "hora", "tipo", "descripcion")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True)
        tk.Button(parent, text="Actualizar", command=self.actualizar_datos).pack()

    def setup_tendencias_tab(self, parent):
        pass

    def actualizar_datos(self):#actualizar eventos
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for evento in self.estado.eventos[-50:]:  #mostrar últimos 50 eventos
            self.tree.insert("", "end", values=(
                evento["dia"],
                evento["hora"],
                evento["tipo"],
                evento["descripcion"]
            ))