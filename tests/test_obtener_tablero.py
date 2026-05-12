from src.aplicacion.obtener_tablero import ObtenerTablero
from src.dominio.tablero import Tablero
from src.dominio.tarea import Tarea
from src.dominio.estado_tarea import EstadoTarea
from tests.conftest import MockRepositorioTablero

def test_obtener_tablero_vacio():
    repo = MockRepositorioTablero()
    caso_uso = ObtenerTablero(repo)

    resultado = caso_uso.ejecutar()

    # AC-01: obtener el tablero devuelve siempre las claves TODO, DOING y DONE.
    assert "TODO" in resultado
    assert "DOING" in resultado
    assert "DONE" in resultado
    assert len(resultado["TODO"]) == 0
    assert len(resultado["DOING"]) == 0
    assert len(resultado["DONE"]) == 0

    # AC-02: una consulta no modifica el estado del dominio.
    assert repo.guardado is False

def test_obtener_tablero_con_tareas():
    tablero = Tablero([
        Tarea("Tarea 1", estado=EstadoTarea.TODO),
        Tarea("Tarea 2", estado=EstadoTarea.DOING),
        Tarea("Tarea 3", estado=EstadoTarea.DONE)
    ])
    repo = MockRepositorioTablero(tablero)
    caso_uso = ObtenerTablero(repo)

    resultado = caso_uso.ejecutar()

    assert len(resultado["TODO"]) == 1
    assert resultado["TODO"][0]["titulo"] == "Tarea 1"
    
    assert len(resultado["DOING"]) == 1
    assert resultado["DOING"][0]["titulo"] == "Tarea 2"
    
    assert len(resultado["DONE"]) == 1
    assert resultado["DONE"][0]["titulo"] == "Tarea 3"

    assert repo.guardado is False
