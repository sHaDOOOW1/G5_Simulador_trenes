import tkinter as tk
from tkinter import ttk
from logica.estaciones import cargar_estaciones, guardar_estaciones, estaciones, ingresar_estacion, modificar_estacion  

class GestorEstaciones(tk.Toplevel): #maneja la gestion -> ingresar, modificar, eliminar

    def __init__(self):
        super().__init__()
        self.title("Gestionar Estaciones")
        self.resizable(False, False) #para no cambiar el tamaño de la ventana
        self.bg = tk.PhotoImage(file="bg.png")
        fondo = tk.Label(self, image=self.bg)
        fondo.place(x=-3, y=-3)

        #btn 
        tk.Button(self, text="Ingresar Estaciones", command=self.ingresar_estacion, padx=15, pady=10).grid(row=0, column=0, padx=70, pady=30)
        tk.Button(self, text="Modificar Estación", command=self.modificar_estacion, padx=15, pady=10).grid(row=0, column=1, padx=70, pady=30)
        tk.Button(self, text="Eliminar Estación", command=self.eliminar_estacion, padx=15, pady=10).grid(row=1, column=0, padx=70, pady=30)

        self.columnconfigure(0, weight=1) #configura el tamaño 
        self.columnconfigure(1, weight=1)

    def ingresar_estacion(self):
        ventana = tk.Toplevel(self) #crea una ventana
        ventana.title("Ingresar Estación")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        #frame
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
        tk.Label(f1, text="Nombre de la Estación").pack()
        tk.Label(f2, text="Población Total").pack()
        tk.Label(f3, text="Cantidad de Vías").pack()
        tk.Label(f4, text="Orientación de las Vías").pack()

        #entrada para los datos
        e_nombre = tk.Entry(f1)
        e_nombre.pack()
        e_poblacion = tk.Entry(f2)
        e_poblacion.pack()
        e_vias = tk.Entry(f3)
        e_vias.pack()
        combo_orientacion = ttk.Combobox(f4, values=["Norte", "Sur", "Sur-Norte", "Norte-Sur"])
        combo_orientacion.pack()

        mensaje = tk.Label(frame, text="") #muestra el mesanje -> algun error o guardado correcto
        mensaje.grid(row=2, column=0, columnspan=2)

        def guardar(): #al precionar el btn guardar 
            resultado = ingresar_estacion(
                e_nombre.get(),
                e_poblacion.get(),
                e_vias.get(),
                combo_orientacion.get()
            )
            mensaje.config(text=resultado) #mensaje

            if resultado == "Estación agregada correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=4, column=1, sticky="e", pady=10)

    def modificar_estacion(self):
        cargar_estaciones()
        ventana = tk.Toplevel(self)
        ventana.title("Modificar Estación")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        estaciones_lista = list(estaciones.keys()) #estaciones existentes

        tk.Label(frame, text="Estación a modificar").grid(row=0, column=0)
        combo = ttk.Combobox(frame, values=estaciones_lista)
        combo.grid(row=0, column=1, pady=10)

        #frames
        f1 = tk.Frame(frame, padx=20, pady=20)
        f1.grid(row=1, column=0)
        f2 = tk.Frame(frame, padx=20, pady=20)
        f2.grid(row=1, column=1)
        f3 = tk.Frame(frame, padx=20, pady=20)
        f3.grid(row=2, column=0)
        f4 = tk.Frame(frame, padx=20, pady=20)
        f4.grid(row=2, column=1)

        #etiqueta
        tk.Label(f1, text="Nuevo Nombre").pack()
        tk.Label(f2, text="Población Total").pack()
        tk.Label(f3, text="Cantidad de Vías").pack()
        tk.Label(f4, text="Orientación de las Vías").pack()

        #entrada datos
        e_nombre = tk.Entry(f1)
        e_nombre.pack()
        e_poblacion = tk.Entry(f2)
        e_poblacion.pack()
        e_vias = tk.Entry(f3)
        e_vias.pack()
        combo_orientacion = ttk.Combobox(f4, values=["Norte", "Sur", "Sur-Norte", "Norte-Sur"])
        combo_orientacion.pack()

        def rellenar(event): #la funcion se activa y rellena automaticamente los datos segun la eestacion seleccionada
            est = combo.get()
            datos_est = estaciones.get(est, ["", "", ""])
            e_nombre.delete(0, "end")
            e_nombre.insert(0, est)
            e_poblacion.delete(0, "end")
            e_poblacion.insert(0, datos_est[0])
            e_vias.delete(0, "end")
            e_vias.insert(0, datos_est[1])
            combo_orientacion.set(datos_est[2])

        combo.bind("<<ComboboxSelected>>", rellenar)

        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.grid(row=3, column=0, columnspan=2)

        def guardar():
            anterior = combo.get()
            nuevo = e_nombre.get()
            poblacion = e_poblacion.get()
            vias = e_vias.get()
            orientacion = combo_orientacion.get()

            resultado = modificar_estacion(anterior, nuevo, poblacion, vias, orientacion)
            mensaje.config(text=resultado)  #mensaje

            if resultado == "Estación modificada correctamente":
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Guardar", command=guardar).grid(row=3, column=1, sticky="e", pady=10)

    def eliminar_estacion(self):
        cargar_estaciones() #cargas todas las estaciones actuales
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar Estación")
        ventana.resizable(False, False)
        fondo = tk.Label(ventana, image=self.bg)
        fondo.place(x=-3, y=-3)

        frame = tk.Frame(ventana, padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Seleccione una estación").pack()

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #muestra las estaciones disponibles
        lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10)
        for e in estaciones:
            lista.insert(tk.END, e)
        lista.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=lista.yview)

        #label mensaje 
        mensaje = tk.Label(frame, text="", fg="black")
        mensaje.pack(pady=5)

        def eliminar(): #elimana la estacion seleccionada
            seleccion = lista.curselection()
            if seleccion:
                estacion = lista.get(seleccion)
                estaciones.pop(estacion, None) #elimina del diccionario 
                guardar_estaciones() #guarda los cambio
                mensaje.config(text="Estación eliminada correctamente")
                ventana.after(1500, ventana.destroy)

        tk.Button(frame, text="Eliminar", command=eliminar).pack(pady=10)

# Función global para abrir la ventana desde la interfaz
def mostrar_ingreso_estacion():
    ventana = GestorEstaciones()
    ventana.grab_set()