from abc import ABC, abstractmethod
from src.dominio.tablero import Tablero

class RepositorioTablero(ABC):
    @abstractmethod
    def cargar(self) -> Tablero:
        pass

    @abstractmethod
    def guardar(self, tablero: Tablero) -> None:
        pass
