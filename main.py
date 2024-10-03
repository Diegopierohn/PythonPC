# Problema 9

from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado

def validar_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser un número positivo.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            radio = validar_numero_positivo("Ingrese el radio del círculo: ")
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area():.2f}")
        
        elif opcion == '2':
            largo = validar_numero_positivo("Ingrese el largo del rectángulo: ")
            ancho = validar_numero_positivo("Ingrese el ancho del rectángulo: ")
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")
        
        elif opcion == '3':
            lado = validar_numero_positivo("Ingrese el lado del cuadrado: ")
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

menu()

# Problema 10

from gestion import GestionBiblioteca
from libro import Libro

def menu():
    gestion = GestionBiblioteca()

    while True:
        print("\nMenú de Biblioteca:")
        print("1. Agregar un libro a la biblioteca")
        print("2. Listar los libros en la biblioteca")
        print("3. Buscar un libro según su título")
        print("4. Buscar un libro según su autor")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(nuevo_libro)
        
        elif opcion == '2':
            gestion.listar_libros()
        
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a buscar: ")
            gestion.buscar_por_titulo(titulo)
        
        elif opcion == '4':
            autor = input("Ingrese el nombre del autor a buscar: ")
            gestion.buscar_por_autor(autor)
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

menu()