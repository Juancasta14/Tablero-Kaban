import json
import os
from src.aplicacion.repositorio_tablero import RepositorioTablero
from src.dominio.tablero import Tablero
from src.dominio.tarea import Tarea
from src.dominio.estado_tarea import EstadoTarea

class RepositorioTableroJSON(RepositorioTablero):
    def __init__(self, ruta_archivo: str = "tablero.json"):
        self.ruta_archivo = ruta_archivo

    def cargar(self) -> Tablero:
        if not os.path.exists(self.ruta_archivo):
            return Tablero()
            
        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                datos = {}
            
        tareas = []
        for d in datos.get('tareas', []):
            tareas.append(Tarea(
                titulo=d['titulo'],
                id_tarea=d['id_tarea'],
                estado=EstadoTarea(d['estado'])
            ))
        return Tablero(tareas=tareas)

    def guardar(self, tablero: Tablero) -> None:
        datos = {
            'tareas': [
                {
                    'id_tarea': t.id_tarea,
                    'titulo': t.titulo,
                    'estado': t.estado.value
                } for t in tablero.tareas
            ]
        }
        with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
