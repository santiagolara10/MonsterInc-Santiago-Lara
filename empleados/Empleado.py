class Empleado:
    """Representa un empleado base de la empresa.

    Args:
        nombre (str): Nombre del empleado.
        numero_empleado (int): Número de identificación del empleado, debe ser mayor a 0.
    """

    def __init__(self, nombre, numero_empleado):
        self.nombre = nombre
        self.numero_empleado = numero_empleado

    @property
    def nombre(self):
        """str: Nombre del empleado."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def numero_empleado(self):
        """int: Número de identificación del empleado."""
        return self.__numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        if type(valor) != int or valor <= 0:
            raise ValueError("El número de empleado debe ser un número entero mayor a 0.")
        self.__numero_empleado = valor

    def realizar_trabajo(self):
        """Simula la acción de trabajar del empleado.

        Returns:
            str: Un mensaje genérico indicando que el empleado está trabajando.
        """
        return "El empleado está realizando su trabajo."

    def __str__(self):
        return f"Empleado: {self.nombre}, número: {self.numero_empleado}"