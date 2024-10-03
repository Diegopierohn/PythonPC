# Practica 03
# Apellidos y Nombres: Huallpa Nina Diego Piero

def problema_1():
    while True:
        try:
            fraccion = input("Ingrese fracción en el formato X/Y: ")
            x, y = fraccion.split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            elif x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = (x/y)*100
            
            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            
            break
        
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar números enteros en el formato X/Y.")
        except ZeroDivisionError:
            print("Entrada no válida. El denominador no puede ser 0.")
            
problema_1()

# Problema 2

def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            
            calificaciones = entrada.split(",")
            
            calificaciones_int = [int(calificacion.strip()) for calificacion in calificaciones]

            return calificaciones_int

        except ValueError:
            print("Error: Se ha ingresado un valor no válido. Asegúrese de que todas las calificaciones sean números enteros.")

lista_calificaciones = obtener_calificaciones()
print("Lista de calificaciones:", lista_calificaciones)

# Problema 3

import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

print(f"El área del círculo 1 con radio {circulo1.radio} es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo 2 con radio {circulo2.radio} es: {circulo2.calcular_area():.2f}")

# Problema 4

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo1 = RECTANGULO(10, 5)

cuadrado1 = CUADRADO(7)

print(f"El área del rectángulo con largo {rectangulo1.largo} y ancho {rectangulo1.ancho} es: {rectangulo1.calcular_area()}")
print(f"El área del cuadrado con lado {cuadrado1.largo} es: {cuadrado1.calcular_area()}")

# Problema 5

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad if self.edad is not None else 'No asignada'}")
        print(f"Nota: {self.nota if self.nota is not None else 'No asignada'}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota

estudiante1 = Alumno("Carlos López", "B12345")

estudiante1.setAge(21)
estudiante1.setNota(88)

estudiante1.display()

# Problema 6

class Producto:
    def __init__(self, nombre, precio, tipo, año_fabricacion):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.año_fabricacion = año_fabricacion

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Tipo: {self.tipo}, Año: {self.año_fabricacion}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al catálogo.")

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos fabricados en el año {año}:")
        encontrados = [prod for prod in self.productos if prod.año_fabricacion == año]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos del año {año}.")

    def filtrar_por_tipo(self, tipo):
        print(f"Productos del tipo '{tipo}':")
        encontrados = [prod for prod in self.productos if prod.tipo.lower() == tipo.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos del tipo '{tipo}'.")

producto1 = Producto("Motor V8", 2500, "Motor", 2021)
producto2 = Producto("Batería de coche", 120, "Batería", 2020)
producto3 = Producto("Pastillas de freno", 75, "Frenos", 2022)

catalogo_tienda = Catalogo()

catalogo_tienda.agregar_producto(producto1)
catalogo_tienda.agregar_producto(producto2)
catalogo_tienda.agregar_producto(producto3)

catalogo_tienda.mostrar_productos()

catalogo_tienda.filtrar_por_año(2020)

catalogo_tienda.filtrar_por_tipo("Motor")

# Problema 7

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Punto movido a: ({self.x}, {self.y})")

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

p1 = Punto(3, 4)
p2 = Punto(7, 1)

p1.mostrar()
p2.mostrar()

dist = p1.distancia(p2)
print(f"Distancia entre p1 y p2: {dist:.2f}")

p1.mover(2, -3)