import tkinter as tk
from tkinter import ttk
import datos

class GestorEstaciones(tk.Toplevel):
	def ingresar_estacion(self):
		ingresar = tk.Toplevel()
		ingresar.title("Ingresar Estacion")
		ingresar.resizable(False, False)
		label_bg = tk.Label(ingresar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_ingresar = tk.Frame(ingresar, padx=10, pady=10)
		frame_ingresar.pack(expand=True, padx=20, pady=20)
		frame_nombre = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_nombre.grid(column=0, row=0)
		frame_poblacion = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_poblacion.grid(column=1, row=0)
		frame_vias = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_vias.grid(column=0, row=1)
		frame_orientacion = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_orientacion.grid(column=1, row=1)

		frame_ingresar.columnconfigure(0, weight=1)
		frame_ingresar.columnconfigure(1, weight=1)

		# labels
		label_nombre = tk.Label(frame_nombre, text="Nombre de la Estación")
		label_nombre.pack()
		label_poblacion = tk.Label(frame_poblacion, text="Población Total")
		label_poblacion.pack()
		label_vias = tk.Label(frame_vias, text="Cantidad de Vias")
		label_vias.pack()
		label_orientacion = tk.Label(frame_orientacion, text="Orientación de las Vias")
		label_orientacion.pack()

		# entries
		entry_nombre = tk.Entry(frame_nombre)
		entry_nombre.pack()
		entry_poblacion = tk.Entry(frame_poblacion)
		entry_poblacion.pack()
		entry_vias = tk.Entry(frame_vias)
		entry_vias.pack()

		# combo box
		combo_orientacion = ttk.Combobox(frame_orientacion, values=["Norte", "Sur"])
		combo_orientacion.pack()

		def cmd_guardar():
			print(f"{entry_nombre.get()},{entry_poblacion.get()},{entry_vias.get()},{combo_orientacion.get()}")
			if len(entry_nombre.get().strip()) != 0:
				datos.estaciones.append(entry_nombre.get())

		# button
		btn_guardar = tk.Button(frame_ingresar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=2)

	def modificar_estacion(self):
		modificar = tk.Toplevel()
		modificar.title("Modificar Estacion")
		modificar.resizable(False, False)
		label_bg = tk.Label(modificar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_modificar = tk.Frame(modificar, padx=10, pady=10)
		frame_modificar.pack(expand=True, padx=20, pady=20)
		frame_nombre = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_nombre.grid(column=0, row=1)
		frame_poblacion = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_poblacion.grid(column=1, row=1)
		frame_vias = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_vias.grid(column=0, row=2)
		frame_orientacion = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_orientacion.grid(column=1, row=2)

		# labels
		label_estaciones = tk.Label(frame_modificar, text="Estación a Modificar")
		label_estaciones.grid(column=0, row=0)
		label_nombre = tk.Label(frame_nombre, text="Nombre de la Estación")
		label_nombre.pack()
		label_poblacion = tk.Label(frame_poblacion, text="Población Total")
		label_poblacion.pack()
		label_vias = tk.Label(frame_vias, text="Cantidad de Vias")
		label_vias.pack()
		label_orientacion = tk.Label(frame_orientacion, text="Orientación de las Vias")
		label_orientacion.pack()

		# entries
		entry_nombre = tk.Entry(frame_nombre)
		entry_nombre.pack()
		entry_poblacion = tk.Entry(frame_poblacion)
		entry_poblacion.pack()
		entry_vias = tk.Entry(frame_vias)
		entry_vias.pack()

		# poblar datos
		def select(event):
			estacion = combo_estaciones.get()
			entry_nombre.delete(0, "end")
			entry_nombre.insert(0, estacion) #.nombre??????
			entry_poblacion.delete(0, "end")
			entry_poblacion.insert(0, estacion)
			entry_vias.delete(0, "end")
			entry_vias.insert(0, estacion)
			combo_orientacion.set(estacion)

		# combo boxes
		combo_estaciones = ttk.Combobox(frame_modificar, values=datos.estaciones)
		combo_estaciones.grid(column=1, row=0)
		combo_estaciones.bind("<<ComboboxSelected>>", select)
		combo_orientacion = ttk.Combobox(frame_orientacion, values=["Norte", "Sur"])
		combo_orientacion.pack()

		def cmd_guardar():
			print(f"{entry_nombre.get()},{entry_poblacion.get()},{entry_vias.get()},{combo_orientacion.get()}")
			for i in range(len(datos.estaciones)):
				if datos.estaciones[i] == combo_estaciones.get():
					datos.estaciones[i] = entry_nombre.get()

		# button
		btn_guardar = tk.Button(frame_modificar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=3)

	def eliminar_estacion(self):
		eliminar = tk.Toplevel()
		eliminar.title("Eliminar Estacion")
		eliminar.resizable(False, False)
		label_bg = tk.Label(eliminar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_eliminar = tk.Frame(eliminar, padx=10, pady=10)
		frame_eliminar.pack(expand=True, padx=20, pady=20)

		# lista de estaciones
		scrollbar = tk.Scrollbar(frame_eliminar)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		list_estaciones = tk.Listbox(frame_eliminar, yscrollcommand=scrollbar.set)

		for estacion in datos.estaciones:
			list_estaciones.insert(tk.END, estacion)
		    
		list_estaciones.pack(side=tk.TOP, fill=tk.BOTH)
		scrollbar.config(command=list_estaciones.yview)

		def cmd_eliminar():
			x = list_estaciones.get(list_estaciones.curselection())
			if x in datos.estaciones:
				datos.estaciones.remove(x)
			eliminar.destroy()
			self.eliminar_estacion()

		# buttons
		btn_eliminar = tk.Button(frame_eliminar, text="Eliminar", command=cmd_eliminar)
		btn_eliminar.pack()

	def __init__(self):
		# super constructor
		tk.Toplevel.__init__(self)
		# configuracion ventana
		self.title("Gestionar Estaciones")
		self.resizable(False, False)

		## crear label con imagen de fondo
		self.bg = tk.PhotoImage(file="bg.png")
		label_bg = tk.Label(self, image=self.bg)
		label_bg.place(x=-3, y=-3)

		# botones
		tk.Button(self, text='Ingresar Estaciones', command=self.ingresar_estacion, padx=15, pady=10).grid(column=0, row=0, padx=70, pady=30)
		tk.Button(self, text='Modificar Estacion', command=self.modificar_estacion, padx=15, pady=10).grid(column=1, row=0, padx=70, pady=30)
		tk.Button(self, text='Eliminar Estacion', command=self.eliminar_estacion, padx=15, pady=10).grid(column=0, row=1, padx=70, pady=30)

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)