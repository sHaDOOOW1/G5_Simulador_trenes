from enum import Enum

class TiposEvento(Enum):
    # Eventos del sistema
    SIMULACION_INICIADA = "simulacion_iniciada"
    SIMULACION_PAUSADA = "simulacion_pausada"
    DIA_AVANZADO = "dia_avanzado"
    
    # Eventos de trenes
    TREN_PARTIO = "tren_partio"
    TREN_LLEGO = "tren_llego"
    TREN_RETRASADO = "tren_retrasado"
    
    # Eventos de estaciones
    ESTACION_ABARROTADA = "estacion_abarrotada"
    PERSONAS_ACUMULADAS = "personas_acumuladas"
    
    # Eventos especiales
    INCIDENTE = "incidente"
    MANTENIMIENTO = "mantenimiento"

class GeneradorEventos:
    @staticmethod
    def tren_partio(tren, estacion, fecha):
        from logica.evento import Evento
        return Evento(
            nombre="Tren partió",
            descripcion=f"Tren {tren.nombre} partió de {estacion.nombre}",
            fecha=fecha,
            afectado=tren,
            tipo=TiposEvento.TREN_PARTIO
        )

    @staticmethod
    def tren_retrasado(tren, minutos_retraso, motivo, fecha):
        from logica.evento import Evento
        return Evento(
            nombre="Tren retrasado",
            descripcion=f"Tren {tren.nombre} retrasado {minutos_retraso} min: {motivo}",
            fecha=fecha,
            afectado=tren,
            tipo=TiposEvento.TREN_RETRASADO
        )
    # ...puedes agregar más métodos similares para otros eventos...
 
    