# Problema 1

import requests

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        datos = respuesta.json()

        precio_bitcoin = datos["bpi"]["USD"]["rate_float"]
        return precio_bitcoin

    except requests.RequestException as e:
        print("Error al obtener los datos:", e)
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))

        precio = obtener_precio_bitcoin()

        if precio is not None:
            costo_total = n * precio

            print(f"El valor de {n} bitcoins es: ${costo_total:,.4f} USD")
        else:
            print("No se pudo obtener el precio del Bitcoin.")
    
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
    
# Problema 2

import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    fuentes_disponibles = figlet.getFonts()

    fuente_usuario = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")

    if fuente_usuario and fuente_usuario in fuentes_disponibles:
        fuente_seleccionada = fuente_usuario
    else:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Se ha seleccionado la fuente aleatoria: {fuente_seleccionada}")

    figlet.setFont(font=fuente_seleccionada)

    texto = input("Ingrese el texto a imprimir: ")

    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
    
# Problema 3

import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        print("Descargando la imagen...")
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Imagen descargada como: {nombre_archivo}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def crear_zip(nombre_imagen, nombre_zip):
    try:
        print(f"Creando el archivo ZIP: {nombre_zip}...")
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_imagen)
        print("Archivo ZIP creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

def extraer_zip(nombre_zip, directorio_destino):
    try:
        print(f"Extrayendo el archivo ZIP: {nombre_zip}...")
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(directorio_destino)
        print(f"Archivo extraído en: {directorio_destino}")
    except Exception as e:
        print(f"Error al extraer el archivo ZIP: {e}")

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"
    nombre_zip = "imagen_comprimida.zip"
    directorio_destino = "./extraido"

    descargar_imagen(url, nombre_imagen)

    crear_zip(nombre_imagen, nombre_zip)

    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    extraer_zip(nombre_zip, directorio_destino)

if __name__ == "__main__":
    main()
    
# Problema 4

import csv

def leer_temperaturas(nombre_archivo):
    temperaturas = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                fecha, temperatura = linea
                temperaturas.append(float(temperatura))
    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return temperaturas

def calcular_estadisticas(temperaturas):
    if temperaturas:
        promedio = sum(temperaturas) / len(temperaturas)
        maxima = max(temperaturas)
        minima = min(temperaturas)
        return promedio, maxima, minima
    else:
        return None, None, None

def escribir_resumen(nombre_archivo, promedio, maxima, minima):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Temperatura promedio: {promedio:.2f}°C\n")
            archivo.write(f"Temperatura máxima: {maxima:.2f}°C\n")
            archivo.write(f"Temperatura mínima: {minima:.2f}°C\n")
        print(f"Resumen escrito en: {nombre_archivo}")
    except Exception as e:
        print(f"Error al escribir el resumen: {e}")

def main():
    archivo_entrada = "temperaturas.txt"
    archivo_salida = "resumen_temperaturas.txt"

    temperaturas = leer_temperaturas(archivo_entrada)

    promedio, maxima, minima = calcular_estadisticas(temperaturas)

    if promedio is not None:
        escribir_resumen(archivo_salida, promedio, maxima, minima)
    else:
        print("No se pudieron calcular estadísticas debido a un error.")

if __name__ == "__main__":
    main()
    
# Problema 5

import os

def generar_tabla(n):
    """Genera la tabla de multiplicar del número n y la guarda en un archivo."""
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla del {n} generada y guardada en {nombre_archivo}")

def leer_tabla(n):
    """Lee y muestra en pantalla la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nTabla de multiplicar del {n}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def mostrar_linea_tabla(n, m):
    """Muestra la línea m de la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m}: {lineas[m - 1]}", end='')
            else:
                print("El número de línea debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    """Menú principal para interactuar con el programa."""
    while True:
        print("\n--- Menú ---")
        print("1. Generar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= n <= 10:
                    generar_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '2':
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= n <= 10:
                    leer_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '3':
            try:
                n = int(input("Ingrese un número entre 1 y 10: "))
                m = int(input("Ingrese la línea que desea mostrar (entre 1 y 10): "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    mostrar_linea_tabla(n, m)
                else:
                    print("Ambos números deben estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese números válidos.")

        elif opcion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
    
# Problema 6

def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código en un archivo .py, excluyendo comentarios y líneas en blanco."""
    try:
        if not ruta_archivo.endswith(".py"):
            print("El archivo debe tener extensión .py.")
            return

        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        lineas_codigo = [
            linea for linea in lineas if linea.strip() and not linea.strip().startswith("#")
        ]

        print(f"El archivo {ruta_archivo} tiene {len(lineas_codigo)} líneas de código.")

    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
    
# Problema 7

import requests
from datetime import datetime, timedelta
from pymongo import MongoClient

def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["base_datos"]
        return db["sunat_info"]
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        return None

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos["compra"], datos["venta"]
        else:
            print(f"Error al obtener datos para {fecha}: {respuesta.status_code}")
            return None, None
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None, None

def insertar_datos_mongo(coleccion, fecha, compra, venta):
    try:
        coleccion.insert_one({"fecha": fecha, "compra": compra, "venta": venta})
        print(f"Datos insertados para {fecha}")
    except Exception as e:
        print(f"Error al insertar en MongoDB: {e}")

def mostrar_datos_mongo(coleccion):
    for registro in coleccion.find():
        print(registro)

def main():
    coleccion = conectar_mongo()
    if not coleccion:
        print("No se pudo conectar a MongoDB.")
        return

    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    delta = timedelta(days=1)

    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_fin:
        fecha_str = fecha_actual.strftime("%Y-%m-%d")
        compra, venta = obtener_tipo_cambio(fecha_str)

        if compra is not None and venta is not None:
            insertar_datos_mongo(coleccion, fecha_str, compra, venta)
        else:
            print(f"No se pudo obtener el tipo de cambio para {fecha_str}")

        fecha_actual += delta

    print("\nDatos almacenados en MongoDB:")
    mostrar_datos_mongo(coleccion)

if __name__ == "__main__":
    main()
    
# Problema 8

import csv
from pymongo import MongoClient

def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["base_datos"]
        return db["sunat_info"]
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        return None

def obtener_tipo_cambio(coleccion, fecha):
    resultado = coleccion.find_one({"fecha": fecha})
    if resultado:
        return resultado["compra"], resultado["venta"]
    return None, None

def leer_ventas(archivo_csv):
    ventas = []
    try:
        with open(archivo_csv, 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                producto = fila["producto"]
                fecha = fila["fecha"]
                precio_usd = float(fila["precio_usd"])
                ventas.append((producto, fecha, precio_usd))
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no existe.")
    return ventas

def procesar_ventas(ventas, coleccion):
    for producto, fecha, precio_usd in ventas:
        compra, venta = obtener_tipo_cambio(coleccion, fecha)

        if compra and venta:
            precio_soles = precio_usd * venta
            print(f"Producto: {producto} | Fecha: {fecha} | Precio (USD): ${precio_usd:.2f} | Precio (Soles): S/{precio_soles:.2f}")
        else:
            print(f"No se encontró tipo de cambio para la fecha {fecha}")

def main():
    coleccion = conectar_mongo()
    if not coleccion:
        print("No se pudo conectar a la base de datos MongoDB.")
        return

    archivo_ventas = "ventas.csv"
    ventas = leer_ventas(archivo_ventas)

    if ventas:
        procesar_ventas(ventas, coleccion)
    else:
        print("No se encontraron ventas para procesar.")

if __name__ == "__main__":
    main()