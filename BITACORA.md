# BITACORA.md -- Tablero Kanban Personal

### 1. Estado actual
- Pasos ejecutados: 13 de 15.
- Paso en curso: ninguno.
- Última actualización: 2026-05-11 20:00.
- Rama de trabajo: main.

## 2. Plan original
(Plan detallado en PLAN_ATOMICO.md)

## 3. Pasos ejecutados

### Paso 1 - Preparar paquetes Python y archivos __init__.py
- Fecha: 2026-05-10 21:50
- Archivos modificados: `src/__init__.py`, `src/dominio/__init__.py`, `src/aplicacion/__init__.py`, `src/infraestructura/__init__.py`, `src/infraestructura/persistencia/__init__.py`, `src/infraestructura/http/__init__.py`
- Validación ejecutada: `Get-ChildItem -Filter __init__.py -Recurse .\src`
- Resultado: OK
- Commit: `2d383aa`
- Observación técnica breve: Se inicializaron los paquetes de la arquitectura hexagonal para habilitar importaciones.

### Paso 2 - Crear EstadoTarea y Tarea
- Fecha: 2026-05-10 21:55
- Archivos modificados: `src/dominio/estado_tarea.py`, `src/dominio/tarea.py`
- Validación ejecutada: `python -c "from src.dominio.tarea import Tarea; t = Tarea(' Mi primera tarea '); print(t.titulo)"`
- Resultado: OK
- Commit: `2d383aa`
- Observación técnica breve: Creación de la entidad Tarea y el enumerado EstadoTarea con validación inicial de título (INV-04).

### Paso 3 - Crear errores de dominio
- Fecha: 2026-05-10 21:56
- Archivos modificados: `src/dominio/errores.py`, `src/dominio/tarea.py`
- Validación ejecutada: `python -c "from src.dominio.tarea import Tarea; Tarea('')"`
- Resultado: OK
- Commit: `2d383aa`
- Observación técnica breve: Implementación de excepciones específicas del dominio y refactorización de Tarea para usarlas.

### Paso 4 - Crear Tablero y operación crear_tarea
- Fecha: 2026-05-10 22:04
- Archivos modificados: `src/dominio/tablero.py`
- Validación ejecutada: `python -c "from src.dominio.tablero import Tablero; t = Tablero(); t.crear_tarea('Prueba'); print(t.tareas[0].titulo)"`
- Resultado: OK
- Commit: `e59c220`
- Observación técnica breve: Creación de la entidad Tablero como aggregate root y método crear_tarea (INV-04, FEATURE_SPEC_001).

### Paso 5 - Implementar movimiento y transiciones
- Fecha: 2026-05-10 22:07
- Archivos modificados: `src/dominio/tablero.py`
- Validación ejecutada: `python -c "from src.dominio.tablero import Tablero; from src.dominio.estado_tarea import EstadoTarea; t = Tablero(); tarea = t.crear_tarea('Test'); t.mover_tarea(tarea.id_tarea, EstadoTarea.DOING); print(t.tareas[0].estado)"`
- Resultado: OK
- Commit: `e59c220`
- Observación técnica breve: Implementación de mover_tarea en Tablero con validación de transiciones de estado (INV-03, FEATURE_SPEC_002).

### Paso 6 - Proteger límite WIP y atomicidad
- Fecha: 2026-05-10 22:15
- Archivos modificados: `src/dominio/tablero.py`
- Validación ejecutada: Script en Python comprobando que una cuarta tarea al pasar a DOING lanza `ErrorLimiteWipExcedido`.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Implementación de la validación del límite WIP en `mover_tarea`, asegurando la atomicidad al no mutar el estado antes de validar (INV-01, INV-02, INV-05).

### Paso 7 - Crear puerto RepositorioTablero
- Fecha: 2026-05-10 22:19
- Archivos modificados: `src/aplicacion/repositorio_tablero.py`
- Validación ejecutada: `python -c "from src.aplicacion.repositorio_tablero import RepositorioTablero; print(RepositorioTablero.__abstractmethods__)"`
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Creación de la interfaz `RepositorioTablero` en la capa de aplicación usando `abc.ABC` según lo definido en `ARCHITECTURE.md`.

### Paso 8 - Crear caso de uso CrearTarea
- Fecha: 2026-05-10 22:24
- Archivos modificados: `src/aplicacion/crear_tarea.py`
- Validación ejecutada: Script en Python con un repositorio mock para comprobar el ciclo `cargar` -> `crear_tarea` -> `guardar`.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Implementación de la orquestación en la capa de aplicación, delegando reglas de negocio al dominio y persistencia al puerto (AC-01, AC-04).

### Paso 9 - Crear caso de uso MoverTarea
- Fecha: 2026-05-10 22:30
- Archivos modificados: `src/aplicacion/mover_tarea.py`
- Validación ejecutada: Script con MockRepositorio verificando el flujo cargar -> mover -> guardar.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Se implementó el caso de uso para mover tareas, asegurando que la persistencia se actualice únicamente si la lógica de dominio permite la transición.

### Paso 10 - Crear caso de uso ObtenerTablero
- Fecha: 2026-05-10 22:33
- Archivos modificados: `src/dominio/tablero.py`, `src/aplicacion/obtener_tablero.py`
- Validación ejecutada: Script simulando la carga del tablero e imprimiendo la salida JSON agrupada por las columnas TODO, DOING y DONE.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Implementación de la agrupación y serialización de tareas en el aggregate root, y el caso de uso de solo lectura que orquesta la consulta (AC-01, AC-02, AC-03).

### Paso 11 - Implementar repositorio JSON
- Fecha: 2026-05-10 22:36
- Archivos modificados: `src/infraestructura/persistencia/repositorio_json.py`
- Validación ejecutada: Script simulando un caso de uso con persistencia real hacia archivo `test_tablero.json`.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Implementación concreta de `RepositorioTablero` en la capa de infraestructura usando el módulo `json`. Maneja correctamente la inicialización de tableros vacíos y serializa/deserializa entidades del dominio.

### Paso 12 - Crear adaptador HTTP Flask
- Fecha: 2026-05-10 22:45
- Archivos modificados: `src/infraestructura/http/api.py`
- Validación ejecutada: `python -m py_compile src/infraestructura/http/api.py`
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Creación del adaptador primario HTTP exponiendo rutas GET, POST y PUT, inyectando el RepositorioJSON a los casos de uso y traduciendo excepciones de dominio (`ErrorDominio`) a códigos HTTP 400.

### Paso 13 - Crear frontend HTML/CSS/JS
- Fecha: 2026-05-10 22:50
- Archivos modificados: `src/infraestructura/frontend/index.html`, `src/infraestructura/frontend/style.css`, `src/infraestructura/frontend/app.js`, `src/infraestructura/http/api.py`
- Validación ejecutada: Verificación manual de la sintaxis y ejecución del servidor de desarrollo con `python src/infraestructura/http/api.py`.
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Creación de la interfaz de usuario en Vanilla JS, HTML5 y CSS3. Se actualizó el adaptador HTTP (Flask) para servir estos archivos estáticos en la ruta raíz (`/`).

### Paso 14 - Agregar pruebas y validaciones finales
- Fecha: 2026-05-11 20:00
- Archivos modificados: `tests/conftest.py`, `tests/test_crear_tarea.py`, `tests/test_mover_tarea.py`, `tests/test_obtener_tablero.py`
- Validación ejecutada: `python -m pytest tests/`
- Resultado: OK
- Commit: pendiente
- Observación técnica breve: Se implementaron pruebas automatizadas validando todos los criterios de aceptación (AC) para crear, mover y obtener tareas usando un MockRepositorio.

## 4. Pasos pendientes
- [x] Paso 12 - Crear adaptador HTTP Flask
- [x] Paso 13 - Crear frontend HTML/CSS/JS
- [x] Paso 14 - Agregar pruebas y validaciones finales
- [ ] Paso 15 - Actualizar README y cerrar BITACORA.md

## 5. Decisiones tomadas

### DEC-01 (Paso 2) - Uso de ValueError como placeholder
- Decisión: Implementar validación de INV-04 usando `ValueError` temporalmente.
- Justificación: El paso CAM-03 (Crear errores de dominio) aún no se había ejecutado y se requería validar la invariante de inmediato.
- Impacto: Refactorización realizada exitosamente en el Paso 3.

### DEC-02 (Paso 3) - Jerarquía de errores de dominio
- Decisión: Crear `ErrorDominio` como clase base para todas las excepciones del tablero.
- Justificación: Facilita el manejo de errores en las capas externas (Aplicación/Infraestructura) permitiendo capturar cualquier fallo de lógica de negocio de forma genérica.
- Impacto: Mejora la limpieza de los bloques try/except en adaptadores futuros.

### DEC-03 (Paso 4) - Tablero como Aggregate Root
- Decisión: La clase `Tablero` maneja la lista de tareas en memoria mediante el atributo `tareas` de tipo `List[Tarea]`.
- Justificación: Representar la relación como una lista facilita la implementación en memoria y la iteración para realizar validaciones o búsquedas, alineándose con el concepto de aggregate root.
- Impacto: Define la estructura que se usará para serializar en el repositorio JSON (Paso 11).

### DEC-04 (Paso 5) - Control de invariantes en Aggregate Root
- Decisión: Validar las transiciones de estado directamente en el método `mover_tarea` del `Tablero` en lugar de la entidad `Tarea`.
- Justificación: Siguiendo las directrices de DOMAIN.md, el `Tablero` como aggregate root debe proteger las invariantes y controlar todos los cambios sobre sus entidades internas.
- Impacto: Mantiene la lógica de orquestación de tareas fuertemente cohesiva dentro del Tablero.

### DEC-05 (Paso 7) - Uso de ABC para puerto RepositorioTablero
- Decisión: Utilizar `abc.ABC` y `@abstractmethod` de Python para definir la interfaz abstracta de persistencia en la capa de aplicación.
- Justificación: Al no contar con interfaces nativas en Python, el módulo `abc` proporciona seguridad al fallar tempranamente (en tiempo de instanciación) si los adaptadores de infraestructura omiten implementar métodos del puerto.
- Impacto: Garantiza cumplimiento estricto del contrato por parte del repositorio JSON que se construirá en el Paso 11.

### DEC-06 (Paso 9) - Orquestación del cambio de estado
- Decisión: El caso de uso `MoverTarea` delega toda la lógica de validación al aggregate root `Tablero`.
- Justificación: Mantiene la lógica de negocio centralizada en el dominio y asegura que la persistencia solo ocurra si la transición es válida.
- Impacto: El caso de uso es simple y enfocado en la orquestación (cargar -> ejecutar dominio -> guardar).

### DEC-08 (Paso 10) - Serialización agrupada en el Aggregate Root
- Decisión: Ubicar la lógica de agrupación por estados (TODO, DOING, DONE) y serialización a diccionarios en el método `obtener_tareas_por_estado` dentro de `Tablero`.
- Justificación: Concentra las reglas estructurales de cómo se representa un tablero agrupado en el dominio, en vez de ensuciar el caso de uso `ObtenerTablero` con bucles lógicos.
- Impacto: El caso de uso actúa estrictamente como un orquestador, y la respuesta generada es directamente compatible con JSON y el frontend.

### DEC-07 (Paso 11) - Tolerancia a fallos en deserialización JSON
- Decisión: Capturar la excepción `json.JSONDecodeError` al cargar el tablero y devolver un diccionario vacío para inicializar un nuevo estado.
- Justificación: Protege la aplicación si el archivo JSON persistido se corrompe o queda vacío de forma abrupta, cumpliendo con la expectativa de que siempre se pueda iniciar un tablero vacío si falla la carga.
- Impacto: Permite que la aplicación arranque de manera confiable y reescriba el archivo de persistencia con un estado limpio al primer intento de guardado.

### DEC-09 (Paso 12) - Traducción de excepciones a códigos HTTP
- Decisión: Capturar genéricamente `ErrorDominio` y `ValueError` en las rutas de Flask y mapearlos a respuestas `400 Bad Request`.
- Justificación: Evita que el dominio conozca o manipule conceptos web (como códigos HTTP), manteniendo la estricta separación requerida en la arquitectura hexagonal.
- Impacto: El adaptador HTTP maneja consistentemente cualquier fallo de negocio sin romper la aplicación.

### DEC-10 (Paso 13) - Servir archivos estáticos mediante el adaptador HTTP
- Decisión: Configurar Flask en `api.py` para servir los archivos del frontend estático (HTML, CSS, JS) desde el directorio `../frontend`.
- Justificación: Esto simplifica la ejecución del proyecto localmente evitando problemas de CORS, ya que tanto el API como la interfaz gráfica se acceden desde el mismo origen (`localhost:5000`).
- Impacto: El frontend interactúa fluidamente con los endpoints definidos sin configuración adicional, respetando la estructura de carpetas establecida en la arquitectura.

## 6. Bloqueos y solución

### BLOQ-01 - Error en creación de archivos vacíos
- Síntoma: Fallo en la herramienta `write_to_file` al intentar generar archivos `__init__.py` sin contenido.
- Causa probable: Restricción del esquema de la herramienta o error de parsing con strings vacíos.
- Solución aplicada: Ejecución de comando PowerShell `New-Item` para creación masiva de archivos.
- Evidencia: Salida de terminal confirmando la creación de los 6 archivos en la estructura `src/`.

### BLOQ-02 (Paso 4) - Archivo PLAN_ATOMICO.md no encontrado en raíz
- Síntoma: Fallo al intentar leer `PLAN_ATOMICO.md` directamente en la raíz del proyecto para validar los pasos siguientes.
- Causa probable: El archivo había sido ubicado de forma ordenada dentro del directorio `plan/` y no en la ruta principal.
- Solución aplicada: Se listó el contenido del directorio raíz para ubicar la carpeta correcta y luego se leyó desde `plan/PLAN_ATOMICO.md`.
- Evidencia: Acceso exitoso al plan atómico y reanudación inmediata de las tareas.
