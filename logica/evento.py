from logica.eventos import TiposEvento

class Evento:
    def __init__(self, nombre, descripcion="", fecha=None, afectado=None, tipo=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.afectado = afectado  # Puede ser un tren, estación, ruta, etc.
        self.estado = "activo"
        self.tipo = tipo  # Tipo de evento (usando TiposEvento)
        # ...otros atributos y métodos según tu lógica...
