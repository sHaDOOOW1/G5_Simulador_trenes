import tkinter as tk
from tkinter import ttk
from logica.trenes import cargar_trenes, ingresar_tren, modificar_tren, eliminar_tren, trenes
from logica.ruta import cargar_rutas, rutas

class GestorTrenes(tk.Toplevel):
    def __init__(self):
        super().__init__()
        cargar_rutas()
        self.title("Gestionar Trenes")
        self.resizable(False, False)
        self.bg = tk.PhotoImage(file="bg.png")
        fondo = tk.Label(self, image=self.bg)
        fondo.place(x=-3, y=-3)

        tk.Button(self, text="Ingresar Tren", command=self.ingresar_tren, padx=15, pady=10).grid(row=0, column=0, padx=70, pady=30)
        tk.Button(self, text="Modificar Tren", command=self.modificar_tren, padx=15, pady=10).grid(row=0, column=1, padx=70, pady=30)
        tk.Button(self, text="Eliminar Tren", command=self.eliminar_tren, padx=15, pady=10).grid(row=1, column=0, padx=70, pady=30)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def ingresar_tren(self):
        ventana = tk.Toplevel(self)
        ventana.title("Ingresar Tren")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        #frames
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
        f5 = tk.Frame(frame, padx=20, pady=20)
        f5.grid(row=2, column=0)
        f6 = tk.Frame(frame, padx=20, pady=20)
        f6.grid(row=2, column=1)

        #etiquetas
        tk.Label(f1, text="Nombre del Tren").pack()
        tk.Label(f2, text="Cantidad de Vagones").pack()
        tk.Label(f3, text="Capacidad por Vagón(pasajeros)").pack()
        tk.Label(f4, text="Energía").pack()
        tk.Label(f5, text="Velocidad Máxima (km/h)").pack()
        tk.Label(f6, text="Ruta Asignada").pack()

        #entrada
        e_nombre = tk.Entry(f1)
        e_nombre.pack()
        e_vagones = tk.Entry(f2)
        e_vagones.pack()
        e_capacidad = tk.Entry(f3)
        e_capacidad.pack()
        combo_energia = ttk.Combobox(f4, values=["Diesel", "Eléctrico", "Vapor"], state="readonly")
        combo_energia.pack()
        e_velocidad = tk.Entry(f5)
        e_velocidad.pack()
        combo_ruta = ttk.Combobox(f6, values=list(rutas.keys()), state="readonly")
        combo_ruta.pack()

        mensaje = tk.Label(frame, text="")
        mensaje.grid(row=4, column=0, columnspan=2)

        def guardar():
            nombre = e_nombre.get().strip()
            vagones = e_vagones.get().strip()
            capacidad = e_capacidad.get().strip()
            energia = combo_energia.get().strip()
            velocidad = e_velocidad.get().strip()
            ruta = combo_ruta.get().strip()

            resultado = ingresar_tren(nombre, vagones, capacidad, energia, velocidad, ruta)
            mensaje.config(text=resultado)
            if resultado == "Tren agregado correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=1, sticky="e", pady=10)

    def modificar_tren(self):
        cargar_trenes()
        ventana = tk.Toplevel(self)
        ventana.title("Modificar Tren")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        trenes_lista = list(trenes.keys())

        tk.Label(frame, text="Tren a modificar").grid(row=0, column=0)
        combo = ttk.Combobox(frame, values=trenes_lista)
        combo.grid(row=0, column=1, pady=10)

        f1 = tk.Frame(frame, padx=20, pady=20)
        f1.grid(row=1, column=0)
        f2 = tk.Frame(frame, padx=20, pady=20)
        f2.grid(row=1, column=1)
        f3 = tk.Frame(frame, padx=20, pady=20)
        f3.grid(row=2, column=0)
        f4 = tk.Frame(frame, padx=10, pady=10)
        f4.grid(row=2, column=1)
        f5 = tk.Frame(frame, padx=10, pady=10)
        f5.grid(row=3, column=0)
        f6 = tk.Frame(frame, padx=10, pady=10)
        f6.grid(row=3, column=1)

        #etiquetas
        tk.Label(f1, text="Nuevo Nombre").pack()
        tk.Label(f2, text="Cantidad de Vagones").pack()
        tk.Label(f3, text="Capacidad por Vagón(personas)").pack()
        tk.Label(f4, text="Energía").pack()
        tk.Label(f5, text="Velocidad Máxima").pack()
        tk.Label(f6, text="Ruta").pack()

        #entrada datos 
        e_nombre = tk.Entry(f1)
        e_nombre.pack()
        e_vagones = tk.Entry(f2)
        e_vagones.pack()
        e_capacidad = tk.Entry(f3)
        e_capacidad.pack()
        combo_energia = ttk.Combobox(f4, values=["Diesel", "Eléctrico", "Vapor"], state="readonly")
        combo_energia.pack()
        e_velocidad = tk.Entry(f5)
        e_velocidad.pack()
        combo_ruta = ttk.Combobox(f6, values=list(rutas.keys()), state="readonly")
        combo_ruta.pack()

        def rellenar(event):
            nombre = combo.get()
            datos = trenes.get(nombre, ["", "", "", "", ""])
            e_nombre.delete(0, "end")
            e_nombre.insert(0, nombre)
            e_vagones.delete(0, "end")
            e_vagones.insert(0, datos[0])
            e_capacidad.delete(0, "end")
            e_capacidad.insert(0, datos[1])
            combo_energia.set(datos[2])
            e_velocidad.delete(0, "end")
            e_velocidad.insert(0, datos[3])
            combo_ruta.set(datos[4])

        combo.bind("<<ComboboxSelected>>", rellenar)

        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.grid(row=3, column=0, columnspan=2)

        def guardar():
            anterior = combo.get()
            nuevo = e_nombre.get().strip()
            vagones = e_vagones.get().strip()
            capacidad = e_capacidad.get().strip()
            energia = combo_energia.get().strip()
            velocidad = e_velocidad.get().strip()
            ruta = combo_ruta.get().strip()

            resultado = modificar_tren(anterior, nuevo, vagones, capacidad, energia, velocidad, ruta)
            mensaje.config(text=resultado)
            if resultado == "Tren modificado correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=5, column=1, sticky="e", pady=10)

    def eliminar_tren(self):
        cargar_trenes()
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar Tren")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Seleccione un tren").pack()

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10)
        for t in trenes:
            lista.insert(tk.END, t)
        lista.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=lista.yview)

        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.pack(pady=5)

        def eliminar():
            seleccion = lista.curselection()
            if seleccion:
                tren = lista.get(seleccion)
                resultado = eliminar_tren(tren)
                mensaje.config(text=resultado)
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Eliminar", command=eliminar).pack(pady=10)
