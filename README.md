# Simulador de Tráfico Ferroviario

## Descripción
Este simulador permite modelar, analizar y optimizar el tráfico ferroviario entre estaciones reales de Chile, gestionando rutas, trenes, vías y demanda de pasajeros. La simulación es determinista, basada en eventos, y permite experimentar con diferentes configuraciones y escenarios.

## Características principales

- **Administración completa:** Permite crear, modificar y eliminar Estaciones, Rutas, Trenes y Vías.
- **Datos iniciales reales:** Al iniciar una nueva simulación, se cargan los datos base del Anexo 01 (Estación Central, Rancagua, Talca, Chillán, trenes BMU y EMU).
- **Generación de demanda:** Implementa dos funciones de generación de demanda, seleccionables por estación y modificables durante la simulación.
- **Determinismo:** La generación de personas es determinista, usando una semilla basada en el estado, garantizando reproducibilidad.
- **Gestión de eventos:** El sistema mantiene y muestra todos los eventos ocurridos (movimiento de trenes, generación de demanda, etc.).
- **Indicadores clave:** Muestra indicadores como ocupación promedio de trenes y porcentaje de personas satisfechas en la interfaz.
- **Persistencia:** Permite guardar y cargar simulaciones, incluyendo múltiples líneas de tiempo.
- **Interfaz gráfica:** Control total de la simulación mediante una GUI intuitiva.

## Indicadores implementados

1. **Ocupación promedio de trenes:**  
   Muestra el porcentaje promedio de ocupación de todos los trenes activos en la simulación.

2. **Personas satisfechas:**  
   Muestra el porcentaje de personas que han completado exitosamente su viaje.

Ambos indicadores se muestran en la interfaz principal y se actualizan en tiempo real.

## Determinismo

- La generación de personas y eventos es completamente determinista:  
  - Se utiliza una semilla basada en el nombre de la estación, día y hora para la generación de demanda.
  - Mismos datos de entrada y configuración producen siempre los mismos resultados.

## Cómo usar

1. Ejecuta `interfaz.py`.
2. Usa los botones para gestionar estaciones, rutas, trenes, demanda y eventos.
3. Puedes pausar/iniciar la simulación, avanzar eventos, ver el monitoreo y el estado de los trenes en tiempo real.
4. Guarda y carga simulaciones desde la interfaz.
5. Usa "Nueva Simulación" para restaurar los datos base del anexo.

## Documentación de entidades y eventos

- **Estación:** Nombre, población, vías, flujo acumulado.
- **Ruta:** Origen, destino, longitud.
- **Tren:** Nombre, velocidad, vagones (capacidad), flujo acumulado, acción actual.
- **Persona:** ID, estación origen, fecha creación, estación destino, fecha regreso, estado, satisfecho.
- **Evento:** Nombre, descripción, fecha, afectado, tipo (ver `logica/eventos.py`).

## Robustez y restricciones

- El sistema impide acciones inválidas (por ejemplo, trenes sobrecargados o en vías ocupadas).
- Las estaciones cuentan con al menos una vía de rotación.
- Se respeta el horario de funcionamiento (7:00-20:00).
- La interfaz maneja errores de usuario y muestra mensajes claros.

## Decisiones de diseño

- Los atributos de trenes, estaciones y personas se pueden extender fácilmente.
- El sistema está preparado para agregar nuevas rutas, trenes o estaciones.
- La lógica de eventos permite pausar, retroceder y crear líneas temporales alternativas.

## Validación de determinismo y líneas de tiempo

- Puedes volver a cualquier evento anterior y crear una nueva línea temporal desde ese punto.
- El sistema garantiza que, si no se modifican parámetros, la simulación es siempre reproducible.



