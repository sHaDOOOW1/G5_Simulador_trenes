import tkinter as tk
from tkinter import filedialog, messagebox

from logica.estaciones import *
from logica.ruta import *
from logica.trenes import *
from logica.evento import *  

from gestiones.gestor_estaciones import GestorEstaciones
from gestiones.gestor_rutas import GestorRutas
from gestiones.gestor_trenes import GestorTrenes
from gestiones.gestor_demanda import GestorDemanda
from gestiones.gestor_eventos import GestorEventos 

from estado_simulacion import EstadoSimulacion

estado = EstadoSimulacion() #crea instancia global del estado

def nueva_simulacion():
    global estado
    estado = EstadoSimulacion()  #reinicia todo con la informacion de datos base
    actualizar_estado()
    messagebox.showinfo("Nueva Simulación", "La simulación ha sido reiniciada con los datos predeterminados.")

root = tk.Tk()
root.title("Sistema de Simulación de Tráfico Ferroviario")
root.geometry("1022x574")
root.resizable(False, False)

try:
    bg = tk.PhotoImage(file="bg.png") #img fondo
    tk.Label(root, image=bg).place(x=-3, y=-3)
except Exception:
    pass #si no existe la imagen continua 

cuadro = tk.Frame(root, bg="#f0f0f0", width=350, height=420)
cuadro.place(x=610, y=50)
estado_label = tk.Label(cuadro, text="", bg="#f0f0f0", justify="left", anchor="nw", font=("Arial", 10))
estado_label.place(x=10, y=40)
label_dia = tk.Label(cuadro, text="Día:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_dia.place(x=10, y=10)
label_fecha = tk.Label(cuadro, text="", bg="#f0f0f0", font=("Arial", 12))
label_fecha.place(x=60, y=10)
label_hora1 = tk.Label(cuadro, text="Hora:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_hora1.place(x=210, y=10)
label_hora2 = tk.Label(cuadro, text="", bg="#f0f0f0", font=("Arial", 12))
label_hora2.place(x=260, y=10)

#indicadores
indicador1_label = tk.Label(cuadro, text="Ocupación promedio: --%", bg="#f0f0f0", font=("Arial", 11))
indicador1_label.place(x=10, y=200)
indicador2_label = tk.Label(cuadro, text="Personas satisfechas: --%", bg="#f0f0f0", font=("Arial", 11))
indicador2_label.place(x=10, y=230)

def actualizar_estado():
    texto = (
        f"Estaciones: {len(estado.estaciones)}\n"
        f"Rutas: {len(estado.rutas)}\n"
        f"Trenes: {len(estado.trenes)}\n"
        f"Vías: {len(estado.vias)}\n"
        f"Personas: {len(estado.personas)}\n"
        f"Eventos: {len(estado.eventos)}"  
    )
    estado_label.config(text=texto)
    actualizar_fecha_y_hora()

def actualizar_fecha_y_hora():
    fecha = estado.hora_actual.strftime("%d/%m/%Y")
    hora = estado.hora_actual.strftime("%H:%M")
    label_fecha.config(text=fecha)
    label_hora2.config(text=hora)

def actualizar_indicadores():
    try:
        ocupacion = sum([t.ocupacion for t in estado.trenes]) / len(estado.trenes)
        satisfechos = len([p for p in estado.personas if p.satisfecho]) / len(estado.personas) * 100
        indicador1_label.config(text=f"Ocupación promedio: {ocupacion:.1f}%")
        indicador2_label.config(text=f"Personas satisfechas: {satisfechos:.1f}%")
    except Exception:
        indicador1_label.config(text="Ocupación promedio: --%")
        indicador2_label.config(text="Personas satisfechas: --%")

def mostrar_monitoreo():
    import tkinter as tk

    ventana = tk.Toplevel()
    ventana.title("Monitoreo de la Simulación")
    ventana.geometry("600x500")

    texto = tk.Text(ventana, wrap='word')
    texto.pack(expand=True, fill='both')

    def refrescar():
        texto.config(state='normal')
        texto.delete('1.0', tk.END)
        info = (
            f"Estaciones ({len(estado.estaciones)}):\n" +
            "\n".join([f"- {e.nombre}" for e in estado.estaciones]) +
            "\n\n"
            f"Rutas ({len(estado.rutas)}):\n" +
            "\n".join([f"- {r.nombre}" for r in estado.rutas]) +
            "\n\n"
            f"Trenes ({len(estado.trenes)}):\n" +
            "\n".join([f"- {t.nombre}" for t in estado.trenes]) +
            "\n\n"
            f"Personas en demanda: {len(estado.personas)}\n"
            "\n"
            "Eventos recientes:\n" +
            "\n".join([
                f"- [{getattr(ev, 'fecha', '')}] {getattr(ev, 'nombre', '')}: {getattr(ev, 'descripcion', '')}"
                for ev in estado.eventos[-10:]
            ])
        )
        texto.insert('1.0', info)
        texto.config(state='disabled')
        ventana.after(2000, refrescar) #refresca automáticamente cada 2 segundos

    btn_actualizar = tk.Button(ventana, text="Actualizar", command=refrescar)
    btn_actualizar.pack(pady=5)

    refrescar()

def mostrar_eventos():
    ventana = tk.Toplevel()
    ventana.title("Eventos de la Simulación")
    ventana.geometry("700x400")

    texto = tk.Text(ventana, wrap='word')
    texto.pack(expand=True, fill='both')

    def refrescar():
        texto.config(state='normal')
        texto.delete('1.0', tk.END)
        info = "Lista de eventos registrados:\n\n"
        for ev in estado.eventos:
            info += f"- [{getattr(ev, 'fecha', '')}] {getattr(ev, 'nombre', '')}: {getattr(ev, 'descripcion', '')}\n"
        texto.insert('1.0', info)
        texto.config(state='disabled')

    btn_actualizar = tk.Button(ventana, text="Actualizar", command=refrescar)
    btn_actualizar.pack(pady=5)

    refrescar()

def gestionar_estaciones():
    GestorEstaciones()
    actualizar_estado()

def gestionar_rutas():
    GestorRutas()
    actualizar_estado()

def gestionar_trenes():
    GestorTrenes()
    actualizar_estado()

def generar_demanda():
    GestorDemanda()
    actualizar_estado()

def gestionar_eventos():
    GestorEventos()
    actualizar_estado()

def guardar_simulacion():
    archivo = filedialog.asksaveasfilename(defaultextension=".json",
                                           filetypes=[("Archivos JSON", "*.json")],
                                           title="Guardar Simulación")
    if archivo:
        try:
            estado.guardar_estado(archivo)
            messagebox.showinfo("Éxito", "Simulación guardada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")
        actualizar_estado()     

def cargar_simulacion():
    archivo = filedialog.askopenfilename(defaultextension=".json",
                                         filetypes=[("Archivos JSON", "*.json")],
                                         title="Cargar Simulación")
    if archivo:
        try:
            estado.cargar_estado(archivo)
            messagebox.showinfo("Éxito", "Simulación cargada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar: {e}")
        actualizar_estado()

def avanzar_evento():#lógica para el siguiente evento
    if hasattr(estado, "avanzar_al_siguiente_evento"):
        estado.avanzar_al_siguiente_evento()
        actualizar_estado()
    else:
        messagebox.showinfo("Info", "Funcionalidad no implementada.")

def iniciar_simulacion():
    if estado.pausada:
        estado.pausada = False
        estado.registrar_evento("Simulación reanudada")
        messagebox.showinfo("Simulación", "La simulación ya esta iniciada")
        actualizar_estado()
    else:
        messagebox.showinfo("Simulación", "Simulación iniciada")

def pausar_simulacion():
    if not estado.pausada:
        estado.pausada = True
        estado.registrar_evento("Simulación pausada")
        messagebox.showinfo("Simulación", "Simulación pausada")
        actualizar_estado()
    else:
        messagebox.showinfo("Simulación", "La simulación ya está pausada")

def mostrar_estado_trenes():
    ventana = tk.Toplevel()
    ventana.title("Estado de Trenes en Tiempo Real")
    ventana.geometry("600x400")

    texto = tk.Text(ventana, wrap='word')
    texto.pack(expand=True, fill='both')

    def refrescar():
        texto.config(state='normal')
        texto.delete('1.0', tk.END)
        info = "Estado actual de los trenes:\n\n"
        for tren in estado.trenes:
            nombre = getattr(tren, "nombre", "")
            accion = getattr(tren, "accion", "desconocido")
            llegada = getattr(tren, "tiempo_llegada", "N/A")
            info += f"- {nombre}: {accion}"
            if accion == "En ruta":
                info += f" | Tiempo estimado de llegada: {llegada}"
            info += "\n"
        texto.insert('1.0', info)
        texto.config(state='disabled')

    btn_actualizar = tk.Button(ventana, text="Actualizar", command=refrescar)
    btn_actualizar.pack(pady=5)
    refrescar()

#botones principales
tk.Button(root, text="Iniciar Simulación", command=iniciar_simulacion, padx=15, pady=10).place(x=100, y=50) 
tk.Button(root, text="Pausar Simulación", command=pausar_simulacion, padx=20, pady=10).place(x=260, y=50) 
tk.Button(root, text="Nueva Simulación", command=nueva_simulacion, padx=20, pady=10, bg="#e0e0e0").place(x=430, y=50)
tk.Button(root, text="Gestionar Estaciones", command=gestionar_estaciones, padx=20, pady=10).place(x=100, y=150)
tk.Button(root, text="Gestionar Rutas", command=gestionar_rutas, padx=28, pady=10).place(x=100, y=210)
tk.Button(root, text='Gestionar Trenes', command=gestionar_trenes, padx=27, pady=10).place(x=105, y=270)
tk.Button(root, text="Gestionar Eventos", command=gestionar_eventos, padx=22, pady=10).place(x=100, y=340)
tk.Button(root, text="Monitoreo", command=mostrar_monitoreo, padx=20, pady=10).place(x=350, y=150) #botones de simulación
tk.Button(root, text="Generación de Demanda", command=generar_demanda, padx=15, pady=10).place(x=350, y=210)
tk.Button(root, text="Ver Estado de Trenes", command=mostrar_estado_trenes, padx=20, pady=10).place(x=350, y=270)  #estado trenes
tk.Button(root, text="Ver Eventos", command=mostrar_eventos, padx=20, pady=10).place(x=350, y=340)
tk.Button(root, text="Avanzar al próximo evento", command=avanzar_evento, padx=10, pady=10).place(x=350, y=400) #botones de simulación
tk.Button(root, text="Guardar Simulación", command=guardar_simulacion, padx=15, pady=10).place(x=820, y=480) #botones de simulación
tk.Button(root, text="Cargar Simulación", command=cargar_simulacion, padx=15, pady=10).place(x=820, y=430) #botones de simulación
actualizar_estado()  #muestra los datos iniciales

root.mainloop()