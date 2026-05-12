# Tablero Kanban Personal con Límite WIP

## 1. Descripción
Aplicación local para gestionar tareas personales en columnas TODO, DOING y DONE. La regla central es que DOING no puede contener más de tres tareas simultáneas.

## 2. Requisitos
- Python 3.11 o superior.
- Flask 3.x.
- pytest.

## 3. Instalación sugerida
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install flask pytest
```

## 4. Ejecución de pruebas
```bash
python -m pytest tests/
```

## 5. Ejecución de la aplicación
```bash
python src/infraestructura/http/api.py
```
La aplicación estará disponible en `http://localhost:5000/`.

## 6. Validación arquitectónica
El dominio no debe importar Flask, HTTP, JSON, rutas de archivo ni dependencias de infraestructura.

## 7. Trazabilidad
Cada cambio debe estar asociado a un paso de PLAN_ATOMICO.md y a una entrada de BITACORA.md.
