import tkinter as tk
from tkinter import ttk
import datos

class GestorTrenes(tk.Toplevel):
	def ingresar_tren(self):
		ingresar = tk.Toplevel()
		ingresar.title("Ingresar Tren")
		ingresar.resizable(False, False)
		label_bg = tk.Label(ingresar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_ingresar = tk.Frame(ingresar, padx=10, pady=10)
		frame_ingresar.pack(expand=True, padx=20, pady=20)
		frame_nombre = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_nombre.grid(column=0, row=0)
		frame_vagones = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_vagones.grid(column=1, row=0)
		frame_capacidad = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_capacidad.grid(column=0, row=1)

		frame_ingresar.columnconfigure(0, weight=1)
		frame_ingresar.columnconfigure(1, weight=1)

		# labels
		label_nombre = tk.Label(frame_nombre, text="Nombre del Tren")
		label_nombre.pack()
		label_vagones = tk.Label(frame_vagones, text="Cantidad de Vagones")
		label_vagones.pack()
		label_capacidad = tk.Label(frame_capacidad, text="Capacidad por Vagon")
		label_capacidad.pack()

		# entries
		entry_nombre = tk.Entry(frame_nombre)
		entry_nombre.pack()
		entry_vagones = tk.Entry(frame_vagones)
		entry_vagones.pack()
		entry_capacidad = tk.Entry(frame_capacidad)
		entry_capacidad.pack()

		def cmd_guardar():
			print(f"{entry_nombre.get()},{entry_vagones.get()},{entry_capacidad.get()}")
			if len(entry_nombre.get().strip()) != 0:
				datos.trenes.append(entry_nombre.get())

		# button
		btn_guardar = tk.Button(frame_ingresar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=2)

	def modificar_tren(self):
		modificar = tk.Toplevel()
		modificar.title("Modificar Tren")
		modificar.resizable(False, False)
		label_bg = tk.Label(modificar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_modificar = tk.Frame(modificar, padx=10, pady=10)
		frame_modificar.pack(expand=True, padx=20, pady=20)
		frame_nombre = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_nombre.grid(column=0, row=1)
		frame_vagones = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_vagones.grid(column=1, row=1)
		frame_capacidad = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_capacidad.grid(column=0, row=2)
		frame_orientacion = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_orientacion.grid(column=1, row=2)

		# labels
		label_trenes = tk.Label(frame_modificar, text="Tren a Modificar")
		label_trenes.grid(column=0, row=0)
		label_nombre = tk.Label(frame_nombre, text="Nombre del Tren")
		label_nombre.pack()
		label_vagones = tk.Label(frame_vagones, text="Cantidad de Vagones")
		label_vagones.pack()
		label_capacidad = tk.Label(frame_capacidad, text="Capacidad por Vagon")
		label_capacidad.pack()

		# entries
		entry_nombre = tk.Entry(frame_nombre)
		entry_nombre.pack()
		entry_vagones = tk.Entry(frame_vagones)
		entry_vagones.pack()
		entry_capacidad = tk.Entry(frame_capacidad)
		entry_capacidad.pack()

		# poblar datos
		def select(event):
			tren = combo_trenes.get()
			entry_nombre.delete(0, "end")
			entry_nombre.insert(0, tren) #.nombre??????
			entry_vagones.delete(0, "end")
			entry_vagones.insert(0, tren)
			entry_capacidad.delete(0, "end")
			entry_capacidad.insert(0, tren)
			combo_orientacion.set(tren)

		# combo boxes
		combo_trenes = ttk.Combobox(frame_modificar, values=datos.trenes)
		combo_trenes.grid(column=1, row=0)
		combo_trenes.bind("<<ComboboxSelected>>", select)

		def cmd_guardar():
			print(f"{entry_nombre.get()},{entry_vagones.get()},{entry_capacidad.get()}")
			for i in range(len(datos.trenes)):
				if datos.trenes[i] == combo_trenes.get():
					datos.trenes[i] = entry_nombre.get()

		# button
		btn_guardar = tk.Button(frame_modificar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=3)

	def eliminar_tren(self):
		eliminar = tk.Toplevel()
		eliminar.title("Eliminar Tren")
		eliminar.resizable(False, False)
		label_bg = tk.Label(eliminar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_eliminar = tk.Frame(eliminar, padx=10, pady=10)
		frame_eliminar.pack(expand=True, padx=20, pady=20)

		# lista de trenes
		scrollbar = tk.Scrollbar(frame_eliminar)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		list_trenes = tk.Listbox(frame_eliminar, yscrollcommand=scrollbar.set)

		for tren in datos.trenes:
			list_trenes.insert(tk.END, tren)

		list_trenes.pack(side=tk.TOP, fill=tk.BOTH)
		scrollbar.config(command=list_trenes.yview)

		def cmd_eliminar():
			x = list_trenes.get(list_trenes.curselection())
			if x in datos.trenes:
				datos.trenes.remove(x)
			eliminar.destroy()
			self.eliminar_tren()

		# buttons
		btn_eliminar = tk.Button(frame_eliminar, text="Eliminar", command=cmd_eliminar)
		btn_eliminar.pack()

	def __init__(self):
		# super constructor
		tk.Toplevel.__init__(self)
		# configuracion ventana
		self.title("Gestionar Trenes")
		self.resizable(False, False)

		## crear label con imagen de fondo
		self.bg = tk.PhotoImage(file="bg.png")
		label_bg = tk.Label(self, image=self.bg)
		label_bg.place(x=-3, y=-3)

		# botones
		tk.Button(self, text='Ingresar Tren', command=self.ingresar_tren, padx=15, pady=10).grid(column=0, row=0, padx=70, pady=30)
		tk.Button(self, text='Modificar Tren', command=self.modificar_tren, padx=15, pady=10).grid(column=1, row=0, padx=70, pady=30)
		tk.Button(self, text='Eliminar Tren', command=self.eliminar_tren, padx=15, pady=10).grid(column=0, row=1, padx=70, pady=30)

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)