from src.aplicacion.repositorio_tablero import RepositorioTablero

class ObtenerTablero:
    def __init__(self, repositorio: RepositorioTablero):
        self.repositorio = repositorio

    def ejecutar(self) -> dict:
        tablero = self.repositorio.cargar()
        return tablero.obtener_tareas_por_estado()
