# Apellidos y Nombres: Huallpa Nina Diego Piero

# Problema 1

numero_encontrados = []

for numero in range(1500,2701):
    if numero % 7 == 0 and numero % 5 == 0:
        numero_encontrados.append(numero)
        
print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(numero)

# Problema 2

n = 5

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)
    
# Problema 3

numero_ingresados = []
contador_pares = 0
contador_impares = 0

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if desea_ingresar == "SI":
        numero = int(input("Ingrese el número: "))
        numero_ingresados.append(numero)
        
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    elif desea_ingresar == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")
        
print("Números ingresados:", numero_ingresados)
print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)

# Problema 4

alumnos = []

n = int(input("¿Cuántos alumnos desea ingresar? "))

for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    
    notas = []
    for i in range(3):
        calificacion = int(input(f"Ingrese la calificación {i + 1} para {nombre}: "))
        notas.append(calificacion)

    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }

    alumnos.append(alumno)

print("\nListado de alumnos y sus notas:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
    
# Problema 5

def es_primo(num):
    """Función que determina si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

suma_primos = 0

for numero in range(100):
    if es_primo(numero):
        suma_primos += numero
        
print("La suma de todos los números primos menores que 100 es:", suma_primos)

# Problema 6

fibonacci = []
a, b = 0, 1

while a <= 50:
    fibonacci.append(a)
    a, b = b, a + b

print("La serie de Fibonacci entre 0 y 50 es:", fibonacci)

# Problema 7

def es_numero_perfecto(n):
    """Función que verifica si un número es perfecto."""
    suma_divisores = 0

    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
            
    return suma_divisores == n

numeros_perfectos = []

for numero in range(1, 1000):
    if es_numero_perfecto(numero):
        numeros_perfectos.append(numero)

print("Números perfectos menores que 1000:", numeros_perfectos)

# Problema 8

def factorial_iterativo(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {numero} es: {factorial_iterativo(numero)}")
    
# Problema 9

def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    texto_sin_vocales = ""

    for letra in texto:
        if letra not in vocales:
            texto_sin_vocales += letra

    return texto_sin_vocales

entrada = input("Ingrese una cadena de texto: ")

resultado = omitir_vocales(entrada)

print("Texto sin vocales:", resultado)

# Problema 10

def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03",
        "Abril": "04", "Mayo": "05", "Junio": "06",
        "Julio": "07", "Agosto": "08", "Septiembre": "09",
        "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    
    if '/' in fecha:
        mes, dia, año = fecha.split('/')
        return f"{año}-{mes.zfill(2)}-{dia.zfill(2)}"

    if ',' in fecha:
        partes = fecha.split(' ')
        mes = partes[0]
        dia = partes[1].rstrip(',')
        año = partes[2]
        if mes in meses:
            return f"{año}-{meses[mes]}-{dia.zfill(2)}"

    return "Formato de fecha no válido."

entrada = input("Ingrese una fecha (MM/DD/AAAA o 'Mes Día, Año'): ")

resultado = convertir_fecha(entrada)
print("Fecha en formato AAAA-MM-DD:", resultado)