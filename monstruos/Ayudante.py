from monstruos.Monstruo import Monstruo

class Ayudante(Monstruo):
    """Representa un monstruo que apoya a otros en la planta.

    Args:
        nombre (str): Nombre del ayudante.
        edad (int): Edad del ayudante, debe ser mayor a 0.
        nivel_apoyo (int): Nivel de apoyo, debe ser un entero entre 1 y 10.
    """

    def __init__(self, nombre, edad, nivel_apoyo):
        super().__init__(nombre, edad)
        self.nivel_apoyo = nivel_apoyo

    @property
    def nivel_apoyo(self):
        """int: Nivel de apoyo del ayudante."""
        return self.__nivel_apoyo

    @nivel_apoyo.setter
    def nivel_apoyo(self, valor):
        if type(valor) != int or valor < 1 or valor > 10:
            raise ValueError("El nivel de apoyo debe ser un número entero entre 1 y 10.")
        self.__nivel_apoyo = valor

    def generar_energia(self):
        """Calcula la energía generada por el ayudante.

        Returns:
            int: El nivel de apoyo multiplicado por 3.
        """
        return self.nivel_apoyo * 3

    def __str__(self):
        return f"Ayudante: {self.nombre}, edad: {self.edad}, nivel de apoyo: {self.nivel_apoyo}"