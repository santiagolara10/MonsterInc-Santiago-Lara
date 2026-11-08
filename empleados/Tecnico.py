from empleados.Empleado import Empleado

class Tecnico(Empleado):
    """Representa un técnico de mantenimiento en la empresa.

    Args:
        nombre (str): Nombre del técnico.
        numero_empleado (int): Número de identificación, debe ser mayor a 0.
        especialidad (str): Especialidad del técnico, no puede estar vacía.
    """

    def __init__(self, nombre, numero_empleado, especialidad):
        super().__init__(nombre, numero_empleado)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        """str: Especialidad técnica del empleado."""
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("La especialidad no puede estar vacía.")
        self.__especialidad = valor

    def realizar_trabajo(self):
        """Simula la acción de trabajar del técnico.

        Returns:
            str: Mensaje indicando en qué especialidad está trabajando.
        """
        return f"El técnico {self.nombre} está dando mantenimiento a los equipos de {self.especialidad}."

    def __str__(self):
        return f"Técnico: {self.nombre}, número: {self.numero_empleado}, especialidad: {self.especialidad}"