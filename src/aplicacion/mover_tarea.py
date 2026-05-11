from src.dominio.tarea import Tarea
from src.dominio.estado_tarea import EstadoTarea
from src.aplicacion.repositorio_tablero import RepositorioTablero

class MoverTarea:
    def __init__(self, repositorio: RepositorioTablero):
        self.repositorio = repositorio

    def ejecutar(self, id_tarea: str, estado_destino: EstadoTarea) -> Tarea:
        tablero = self.repositorio.cargar()
        tarea = tablero.mover_tarea(id_tarea, estado_destino)
        self.repositorio.guardar(tablero)
        return tarea
