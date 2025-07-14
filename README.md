##Simulador de Tráfico Ferroviario
-Descripción
Este simulador permite modelar, analizar y visualizar el tráfico ferroviario entre estaciones reales de Chile, gestionando rutas, trenes, vías y demanda de pasajeros. La simulación está basada en eventos y permite experimentar con diferentes configuraciones a través de una interfaz gráfica.

##Características principales
-Administración completa: Permite crear, modificar y eliminar Estaciones, Rutas, Trenes y Vías.

-Datos iniciales reales: Al iniciar una nueva simulación, se cargan los datos base del Anexo 01 (Estación Central, Rancagua, Talca, Chillán, trenes BMU y EMU).

-Generación de demanda: Permite simular demanda de pasajeros de forma controlada desde la interfaz.

-Gestión de eventos: El sistema mantiene y muestra eventos ocurridos (como generación de demanda o acciones simuladas).

-Indicadores clave: Muestra en la interfaz ocupación promedio de trenes y porcentaje de personas satisfechas.

-Persistencia: Permite guardar y cargar simulaciones desde la interfaz en formato JSON.

-Interfaz gráfica: Control completo de la simulación mediante una GUI intuitiva y accesible.

##Indicadores implementados
-Ocupación promedio de trenes:
   Muestra el porcentaje promedio de ocupación de los trenes activos.

-Personas satisfechas:
   Muestra el porcentaje de personas que han completado exitosamente su viaje.

Ambos indicadores se actualizan en tiempo real y se muestran en la interfaz principal.

#Determinismo
Actualmente, la generación de demanda no incluye control explícito de semilla, por lo que puede considerarse pseudoaleatoria. Se puede adaptar fácilmente para ser determinista en futuras versiones, usando una semilla basada en parámetros del estado.

#Cómo usar
Ejecuta interfaz.py.

Usa los botones para gestionar estaciones, rutas, trenes, demanda y eventos.

Puedes pausar/iniciar la simulación, avanzar eventos, ver el monitoreo y el estado de los trenes en tiempo real.

Guarda y carga simulaciones desde la interfaz.

Usa "Nueva Simulación" para restaurar los datos base del sistema.

Documentación de entidades y eventos
Estación: Nombre, población, vías, flujo acumulado.

Ruta: Origen, destino, longitud.

Tren: Nombre, velocidad, vagones (capacidad), flujo acumulado, acción actual.

Persona: ID, estación origen, estación destino, estado, satisfecho.

Evento: Nombre, descripción, fecha (ver logica/evento.py).

#Robustez y restricciones
-El sistema impide algunas acciones inválidas (por ejemplo, trenes con sobreocupación).

-La interfaz maneja errores comunes del usuario mediante mensajes claros.

-La simulación puede ser pausada y reanudada.

#Decisiones de diseño
-La arquitectura permite extender fácilmente atributos y tipos de entidades.

-Se priorizó una interfaz simple, con botones visibles para cada acción relevante.

-Los datos pueden ser guardados y cargados sin perder el estado actual de la simulación.

#Limitaciones actuales
-No es posible retroceder en la línea de eventos.

-No se permite modificar la función de generación de demanda desde la GUI.

-La lógica de movimiento de trenes aún no se encuentra completamente implementada.

-La generación de personas no es determinista (aunque puede adaptarse fácilmente).





