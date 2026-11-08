from puertas.Puerta import Puerta

class PuertaEspecial(Puerta):
    """Representa una puerta que requiere código de autorización para abrirse.

    Args:
        codigo_puerta (str): Código identificador de la puerta.
        codigo_autorizacion (str): Código necesario para abrir la puerta.
    """

    def __init__(self, codigo_puerta, codigo_autorizacion):
        super().__init__(codigo_puerta)
        self.codigo_autorizacion = codigo_autorizacion

    @property
    def codigo_autorizacion(self):
        """str: Código de autorización de la puerta."""
        return self.__codigo_autorizacion

    @codigo_autorizacion.setter
    def codigo_autorizacion(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El código de autorización no puede estar vacío.")
        self.__codigo_autorizacion = valor

    def abrir(self, codigo=None):
        """Intenta abrir la puerta validando el código de autorización.

        Args:
            codigo (str, optional): Código ingresado para intentar abrir la puerta.

        Returns:
            str: Mensaje indicando si se abrió la puerta o si el acceso fue denegado.
        """
        if codigo == self.codigo_autorizacion:
            super().abrir()
            return f"La puerta especial {self.codigo_puerta} ha sido abierta con éxito."
        else:
            return f"Código incorrecto, acceso denegado en la puerta {self.codigo_puerta}."

    def cerrar(self):
        """Cierra la puerta especial.

        Returns:
            str: Mensaje propio indicando que la puerta especial se cerró.
        """
        super().cerrar()
        return f"La puerta especial {self.codigo_puerta} se cerró."

    def __str__(self):
        estado = "abierta" if self.abierta else "cerrada"
        return f"Puerta especial: {self.codigo_puerta}, estado: {estado}"