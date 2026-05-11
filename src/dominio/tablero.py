from typing import List
from src.dominio.tarea import Tarea

LIMITE_WIP = 3

class Tablero:
    def __init__(self, tareas: List[Tarea] | None = None):
        self.tareas = tareas or []
        
    def crear_tarea(self, titulo: str) -> Tarea:
        tarea = Tarea(titulo=titulo)
        self.tareas.append(tarea)
        return tarea
