# BITACORA.md -- Tablero Kanban Personal

## 1. Estado actual
- Pasos ejecutados: 3 de 15.
- Paso en curso: ninguno.
- Última actualización: 2026-05-10 22:01.
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

## 4. Pasos pendientes
- [ ] Paso 4 - Crear Tablero y operación crear_tarea
- [ ] Paso 5 - Implementar movimiento y transiciones
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
### DEC-XX (paso N) - {titulo} - Decisión: {qué se decidió} - Justificación: {por qué} - Impacto: {pasos afectados} ## 6. Bloqueos y solución ### BLOQ-XX - Síntoma: - Causa probable: - Solución aplicada: - Evidencia:
