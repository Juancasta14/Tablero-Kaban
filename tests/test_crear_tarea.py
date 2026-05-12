import pytest
from src.aplicacion.crear_tarea import CrearTarea
from src.dominio.estado_tarea import EstadoTarea
from src.dominio.errores import ErrorTituloTareaInvalido
from tests.conftest import MockRepositorioTablero

def test_crear_tarea_valida(mock_repo: MockRepositorioTablero):
    # AC-01: crear una tarea con título válido genera id_tarea, conserva titulo y asigna estado TODO.
    caso_uso = CrearTarea(mock_repo)
    tarea = caso_uso.ejecutar("Mi nueva tarea")
    
    assert tarea.id_tarea is not None
    assert tarea.titulo == "Mi nueva tarea"
    assert tarea.estado == EstadoTarea.TODO

    # AC-04: después de crear una tarea válida, el tablero se guarda.
    assert mock_repo.guardado is True
    assert len(mock_repo.tablero.tareas) == 1
    assert mock_repo.tablero.tareas[0].id_tarea == tarea.id_tarea

def test_crear_tarea_titulo_vacio(mock_repo: MockRepositorioTablero):
    # AC-02: crear una tarea con título vacío lanza ErrorTituloTareaInvalido.
    caso_uso = CrearTarea(mock_repo)
    
    with pytest.raises(ErrorTituloTareaInvalido):
        caso_uso.ejecutar("")

    # AC-05: si ocurre un error de dominio, el tablero no se guarda con cambios parciales.
    assert mock_repo.guardado is False
    assert len(mock_repo.tablero.tareas) == 0

def test_crear_tarea_solo_espacios(mock_repo: MockRepositorioTablero):
    # AC-03: crear una tarea con solo espacios lanza ErrorTituloTareaInvalido.
    caso_uso = CrearTarea(mock_repo)
    
    with pytest.raises(ErrorTituloTareaInvalido):
        caso_uso.ejecutar("   ")

    # AC-05: si ocurre un error de dominio, el tablero no se guarda con cambios parciales.
    assert mock_repo.guardado is False
    assert len(mock_repo.tablero.tareas) == 0
