import tkinter as tk
from tkinter import ttk
from logica.ruta import cargar_rutas, guardar_rutas, rutas, ingresar_ruta, modificar_ruta
from logica.estaciones import estaciones, cargar_estaciones

class GestorRutas(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Gestionar Rutas")
        self.resizable(False, False)
        self.bg = tk.PhotoImage(file="bg.png")
        fondo = tk.Label(self, image=self.bg)
        fondo.place(x=-3, y=-3)

        # Botones principales
        tk.Button(self, text="Ingresar Ruta", command=self.ingresar_ruta, padx=15, pady=10).grid(row=0, column=0, padx=70, pady=30)
        tk.Button(self, text="Modificar Ruta", command=self.modificar_ruta, padx=15, pady=10).grid(row=0, column=1, padx=70, pady=30)
        tk.Button(self, text="Eliminar Ruta", command=self.eliminar_ruta, padx=15, pady=10).grid(row=1, column=0, padx=70, pady=30)

    def ingresar_ruta(self):
        cargar_rutas()
        cargar_estaciones()
        ventana = tk.Toplevel(self)
        ventana.title("Ingresar Ruta")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        f1 = tk.Frame(frame, padx=20, pady=20)
        f1.grid(row=0, column=0)
        f2 = tk.Frame(frame, padx=20, pady=20)
        f2.grid(row=0, column=1)
        f3 = tk.Frame(frame, padx=20, pady=20)
        f3.grid(row=1, column=0)
        f4 = tk.Frame(frame, padx=20, pady=20)
        f4.grid(row=1, column=1)

        #etiquetas
        tk.Label(f1, text="ID de la Ruta").pack()
        tk.Label(f2, text="Estación Origen").pack()
        tk.Label(f3, text="Estación Destino").pack()
        tk.Label(f4, text="Longitud (Km)").pack()

        #entrada datos
        entry_id = tk.Entry(f1)
        entry_id.pack()
        combo_origen = ttk.Combobox(f2, values=list(estaciones.keys()))
        combo_origen.pack()
        combo_destino = ttk.Combobox(f3, values=list(estaciones.keys()))
        combo_destino.pack()
        entry_longitud = tk.Entry(f4)
        entry_longitud.pack()

        mensaje = tk.Label(frame, text="")
        mensaje.grid(row=2, column=0, columnspan=2)

        def guardar():
            id_r = entry_id.get().strip()
            origen = combo_origen.get().strip()
            destino = combo_destino.get().strip()
            longitud = entry_longitud.get().strip()

            resultado = ingresar_ruta(id_r, origen, destino, longitud)
            mensaje.config(text=resultado)

            if resultado == "Ruta agregada correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=1, sticky="e", pady=10)

    def modificar_ruta(self):
        cargar_rutas()
        ventana = tk.Toplevel(self)
        ventana.title("Modificar Ruta")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        rutas_lista = list(rutas.keys())

        tk.Label(frame, text="Ruta a modificar").grid(row=0, column=0)
        combo = ttk.Combobox(frame, values=rutas_lista)
        combo.grid(row=0, column=1, pady=10)

        f1 = tk.Frame(frame, padx=20, pady=20)
        f1.grid(row=1, column=0)
        f2 = tk.Frame(frame, padx=20, pady=20)
        f2.grid(row=1, column=1)
        f3 = tk.Frame(frame, padx=20, pady=20)
        f3.grid(row=2, column=0)
        f4 = tk.Frame(frame, padx=20, pady=20)
        f4.grid(row=2, column=1)

        tk.Label(f1, text="Nuevo ID de Ruta").pack()
        tk.Label(f2, text="Estación Origen").pack()
        tk.Label(f3, text="Estación Destino").pack()
        tk.Label(f4, text="Longitud (Km)").pack()

        entry_id = tk.Entry(f1)
        entry_id.pack()
        combo_origen = ttk.Combobox(f2, values=list(estaciones.keys()))
        combo_origen.pack()
        combo_destino = ttk.Combobox(f3, values=list(estaciones.keys()))
        combo_destino.pack()
        entry_longitud = tk.Entry(f4)
        entry_longitud.pack()

        def rellenar(event):
            id_r = combo.get()
            datos_ruta = rutas.get(id_r, ["", "", ""])
            entry_id.delete(0, "end")
            entry_id.insert(0, id_r)
            if len(datos_ruta) == 3:
                combo_origen.set(datos_ruta[0])
                combo_destino.set(datos_ruta[1])
                entry_longitud.delete(0, "end")
                entry_longitud.insert(0, datos_ruta[2])
            else:
                combo_origen.set("")
                combo_destino.set("")
                entry_longitud.delete(0, "end")

        combo.bind("<<ComboboxSelected>>", rellenar)

        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.grid(row=3, column=0, columnspan=2)

        def guardar():
            anterior = combo.get()
            nuevo = entry_id.get().strip()
            origen = combo_origen.get().strip()
            destino = combo_destino.get().strip()
            longitud = entry_longitud.get().strip()

            resultado = modificar_ruta(anterior, nuevo, origen, destino, longitud)
            mensaje.config(text=resultado)

            if resultado == "Ruta modificada correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=1, sticky="e", pady=10)

    def eliminar_ruta(self):
        cargar_rutas()
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar Ruta")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Seleccione una ruta").pack()

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10)
        for r in rutas:
            lista.insert(tk.END, r)
        lista.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=lista.yview)

        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.pack(pady=5)

        def eliminar():
            seleccion = lista.curselection()
            if seleccion:
                ruta = lista.get(seleccion)
                rutas.pop(ruta, None)
                guardar_rutas()
                mensaje.config(text="Ruta eliminada correctamente")
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Eliminar", command=eliminar).pack(pady=10)