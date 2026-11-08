from monstruos.Monstruo import Monstruo

class Asustador(Monstruo):
    """Representa un monstruo que genera energía asustando.

    Args:
        nombre (str): Nombre del asustador.
        edad (int): Edad del asustador, debe ser mayor a 0.
        nivel_susto (int): Nivel de susto, debe ser un entero entre 1 y 10.
    """

    def __init__(self, nombre, edad, nivel_susto):
        super().__init__(nombre, edad)
        self.nivel_susto = nivel_susto

    @property
    def nivel_susto(self):
        """int: Nivel de susto del monstruo."""
        return self.__nivel_susto

    @nivel_susto.setter
    def nivel_susto(self, valor):
        if type(valor) != int or valor < 1 or valor > 10:
            raise ValueError("El nivel de susto debe ser un número entero entre 1 y 10.")
        self.__nivel_susto = valor

    def generar_energia(self):
        """Calcula la energía generada por el asustador.

        Returns:
            int: El nivel de susto multiplicado por 5.
        """
        return self.nivel_susto * 5

    def __str__(self):
        return f"Asustador: {self.nombre}, edad: {self.edad}, nivel de susto: {self.nivel_susto}"