class ErrorDominio(Exception):
    """Excepción base para todos los errores de dominio."""
    pass

class ErrorTareaNoEncontrada(ErrorDominio):
    pass

class ErrorTransicionInvalida(ErrorDominio):
    pass

class ErrorLimiteWipExcedido(ErrorDominio):
    pass

class ErrorTituloTareaInvalido(ErrorDominio):
    pass
