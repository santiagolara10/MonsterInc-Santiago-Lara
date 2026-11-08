from monstruos.Monstruo import Monstruo

class Comediante(Monstruo):
    """Representa un monstruo que genera energía haciendo reír.

    Args:
        nombre (str): Nombre del comediante.
        edad (int): Edad del comediante, debe ser mayor a 0.
        nivel_humor (int): Nivel de humor, debe ser un entero entre 1 y 10.
    """

    def __init__(self, nombre, edad, nivel_humor):
        super().__init__(nombre, edad)
        self.nivel_humor = nivel_humor

    @property
    def nivel_humor(self):
        """int: Nivel de humor del comediante."""
        return self.__nivel_humor

    @nivel_humor.setter
    def nivel_humor(self, valor):
        if type(valor) != int or valor < 1 or valor > 10:
            raise ValueError("El nivel de humor debe ser un número entero entre 1 y 10.")
        self.__nivel_humor = valor

    def generar_energia(self):
        """Calcula la energía generada por el comediante.

        Returns:
            int: El nivel de humor multiplicado por 10.
        """
        return self.nivel_humor * 10

    def __str__(self):
        return f"Comediante: {self.nombre}, edad: {self.edad}, nivel de humor: {self.nivel_humor}"