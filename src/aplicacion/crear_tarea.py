from src.dominio.tarea import Tarea
from src.aplicacion.repositorio_tablero import RepositorioTablero

class CrearTarea:
    def __init__(self, repositorio: RepositorioTablero):
        self.repositorio = repositorio

    def ejecutar(self, titulo: str) -> Tarea:
        tablero = self.repositorio.cargar()
        tarea = tablero.crear_tarea(titulo)
        self.repositorio.guardar(tablero)
        return tarea
