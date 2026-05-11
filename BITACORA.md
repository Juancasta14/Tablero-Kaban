# BITACORA.md -- Tablero Kanban Personal

## 1. Estado actual
- Pasos ejecutados: 5 de 15.
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

## 4. Pasos pendientes
- [ ] Paso 6 - Proteger límite WIP y atomicidad
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

## 6. Bloqueos y solución

### BLOQ-01 - Error en creación de archivos vacíos
- Síntoma: Fallo en la herramienta `write_to_file` al intentar generar archivos `__init__.py` sin contenido.
- Causa probable: Restricción del esquema de la herramienta o error de parsing con strings vacíos.
- Solución aplicada: Ejecución de comando PowerShell `New-Item` para creación masiva de archivos.
- Evidencia: Salida de terminal confirmando la creación de los 6 archivos en la estructura `src/`.
