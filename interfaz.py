import tkinter as tk
from tkinter import filedialog, messagebox

from logica.estaciones import *
from logica.ruta import *
from logica.trenes import *
from logica.evento import *  # <-- Importar eventos

from gestiones.gestor_estaciones import GestorEstaciones
from gestiones.gestor_rutas import GestorRutas
from gestiones.gestor_trenes import GestorTrenes
from gestiones.gestor_demanda import GestorDemanda
from gestiones.gestor_eventos import GestorEventos  # <-- Importar gestor de eventos

from estado_simulacion import EstadoSimulacion

# Crear instancia global del estado
estado = EstadoSimulacion()

def nueva_simulacion():
    global estado
    estado = EstadoSimulacion()  # Reinicia todo con datos base
    actualizar_estado()
    messagebox.showinfo("Nueva Simulación", "La simulación ha sido reiniciada con los datos predeterminados.")

root = tk.Tk()
root.title("Sistema de Simulación de Tráfico Ferroviario")
root.geometry("1022x574")
root.resizable(False, False)

# Imagen de fondo
try:
    bg = tk.PhotoImage(file="bg.png")
    tk.Label(root, image=bg).place(x=-3, y=-3)
except Exception:
    # Si no existe la imagen, continuar sin ella
    pass

# Cuadro decorativo: debe ir antes de usarlo para colocar widgets dentro
cuadro = tk.Frame(root, bg="#f0f0f0", width=350, height=420)
cuadro.place(x=610, y=50)

estado_label = tk.Label(cuadro, text="", bg="#f0f0f0", justify="left", anchor="nw", font=("Arial", 10))
estado_label.place(x=10, y=40)

label_dia = tk.Label(cuadro, text="Día:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_dia.place(x=10, y=10)

# Indicadores
indicador1_label = tk.Label(cuadro, text="Ocupación promedio: --%", bg="#f0f0f0", font=("Arial", 10))
indicador1_label.place(x=10, y=200)
indicador2_label = tk.Label(cuadro, text="Personas satisfechas: --%", bg="#f0f0f0", font=("Arial", 10))
indicador2_label.place(x=10, y=230)

def actualizar_estado():
    texto = (
        f"Estaciones: {len(estado.estaciones)}\n"
        f"Rutas: {len(estado.rutas)}\n"
        f"Trenes: {len(estado.trenes)}\n"
        f"Vías: {len(estado.vias)}\n"
        f"Personas: {len(estado.personas)}\n"
        f"Eventos: {len(estado.eventos)}"  # <-- Mostrar eventos
    )
    estado_label.config(text=texto)

def actualizar_indicadores():
    # Ejemplo simple, reemplaza con tu lógica real
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
        # Refresca automáticamente cada 2 segundos
        ventana.after(2000, refrescar)

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

def avanzar_evento():
    # Lógica para avanzar al siguiente evento
    if hasattr(estado, "avanzar_al_siguiente_evento"):
        estado.avanzar_al_siguiente_evento()
        actualizar_estado()
    else:
        messagebox.showinfo("Info", "Funcionalidad no implementada.")

def iniciar_pausar_simulacion():
    estado.pausada = not estado.pausada
    if estado.pausada:
        messagebox.showinfo("Simulación", "Simulación pausada.")
    else:
        messagebox.showinfo("Simulación", "Simulación en marcha.")
    actualizar_estado()

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
            # Si tienes atributos de tiempo estimado de llegada, muéstralos aquí
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

# Botones principales
tk.Button(root, text="Gestionar Estaciones", command=gestionar_estaciones, padx=15, pady=10).place(x=100, y=50)
tk.Button(root, text="Gestionar Rutas", command=gestionar_rutas, padx=28, pady=10).place(x=100, y=120)
tk.Button(root, text='Gestionar Trenes', command=gestionar_trenes, padx=27, pady=10).place(x=100, y=200)
tk.Button(root, text="Generación de Demanda", command=generar_demanda, padx=15, pady=10).place(x=350, y=50)
tk.Button(root, text="Gestionar Eventos", command=gestionar_eventos, padx=22, pady=10).place(x=100, y=280)
tk.Button(root, text="Nueva Simulación", command=nueva_simulacion, padx=20, pady=10, bg="#e0e0e0").place(x=100, y=350)
tk.Button(root, text="Ver Eventos", command=mostrar_eventos, padx=20, pady=10).place(x=350, y=350)
tk.Button(root, text="Iniciar/Pausar Simulación", command=iniciar_pausar_simulacion, padx=20, pady=10).place(x=100, y=410)  # <-- Botón iniciar/pausar
tk.Button(root, text="Ver Estado de Trenes", command=mostrar_estado_trenes, padx=20, pady=10).place(x=350, y=410)  # <-- Botón estado trenes

# Botones de simulación
tk.Button(root, text="Guardar Simulación", command=guardar_simulacion, padx=15, pady=10).place(x=820, y=480)
tk.Button(root, text="Cargar Simulación", command=cargar_simulacion, padx=15, pady=10).place(x=820, y=430)
tk.Button(root, text="Monitoreo", command=mostrar_monitoreo, padx=20, pady=10).place(x=350, y=120)
tk.Button(root, text="Avanzar al próximo evento", command=avanzar_evento, padx=10, pady=10).place(x=350, y=200)
actualizar_estado()  # Mostrar datos iniciales

root.mainloop()