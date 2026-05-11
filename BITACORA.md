# BITACORA.md -- Tablero Kanban Personal

## 1. Estado actual
- Pasos ejecutados: 6 de 15.
- Paso en curso: ninguno.
- Última actualización: 2026-05-10 22:11.
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

## 4. Pasos pendientes
- [x] Paso 6 - Proteger límite WIP y atomicidad
- [ ] Paso 7 - Crear puerto RepositorioTablero
- [ ] Paso 8 - Crear caso de uso CrearTarea
- [ ] Paso 9 - Crear caso de uso MoverTarea
- [ ] Paso 10 - Crear caso de uso ObtenerTablero
- [ ] Paso 11 - Implementar repositorio JSON
- [ ] Paso 12 - Crear adaptador HTTP Flask
- [ ] Paso 13 - Crear frontend HTML/CSS/JS
- [ ] Paso 14 - Agregar pruebas y validaciones finales
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
