import uuid
from src.dominio.estado_tarea import EstadoTarea
from src.dominio.errores import ErrorTituloTareaInvalido

class Tarea:
    def __init__(self, titulo: str, id_tarea: str | None = None, estado: EstadoTarea = EstadoTarea.TODO):
        if not titulo or not titulo.strip():
            raise ErrorTituloTareaInvalido("El título no puede estar vacío ni contener solo espacios")
        
        self.id_tarea = id_tarea or str(uuid.uuid4())
        self.titulo = titulo.strip()
        self.estado = estado
