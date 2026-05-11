# Manual de Ejecución - Tablero Kanban

Este proyecto utiliza **Poetry** para la gestión de dependencias y entornos virtuales, además de estar basado en Arquitectura Hexagonal.

## 1. Requisitos previos
- **Python:** Versión 3.11 o superior.
- **Poetry:** [Guía de instalación oficial](https://python-poetry.org/docs/#installation)

## 2. Instalación de dependencias
Abre una terminal (PowerShell, Bash o CMD) en la raíz del proyecto (`Tablero-Kaban`) y ejecuta el siguiente comando:

```bash
poetry install
```
Esto creará de forma automática un entorno virtual e instalará `Flask` (para el API HTTP) y `pytest` (para pruebas en desarrollo).

## 3. Ejecutar la aplicación

Para iniciar el servidor local Flask que provee la API y sirve el Frontend estático, ejecuta:

```bash
poetry run python src/infraestructura/http/api.py
```

Deberías ver un mensaje en la consola indicando que Flask está corriendo.

### 4. Acceder al tablero
Abre tu navegador web de preferencia y navega a la siguiente URL:
👉 **[http://localhost:5000](http://localhost:5000)**

## 5. Ejecutar pruebas (opcional)
Si has implementado casos de prueba o scripts de validación compatibles con `pytest`, puedes lanzarlos con:

```bash
poetry run pytest
```
