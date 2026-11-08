from empleados.Empleado import Empleado

class Operador(Empleado):
    """Representa un operador de maquinaria en la empresa.

    Args:
        nombre (str): Nombre del operador.
        numero_empleado (int): Número de identificación, debe ser mayor a 0.
        maquina (str): Nombre de la máquina asignada, no puede estar vacío.
    """

    def __init__(self, nombre, numero_empleado, maquina):
        super().__init__(nombre, numero_empleado)
        self.maquina = maquina

    @property
    def maquina(self):
        """str: Máquina que opera el empleado."""
        return self.__maquina

    @maquina.setter
    def maquina(self, valor):
        if type(valor) != str or valor.strip() == "":
            raise ValueError("El nombre de la máquina no puede estar vacío.")
        self.__maquina = valor

    def realizar_trabajo(self):
        """Simula la acción de trabajar del operador.

        Returns:
            str: Mensaje indicando qué máquina está operando.
        """
        return f"El operador {self.nombre} está a cargo de la máquina {self.maquina}."

    def __str__(self):
        return f"Operador: {self.nombre}, número: {self.numero_empleado}, máquina: {self.maquina}"