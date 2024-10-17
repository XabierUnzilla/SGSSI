import os
import hashlib
import subprocess

# 1. Calcular el hash MD5 de un archivo
def calcular_md5(archivo):
    hash_md5 = hashlib.md5()
    with open(archivo, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 2. Buscar el archivo que corresponde con el hash MD5 proporcionado
def buscar_imagen_por_hash(directorio, hash_objetivo):
    for root, dirs, files in os.walk(directorio):
        for archivo in files:
            ruta_archivo = os.path.join(root, archivo)
            hash_md5 = calcular_md5(ruta_archivo)
            if hash_md5 == hash_objetivo:
                print(f"¡Archivo encontrado!: {ruta_archivo}")
                return ruta_archivo
    return None

# Solicitar la ruta de la carpeta y el hash MD5 desde la consola
directorio_imagenes = input("Introduce la ruta del directorio donde están las imágenes: ")
hash_objetivo = input("Introduce el hash MD5 objetivo: ")

# Paso 1 y 2: Buscar el archivo que corresponde con el hash MD5 proporcionado
imagen_con_hash = buscar_imagen_por_hash(directorio_imagenes, hash_objetivo)


