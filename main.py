from monstruos import Asustador, Comediante, Ayudante
from empleados import Operador, Tecnico, Supervisor
from puertas import PuertaNormal, PuertaEspecial

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n--- Menú Principal ---")
    print("1. Agregar monstruo")
    print("2. Listar monstruos")
    print("3. Agregar empleado")
    print("4. Listar empleados")
    print("5. Agregar puerta")
    print("6. Listar puertas")
    print("7. Simular producción de energía")
    print("0. Salir del sistema")

def agregar_monstruo(lista_monstruos):
    """Submenú para agregar un monstruo específico."""
    print("\n--- Tipo de Monstruo ---")
    print("1. Agregar Asustador")
    print("2. Agregar Comediante")
    print("3. Agregar Ayudante")
    opcion = input("Seleccione el tipo: ")

    if opcion not in ['1', '2', '3']:
        print("Opción inválida.")
        return

    try:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        if opcion == '1':
            nivel = int(input("Ingrese el nivel de susto (1-10): "))
            nuevo_monstruo = Asustador(nombre, edad, nivel)
        elif opcion == '2':
            nivel = int(input("Ingrese el nivel de humor (1-10): "))
            nuevo_monstruo = Comediante(nombre, edad, nivel)
        elif opcion == '3':
            nivel = int(input("Ingrese el nivel de apoyo (1-10): "))
            nuevo_monstruo = Ayudante(nombre, edad, nivel)

        lista_monstruos.append(nuevo_monstruo)
        print("¡Monstruo agregado con éxito!")

    except ValueError as e:
        print(f"Error: {e}")

def agregar_empleado(lista_empleados):
    """Submenú para agregar un empleado específico."""
    print("\n--- Tipo de Empleado ---")
    print("1. Agregar Operador")
    print("2. Agregar Técnico")
    print("3. Agregar Supervisor")
    opcion = input("Seleccione el tipo: ")

    if opcion not in ['1', '2', '3']:
        print("Opción inválida.")
        return

    try:
        nombre = input("Ingrese el nombre: ")
        numero = int(input("Ingrese el número de empleado: "))

        if opcion == '1':
            maquina = input("Ingrese la máquina asignada: ")
            nuevo_empleado = Operador(nombre, numero, maquina)
        elif opcion == '2':
            especialidad = input("Ingrese la especialidad: ")
            nuevo_empleado = Tecnico(nombre, numero, especialidad)
        elif opcion == '3':
            area = input("Ingrese el área a supervisar: ")
            nuevo_empleado = Supervisor(nombre, numero, area)

        lista_empleados.append(nuevo_empleado)
        print("¡Empleado agregado con éxito!")

    except ValueError as e:
        print(f"Error: {e}")

def agregar_puerta(lista_puertas):
    """Submenú para agregar una puerta específica."""
    print("\n--- Tipo de Puerta ---")
    print("1. Agregar Puerta Normal")
    print("2. Agregar Puerta Especial")
    opcion = input("Seleccione el tipo: ")

    if opcion not in ['1', '2']:
        print("Opción inválida.")
        return

    try:
        codigo = input("Ingrese el código de la puerta: ")

        if opcion == '1':
            nueva_puerta = PuertaNormal(codigo)
        elif opcion == '2':
            codigo_auth = input("Ingrese el código de autorización: ")
            nueva_puerta = PuertaEspecial(codigo, codigo_auth)

        lista_puertas.append(nueva_puerta)
        print("¡Puerta agregada con éxito!")

    except ValueError as e:
        print(f"Error: {e}")

def listar(lista, titulo):
    """Muestra los elementos de una lista o un mensaje si está vacía."""
    print(f"\n--- {titulo} ---")
    if not lista:
        print("No hay elementos registrados en esta categoría.")
    else:
        for elemento in lista:
            print(elemento)

def simular_energia(lista_monstruos):
    """Calcula y muestra la energía generada por los monstruos."""
    print("\n--- Simulación de Producción de Energía ---")
    if not lista_monstruos:
        print("No hay monstruos registrados para simular la producción.")
        return

    for monstruo in lista_monstruos:
        tipo_monstruo = type(monstruo).__name__
        energia = monstruo.generar_energia()
        print(f"Nombre: {monstruo.nombre} | Tipo: {tipo_monstruo} | Energía producida: {energia}")

def main():
    """Función principal que controla el flujo del programa."""
    lista_monstruos = []
    lista_empleados = []
    lista_puertas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_monstruo(lista_monstruos)
        elif opcion == '2':
            listar(lista_monstruos, "Lista de Monstruos")
        elif opcion == '3':
            agregar_empleado(lista_empleados)
        elif opcion == '4':
            listar(lista_empleados, "Lista de Empleados")
        elif opcion == '5':
            agregar_puerta(lista_puertas)
        elif opcion == '6':
            listar(lista_puertas, "Lista de Puertas")
        elif opcion == '7':
            simular_energia(lista_monstruos)
        elif opcion == '0':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, seleccione un número del menú.")

if __name__ == '__main__':
    main()