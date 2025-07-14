import tkinter as tk
from tkinter import simpledialog, messagebox
from estado_simulacion import EstadoSimulacion

estado = EstadoSimulacion()

class GestorEventos:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Eventos")
        self.ventana.geometry("400x350")

        self.lista = tk.Listbox(self.ventana, width=50)
        self.lista.pack(pady=10)

        self.actualizar_lista()

        btn_agregar = tk.Button(self.ventana, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(pady=5)

        btn_eliminar = tk.Button(self.ventana, text="Eliminar Evento", command=self.eliminar_evento)
        btn_eliminar.pack(pady=5)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for evento in estado.eventos:
            self.lista.insert(tk.END, getattr(evento, "nombre", str(evento)))

    def agregar_evento(self):
        nombre = simpledialog.askstring("Nuevo Evento", "Nombre del evento:")
        if nombre:
            try:
                from logica.evento import Evento
                nuevo_evento = Evento(nombre)
                estado.eventos.append(nuevo_evento)
                self.actualizar_lista()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo crear el evento: {e}")

    def eliminar_evento(self):
        seleccion = self.lista.curselection()
        if seleccion:
            idx = seleccion[0]
            del estado.eventos[idx]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Info", "Seleccione un evento para eliminar.")
