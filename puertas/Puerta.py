class Puerta:
    """Representa una puerta base del sistema.

    Args:
        codigo_puerta (str): Código identificador de la puerta.
    """

    def __init__(self, codigo_puerta):
        self.codigo_puerta = codigo_puerta
        self.abierta = False

    @property
    def codigo_puerta(self):
        """str: Código identificador de la puerta."""
        return self.__codigo_puerta

    @codigo_puerta.setter
    def codigo_puerta(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El código de la puerta no puede estar vacío.")
        self.__codigo_puerta = valor

    @property
    def abierta(self):
        """bool: Estado de la puerta."""
        return self.__abierta

    @abierta.setter
    def abierta(self, valor):
        if type(valor) != bool:
            raise ValueError("El estado de la puerta debe ser True o False.")
        self.__abierta = valor

    def abrir(self, codigo=None):
        """Abre la puerta cambiando su estado.

        Args:
            codigo (str, optional): Código de acceso opcional para la puerta. Por defecto es None.

        Returns:
            str: Mensaje indicando que la puerta se abrió.
        """
        self.abierta = True
        return f"La puerta {self.codigo_puerta} ahora está abierta."

    def cerrar(self):
        """Cierra la puerta cambiando su estado.

        Returns:
            str: Mensaje indicando que la puerta se cerró.
        """
        self.abierta = False
        return f"La puerta {self.codigo_puerta} ahora está cerrada."

    def __str__(self):
        estado = "abierta" if self.abierta else "cerrada"
        return f"Puerta: {self.codigo_puerta}, estado: {estado}"