from empleados.Empleado import Empleado

class Supervisor(Empleado):
    """Representa un supervisor de área en la empresa.

    Args:
        nombre (str): Nombre del supervisor.
        numero_empleado (int): Número de identificación, debe ser mayor a 0.
        area (str): Área que supervisa, no puede estar vacía.
    """

    def __init__(self, nombre, numero_empleado, area):
        super().__init__(nombre, numero_empleado)
        self.area = area

    @property
    def area(self):
        """str: Área a cargo del supervisor."""
        return self.__area

    @area.setter
    def area(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El área no puede estar vacía.")
        self.__area = valor

    def realizar_trabajo(self):
        """Simula la acción de trabajar del supervisor.

        Returns:
            str: Mensaje indicando qué área está coordinando.
        """
        return f"El supervisor {self.nombre} está coordinando y revisando el área de {self.area}."

    def __str__(self):
        return f"Supervisor: {self.nombre}, número: {self.numero_empleado}, área: {self.area}"