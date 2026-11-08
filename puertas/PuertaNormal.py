from puertas.Puerta import Puerta

class PuertaNormal(Puerta):
    """Representa una puerta normal que no requiere autorización."""

    def __init__(self, codigo_puerta):
        super().__init__(codigo_puerta)

    def abrir(self, codigo=None):
        """Abre la puerta normal sin necesidad de autorización.

        Args:
            codigo (str, optional): Ignorado en esta clase. Por defecto es None.

        Returns:
            str: Mensaje indicando que la puerta se abrió sin autorización.
        """
        super().abrir()
        return f"La puerta {self.codigo_puerta} se abrió sin necesidad de autorización."

    def cerrar(self):
        """Cierra la puerta normal.

        Returns:
            str: Mensaje propio indicando que la puerta normal se cerró.
        """
        super().cerrar()
        return f"La puerta normal {self.codigo_puerta} se cerró."

    def __str__(self):
        estado = "abierta" if self.abierta else "cerrada"
        return f"Puerta normal: {self.codigo_puerta}, estado: {estado}"