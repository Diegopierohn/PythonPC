## Problema 1
nombre=input("Ingrese el nombre del usuario: ")
print(f"¡Hola {nombre}!" )

## Problema 2
costo_comida=float(input("Ingrese cuánto fue el consumo en el restaurante: "))
porcentaje_propina=float(input("Ingrese el porcentaje de propina que va a dejar: "))
propina=(costo_comida * porcentaje_propina)/100
print("La cantidad de dinero que se debe de dejar es:", propina)

## Problema 3
peso_payaso = 112
peso_muñeco = 75

num_payaso = int(input("Ingrese la cantidad de payasos que se vendieron: "))
num_muñecos = int(input("Ingrese la cantidad de muñecos que se vendieron: "))

peso_total = (peso_payaso * num_payaso) + (peso_muñeco * num_muñecos)

print(f"El peso total del paquete que será enviado es: {peso_total} gramos")

## Problema 4

numero_entero = int(input("Ingrese un número(N) entero: "))
suma_N_primeros = (numero_entero * (numero_entero + 1))/2
print(f"La suma de los N primero es: {suma_N_primeros}")

## Problema 5

numero_shows = int(input("Ingrese cuántos shows musicales se ha visto en el último año: "))
comparacion_veces = numero_shows>3
print(f"El usuario ha visto más de 3 shows: {comparacion_veces}")

## Problema 6

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10
    
print("El precio de la entrada es:", precio)

## Problema 7

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

print("\nElige una opción: ")
print("1. Suma de los dos números")
print("2. Restar el primero menos el segundo")
print("3. Multiplica los dos números")

opcion = input("Ingresa el número de la opción seleccionada: ")

if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"El producto es: {resultado}")
else:
    print("Opción incorrecta. Elija 1, 2 o 3")
    
## Problema 8

hora_ingresada = input("Introduce la hora (formato 24 horas HH:MM): ")

if "7:00" <= hora_ingresada <= "8:00":
    print("Es hora de desayunar")
elif "12:00" <= hora_ingresada <= "13:00":
    print("Es hora de almorzar")
elif "18:00" <= hora_ingresada <= "19:00":
    print("Es hora de cenar")
    
## Problema 9

lista_original = ["Di", "buen", "día", "a", "papa"]
lista_original.reverse()
print(lista_original)

## Problema 10

lista =  ["Rojo", "Verde", "Blanco", "Negro", "Rosa", "Amarillo"]
lista.remove("Rojo")
lista.remove("Rosa")
lista.remove("Amarillo")
print(lista)

## Problema 11

conjunto_numeros = {1,1,2,3,4,4,5,1}
conjunto_numeros

## Problema 12

nombre_archivo = input("Introduce el nombre del archivo: ").lower()

mime_tipo = "application/octet-stream"

if nombre_archivo.endswith(".gif"):
    mime_tipo = "image/gif"
elif nombre_archivo.endswith(".jpg"):
    mime_tipo = "image/jpg"
elif nombre_archivo.endswith(".jpeg"):
    mime_tipo = "image/jpeg"
elif nombre_archivo.endswith(".png"):
    mime_tipo = "image/png"
elif nombre_archivo.endswith(".pdf"):
    mime_tipo = "application/pdf"
elif nombre_archivo.endswith(".txt"):
    mime_tipo = "text/plain"
elif nombre_archivo.endswith(".zip"):
    mime_tipo = "application/zip"
    
print(mime_tipo)