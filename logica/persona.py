class Persona:
    def __init__(self, id, estacion_origen, fecha_creacion, estacion_destino, fecha_regreso):
        self.id = id
        self.estacion_origen = estacion_origen
        self.fecha_creacion = fecha_creacion
        self.estacion_destino = estacion_destino
        self.fecha_regreso = fecha_regreso
        self.satisfecho = False  # Para indicadores
        self.estado = "en_origen"  # Puede ser: en_origen, transitando, en_destino

    def __str__(self):
        return f"Persona {self.id} ({self.estacion_origen} → {self.estacion_destino})"
