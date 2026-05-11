from typing import List
from src.dominio.tarea import Tarea
from src.dominio.estado_tarea import EstadoTarea
from src.dominio.errores import ErrorTareaNoEncontrada, ErrorTransicionInvalida

LIMITE_WIP = 3

class Tablero:
    def __init__(self, tareas: List[Tarea] | None = None):
        self.tareas = tareas or []
        
    def crear_tarea(self, titulo: str) -> Tarea:
        tarea = Tarea(titulo=titulo)
        self.tareas.append(tarea)
        return tarea

    def mover_tarea(self, id_tarea: str, estado_destino: EstadoTarea) -> Tarea:
        tarea = next((t for t in self.tareas if t.id_tarea == id_tarea), None)
        if not tarea:
            raise ErrorTareaNoEncontrada(f"Tarea con id {id_tarea} no encontrada")
            
        if tarea.estado == EstadoTarea.TODO and estado_destino != EstadoTarea.DOING:
            raise ErrorTransicionInvalida("Una tarea TODO solo puede pasar a DOING")
        if tarea.estado == EstadoTarea.DOING and estado_destino != EstadoTarea.DONE:
            raise ErrorTransicionInvalida("Una tarea DOING solo puede pasar a DONE")
        if tarea.estado == EstadoTarea.DONE:
            raise ErrorTransicionInvalida("Una tarea DONE no puede cambiar de estado")
            
        tarea.estado = estado_destino
        return tarea
