

import random  # ¡Falta esta línea crucial!
from datetime import datetime, timedelta

class GeneradorDemanda:
    def __init__(self, estaciones, semilla=None):
        self.estaciones = estaciones
        self.semilla = semilla or random.randint(1, 1000)  # Necesita el módulo random
        random.seed(self.semilla)
        self.personas = []
class GeneradorDemanda:
    def __init__(self, estaciones, semilla=None):
        """
        estaciones: Diccionario {nombre: [poblacion, ...]} 
                   o lista de nombres de estaciones
        """
        self.estaciones = estaciones if isinstance(estaciones, dict) else \
                         {nombre: [10000] for nombre in estaciones}  # Valor por defecto
        self.semilla = semilla or random.randint(1, 1000)
        random.seed(self.semilla)
        self.personas = []

    def _get_poblacion(self, datos_estacion):
        """Obtiene población de datos de estación"""
        return int(datos_estacion[0]) if datos_estacion else 10000  # Valor por defecto

    def generar_aleatoria(self, hora_inicio, duracion_horas):
        for nombre, datos in self.estaciones.items():
            poblacion = self._get_poblacion(datos)
            cantidad = int(poblacion * 0.20)
            
            for i in range(cantidad):
                minutos = random.randint(0, duracion_horas * 60)
                self.personas.append({
                    'id': f"{nombre}-{i}-{self.semilla}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones if e != nombre]),
                    'hora': hora_inicio + timedelta(minutes=minutos),
                    'tipo': 'normal'
                })

    def generar_finde_largo(self, hora_inicio, duracion_horas):
        for nombre, datos in self.estaciones.items():
            poblacion = self._get_poblacion(datos)
            cantidad = int(poblacion * 0.25)
            
            for i in range(cantidad):
                hora = max(6, min(20, int(random.normalvariate(12, 3))))
                minutos = random.randint(0, 59)
                self.personas.append({
                    'id': f"{nombre}-FL-{i}-{self.semilla}",
                    'origen': nombre,
                    'destino': random.choice([e for e in self.estaciones if e != nombre]),
                    'hora': hora_inicio + timedelta(hours=hora, minutes=minutos),
                    'tipo': 'finde_largo'
                })