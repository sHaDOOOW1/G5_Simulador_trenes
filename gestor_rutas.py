import tkinter as tk
from tkinter import ttk
import datos

class GestorRutas(tk.Toplevel):
	def ingresar_ruta(self):
		ingresar = tk.Toplevel()
		ingresar.title("Ingresar Ruta")
		ingresar.resizable(False, False)
		label_bg = tk.Label(ingresar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_ingresar = tk.Frame(ingresar, padx=10, pady=10)
		frame_ingresar.pack(expand=True, padx=20, pady=20)
		frame_id = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_id.grid(column=0, row=0)
		frame_origen = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_origen.grid(column=1, row=0)
		frame_destino = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_destino.grid(column=0, row=1)
		frame_longitud = tk.Frame(frame_ingresar, padx=20, pady=20)
		frame_longitud.grid(column=1, row=1)

		frame_ingresar.columnconfigure(0, weight=1)
		frame_ingresar.columnconfigure(1, weight=1)

		# labels
		label_id = tk.Label(frame_id, text="ID de la Ruta")
		label_id.pack()
		label_origen = tk.Label(frame_origen, text="Estacion de Origen")
		label_origen.pack()
		label_vias = tk.Label(frame_destino, text="Estacion de Destino")
		label_vias.pack()
		label_orientacion = tk.Label(frame_longitud, text="Longitud en Km")
		label_orientacion.pack()

		# entries
		entry_id = tk.Entry(frame_id)
		entry_id.pack()
		entry_longitud = tk.Entry(frame_longitud)
		entry_longitud.pack()

		# combo box
		combo_origen = ttk.Combobox(frame_origen, values=datos.rutas)
		combo_origen.pack()
		combo_destino = ttk.Combobox(frame_destino, values=datos.rutas)
		combo_destino.pack()

		def cmd_guardar():
			print(f"{entry_id.get()},{combo_origen.get()},{combo_destino.get()},{entry_longitud.get()}")
			if len(entry_id.get().strip()) != 0:
				datos.rutas.append(entry_id.get())

		# button
		btn_guardar = tk.Button(frame_ingresar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=2)

	def modificar_ruta(self):
		modificar = tk.Toplevel()
		modificar.title("Modificar Estacion")
		modificar.resizable(False, False)
		label_bg = tk.Label(modificar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_modificar = tk.Frame(modificar, padx=10, pady=10)
		frame_modificar.pack(expand=True, padx=20, pady=20)
		frame_id = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_id.grid(column=0, row=1)
		frame_origen = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_origen.grid(column=1, row=1)
		frame_destino = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_destino.grid(column=0, row=2)
		frame_longitud = tk.Frame(frame_modificar, padx=20, pady=20)
		frame_longitud.grid(column=1, row=2)

		# labels
		label_rutas = tk.Label(frame_modificar, text="Ruta a Modificar")
		label_rutas.grid(column=0, row=0)
		label_id = tk.Label(frame_id, text="ID de la Ruta")
		label_id.pack()
		label_origen = tk.Label(frame_origen, text="Estacion de Origen")
		label_origen.pack()
		label_vias = tk.Label(frame_destino, text="Estacion de Destino")
		label_vias.pack()
		label_orientacion = tk.Label(frame_longitud, text="Longitud en Km")
		label_orientacion.pack()

		# entries
		entry_id = tk.Entry(frame_id)
		entry_id.pack()
		entry_longitud = tk.Entry(frame_longitud)
		entry_longitud.pack()

		# poblar datos
		def select(event):
			ruta = combo_rutas.get()
			entry_id.delete(0, "end")
			entry_id.insert(0, ruta)
			combo_origen.set(ruta)
			combo_destino.set(ruta)
			entry_longitud.delete(0, 'end')
			entry_longitud.insert(0, ruta)

		# combo box
		combo_rutas = ttk.Combobox(frame_modificar, values=datos.rutas)
		combo_rutas.grid(column=1, row=0)
		combo_rutas.bind("<<ComboboxSelected>>", select)
		combo_origen = ttk.Combobox(frame_origen, values=datos.rutas)
		combo_origen.pack()
		combo_destino = ttk.Combobox(frame_destino, values=datos.rutas)
		combo_destino.pack()

		def cmd_guardar():
			print(f"{entry_id.get()},{combo_origen.get()},{combo_destino.get()},{entry_longitud.get()}")
			for i in range(len(datos.rutas)):
				if datos.rutas[i] == combo_rutas.get():
					datos.rutas[i] = entry_id.get()

		# button
		btn_guardar = tk.Button(frame_modificar, text="Guardar", command=cmd_guardar)
		btn_guardar.grid(column=1, row=3)

	def eliminar_ruta(self):
		eliminar = tk.Toplevel()
		eliminar.title("Eliminar Estacion")
		eliminar.resizable(False, False)
		label_bg = tk.Label(eliminar, image=self.bg)
		label_bg.place(x=-3, y=-3)

		#frames
		frame_eliminar = tk.Frame(eliminar, padx=10, pady=10)
		frame_eliminar.pack(expand=True, padx=20, pady=20)

		# lista de rutas
		scrollbar = tk.Scrollbar(frame_eliminar)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		list_rutas = tk.Listbox(frame_eliminar, yscrollcommand=scrollbar.set)

		for ruta in datos.rutas:
			list_rutas.insert(tk.END, ruta)
		    
		list_rutas.pack(side=tk.TOP, fill=tk.BOTH)
		scrollbar.config(command=list_rutas.yview)

		def cmd_eliminar():
			x = list_rutas.get(list_rutas.curselection())
			if x in datos.rutas:
				datos.rutas.remove(x)
			eliminar.destroy()
			self.eliminar_ruta()

		# buttons
		btn_eliminar = tk.Button(frame_eliminar, text="Eliminar", command=cmd_eliminar)
		btn_eliminar.pack()

	def __init__(self):
		# super constructor
		tk.Toplevel.__init__(self)
		# configuracion ventana
		self.title("Gestionar Rutas")
		self.resizable(False, False)

		## crear label con imagen de fondo
		self.bg = tk.PhotoImage(file="bg.png")
		label_bg = tk.Label(self, image=self.bg)
		label_bg.place(x=-3, y=-3)

		# botones
		tk.Button(self, text='Ingresar Rutas', command=self.ingresar_ruta, padx=15, pady=10).grid(column=0, row=0, padx=70, pady=30)
		tk.Button(self, text='Modificar Ruta', command=self.modificar_ruta, padx=15, pady=10).grid(column=1, row=0, padx=70, pady=30)
		tk.Button(self, text='Eliminar Ruta', command=self.eliminar_ruta, padx=15, pady=10).grid(column=0, row=1, padx=70, pady=30)

		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)