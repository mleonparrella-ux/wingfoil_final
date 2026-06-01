# wingfoil_final

Qué problema, experiencia o funcionalidad quiere desarrollar el grupo:

  Sistema para registrar sesiones de wingfoil y recibir recomendaciones de equipo basadas en el historial personal del deportista. El programa aprende de las sesiones pasadas y sugiere qué equipo usar según las condiciones del día


Quién sería el usuario del programa:
  
  Deportistas de wingfoil de cualquier nivel que quieran llevar un registro de sus sesiones y recibir recomendaciones personalizadas basadas en su experiencia propia.

Qué podrá hacer el usuario al interactuar con el sistema 
  
  Registrar cada sesión con: fecha, duración, ubicación, velocidad del viento, dirección del viento, condición del agua, equipo usado (wing, tabla, foil) y sensación (1-10)
  Ingresar las condiciones del día (viento, dirección, ubicación, condición del agua) y recibir una recomendación de equipo basada en sesiones similares del historial
  Ver estadísticas generales: días navegados, duración promedio, condiciones más frecuentes
  Ver con qué equipo tuvo mejores sensaciones según las condiciones


Qué información recibirá, procesará, generará o mostrará el programa

  Recibirá: datos de cada sesión ingresados por el usuario y condiciones del día para la recomendación
  Procesará: búsqueda de sesiones similares en el historial, promedios de sensación por equipo y condición
  Mostrará: recomendación de equipo, sensación promedio esperada y resumen de sesiones similares

Qué resultados, salidas o funcionalidades principales tendrá 

  Registro histórico de sesiones guardado en CSV
  Sistema de recomendación de equipo basado en condiciones similares del historial
  Estadísticas de progreso a lo largo del tiempo
  Consulta automática de viento y dirección según ubicación via API

Qué librerías y/o tecnologías usarán para el desarrollo del programa.

  Python
  API de clima (OpenWeatherMap) para obtener velocidad y dirección del viento automáticamente según la ubicación
