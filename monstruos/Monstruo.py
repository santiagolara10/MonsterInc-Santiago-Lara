class Monstruo:
    """Representa un monstruo base del sistema.

    Args:
        nombre (str): Nombre del monstruo.
        edad (int): Edad del monstruo, debe ser mayor a 0.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        """str: Nombre del monstruo."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío y debe ser texto.")
        self.__nombre = valor

    @property
    def edad(self):
        """int: Edad del monstruo."""
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if type(valor) != int or valor <= 0:
            raise ValueError("La edad debe ser un número entero mayor a 0.")
        self.__edad = valor

    def generar_energia(self):
        """Calcula la energía generada por el monstruo.

        Returns:
            int: 0, ya que es la clase padre y las hijas lo sobrescriben.
        """
        return 0

    def __str__(self):
        return f"Monstruo: {self.nombre}, edad: {self.edad}"