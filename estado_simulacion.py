import json
from datetime import datetime, timedelta
from copy import deepcopy
import random
import hashlib
from logica.estaciones import Estacion
from logica.ruta import Ruta
from logica.trenes import Tren
from logica.evento import Evento
from logica.eventos import TiposEvento
from logica.persona import Persona

class EstadoSimulacion:
    def __init__(self):
        self.resetear()
        self.nombre_simulacion = "simulacion_1"
        self.dia_actual = 0
        self.hora_actual = datetime(2015, 3, 1, 7, 0)  # 7 AM por defecto
        self.pausada = False
        self.lineas_temporales = []
        self.historial_estados = []  # <-- Asegúrate de inicializar esto
        self.inicializar_indicadores()
        self.cargar_datos_base()  # <-- Cargar datos base al iniciar

    def inicializar_indicadores(self):
        self.indicadores = {
            'ocupacion_promedio': 0.0,
            'retrasos_acumulados': 0,
            'personas_transportadas': 0,
            'incidentes': 0,
            'trenes_operativos': 0
        }

    def resetear(self):
        self.estaciones = []
        self.rutas = []
        self.trenes = []
        self.vias = []
        self.personas = []
        self.eventos = []
        self.historial_personas = []
        self.evento_actual = -1
        self.historial_estados = []  # <-- Asegúrate de reiniciar esto
        self.inicializar_indicadores()

    def cargar_datos_base(self):
        # Estaciones
        ec = Estacion(
            nombre="Estación Central (Santiago)",
            poblacion=8242459,
            vias=[{"destino": "Rancagua", "orientacion": "sur"}, {"destino": "Chillán", "orientacion": "sur"}],
            flujo_acumulado=0
        )
        ran = Estacion(
            nombre="Rancagua",
            poblacion=274407,
            vias=[{"destino": "Talca", "orientacion": "sur"}, {"destino": "Estación Central (Santiago)", "orientacion": "norte"}],
            flujo_acumulado=0
        )
        tal = Estacion(
            nombre="Talca",
            poblacion=242344,
            vias=[{"destino": "Chillán", "orientacion": "sur"}, {"destino": "Rancagua", "orientacion": "norte"}],
            flujo_acumulado=0
        )
        chi = Estacion(
            nombre="Chillán",
            poblacion=204091,
            vias=[{"destino": "Talca", "orientacion": "norte"}, {"destino": "Estación Central (Santiago)", "orientacion": "norte"}],
            flujo_acumulado=0
        )
        self.estaciones = [ec, ran, tal, chi]

        # Rutas
        self.rutas = [
            Ruta(origen=ec, destino=ran, longitud=87),
            Ruta(origen=ran, destino=tal, longitud=200),
            Ruta(origen=tal, destino=chi, longitud=180),
            Ruta(origen=chi, destino=ec, longitud=467),  # Suma de distancias para el retorno
        ]

        # Trenes
        self.trenes = [
            Tren(nombre="Tren BMU (Bimodal)", velocidad=160, vagones=[{"capacidad": 236}], flujo_acumulado=0, accion="detenido"),
            Tren(nombre="Tren EMU – EFE SUR", velocidad=120, vagones=[{"capacidad": 236}], flujo_acumulado=0, accion="detenido"),
        ]

        self.registrar_evento("Sistema iniciado con datos iniciales")

    def registrar_evento(self, nombre, descripcion="", fecha=None, afectado=None, tipo=None):
        evento = Evento(nombre, descripcion, fecha, afectado, tipo)
        self.eventos.append(evento)

    def avanzar_tiempo(self):
        if self.pausada:
            return
        # Avanza una hora
        self.hora_actual = self.hora_actual.replace(minute=0, second=0, microsecond=0)
        self.hora_actual += timedelta(hours=1)
        if self.hora_actual.hour > 20:  # 20:00 hrs fin de jornada
            self.hora_actual = self.hora_actual.replace(hour=7)
            self.dia_actual += 1

        self.generar_personas()
        self.mover_trenes()
        self.calcular_indicadores()
        self.registrar_evento(f"Avance de tiempo - Día {self.dia_actual} Hora {self.hora_actual.hour}:00")

        # Guarda snapshot del estado para retroceder
        self.historial_estados.append({
            'dia': self.dia_actual,
            'hora': self.hora_actual,
            'indicadores': deepcopy(self.indicadores)
        })

    def generar_personas(self):
        for estacion in self.estaciones:
            semilla = f"{estacion.nombre}{self.dia_actual}{self.hora_actual.hour}"
            hash_md5 = hashlib.md5(semilla.encode()).hexdigest()
            semilla_numerica = int(hash_md5, 16)
            random.seed(semilla_numerica)
            cantidad = max(0, int(random.gauss(50, 15)))
            for _ in range(cantidad):
                destino = random.choice([e for e in self.estaciones if e != estacion])
                persona = Persona(
                    id=len(self.personas)+1,
                    estacion_origen=estacion.nombre,
                    fecha_creacion=self.hora_actual,
                    estacion_destino=destino.nombre,
                    fecha_regreso=None  # Puedes agregar lógica para esto
                )
                self.personas.append(persona)

    def mover_trenes(self):
        for tren in self.trenes:
            # Ajusta según tu clase Tren
            if hasattr(tren, "accion") and tren.accion == "En ruta":
                # Lógica de movimiento determinista
                pass

    def pausar(self):
        self.pausada = not self.pausada
        self.registrar_evento(f"Simulación {'pausada' if self.pausada else 'reanudada'}")

    def retroceder_evento(self):
        if self.evento_actual > 0:
            self.evento_actual -= 1
            self.cargar_desde_evento(self.evento_actual)
            
    def cargar_desde_evento(self, index):
        """Carga estado desde un evento específico (RF07, RF09)"""
        if 0 <= index < len(self.eventos):
            snapshot = deepcopy(self.historial_estados[index])
            self.dia_actual = snapshot['dia']
            self.hora_actual = snapshot['hora']
            self.indicadores = snapshot['indicadores']
            self.evento_actual = index

    def crear_linea_temporal(self, nombre, evento_index):
        """Crea nueva línea temporal (RF09)"""
        nueva_linea = {
            "nombre": nombre,
            "evento_inicio": evento_index,
            "estado": deepcopy(self.historial_estados[evento_index])
        }
        self.lineas_temporales.append(nueva_linea)
        return nueva_linea

    def guardar_linea_temporal(self, nombre_archivo, linea_temporal):
        """Guarda línea temporal específica (RF08)"""
        with open(nombre_archivo, 'w') as f:
            json.dump(linea_temporal, f, indent=4)

    def avanzar_al_siguiente_evento(self):
        if not self.eventos:
            return
        self.eventos.sort(key=lambda e: e.fecha if e.fecha else 0)
        evento = self.eventos.pop(0)
        self.hora_actual = evento.fecha if evento.fecha else self.hora_actual
        self.procesar_evento(evento)

    def procesar_evento(self, evento):
        if evento.tipo == TiposEvento.TREN_PARTIO:
            # Lógica para cuando un tren parte
            pass
        elif evento.tipo == TiposEvento.TREN_LLEGO:
            # Lógica para cuando un tren llega
            pass
        elif evento.tipo == TiposEvento.SIMULACION_PAUSADA:
            # Lógica para pausar la simulación
            pass
        # ...otros tipos de eventos...

    def guardar_estado(self, archivo):
        # Ejemplo simple de guardado
        with open(archivo, 'w') as f:
            json.dump({
                "dia_actual": self.dia_actual,
                "hora_actual": self.hora_actual.isoformat(),
                # Agrega aquí lo que quieras guardar
            }, f, indent=4)

    def cargar_estado(self, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            self.dia_actual = data.get("dia_actual", 0)
            self.hora_actual = datetime.fromisoformat(data.get("hora_actual", "2015-03-01T07:00:00"))
            # Agrega aquí la lógica para restaurar el resto del estado

    # ...otros métodos según necesidades...
    # ...otros métodos según necesidades...
