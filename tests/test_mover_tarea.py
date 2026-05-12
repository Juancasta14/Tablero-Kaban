import pytest
from src.aplicacion.mover_tarea import MoverTarea
from src.dominio.estado_tarea import EstadoTarea
from src.dominio.errores import ErrorLimiteWipExcedido, ErrorTransicionInvalida, ErrorTareaNoEncontrada
from src.dominio.tablero import Tablero
from src.dominio.tarea import Tarea
from tests.conftest import MockRepositorioTablero

def test_mover_tarea_todo_a_doing(mock_repo: MockRepositorioTablero):
    # Setup
    tablero = mock_repo.tablero
    tarea = tablero.crear_tarea("Tarea 1")
    caso_uso = MoverTarea(mock_repo)

    # AC-01: mover una tarea de TODO a DOING funciona si DOING tiene menos de 3 tareas.
    tarea_actualizada = caso_uso.ejecutar(tarea.id_tarea, EstadoTarea.DOING)
    
    assert tarea_actualizada.estado == EstadoTarea.DOING
    # AC-05: después de un movimiento válido, el tablero se guarda.
    assert mock_repo.guardado is True

def test_mover_tarea_limite_wip_excedido():
    # Setup con 3 tareas en DOING y 1 en TODO
    tablero = Tablero([
        Tarea("T1", estado=EstadoTarea.DOING),
        Tarea("T2", estado=EstadoTarea.DOING),
        Tarea("T3", estado=EstadoTarea.DOING),
        Tarea("T4", estado=EstadoTarea.TODO)
    ])
    repo = MockRepositorioTablero(tablero)
    caso_uso = MoverTarea(repo)
    id_t4 = tablero.tareas[3].id_tarea

    # AC-02: mover una cuarta tarea a DOING lanza ErrorLimiteWipExcedido.
    with pytest.raises(ErrorLimiteWipExcedido):
        caso_uso.ejecutar(id_t4, EstadoTarea.DOING)

    # AC-06: si ocurre un error de dominio, el tablero no se guarda con cambios parciales.
    assert repo.guardado is False
    assert tablero.tareas[3].estado == EstadoTarea.TODO

def test_mover_tarea_todo_a_done(mock_repo: MockRepositorioTablero):
    tablero = mock_repo.tablero
    tarea = tablero.crear_tarea("Tarea 1")
    caso_uso = MoverTarea(mock_repo)

    # AC-03: mover de TODO a DONE lanza ErrorTransicionInvalida.
    with pytest.raises(ErrorTransicionInvalida):
        caso_uso.ejecutar(tarea.id_tarea, EstadoTarea.DONE)

    assert mock_repo.guardado is False

def test_mover_tarea_doing_a_done():
    tablero = Tablero([Tarea("T1", estado=EstadoTarea.DOING)])
    repo = MockRepositorioTablero(tablero)
    caso_uso = MoverTarea(repo)
    id_t1 = tablero.tareas[0].id_tarea

    # AC-04: mover de DOING a DONE funciona.
    tarea_actualizada = caso_uso.ejecutar(id_t1, EstadoTarea.DONE)
    
    assert tarea_actualizada.estado == EstadoTarea.DONE
    assert repo.guardado is True

def test_mover_tarea_no_encontrada(mock_repo: MockRepositorioTablero):
    caso_uso = MoverTarea(mock_repo)
    
    with pytest.raises(ErrorTareaNoEncontrada):
        caso_uso.ejecutar("id-falso", EstadoTarea.DOING)

    assert mock_repo.guardado is False
