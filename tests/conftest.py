import pytest
from src.dominio.tablero import Tablero
from src.aplicacion.repositorio_tablero import RepositorioTablero

class MockRepositorioTablero(RepositorioTablero):
    def __init__(self, tablero_inicial: Tablero | None = None):
        self.tablero = tablero_inicial or Tablero()
        self.guardado = False

    def cargar(self) -> Tablero:
        return self.tablero

    def guardar(self, tablero: Tablero) -> None:
        self.tablero = tablero
        self.guardado = True

@pytest.fixture
def mock_repo():
    return MockRepositorioTablero()
