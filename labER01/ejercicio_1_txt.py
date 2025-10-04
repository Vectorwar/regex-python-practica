"""
Ejercicio 1: Validador de correos electrónicos con Regex
Autor: Jose Juan Padilla
"""
import re
import matplotlib.pyplot as plt

def validar_correo(correo):
    """Valida un correo usando expresiones regulares"""
    patron = r'^\d+\.\s*[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(com|mx|org|net|edu|gob)$'
    return re.match(patron, correo) is not None

# Programa principal
print("=== Validador de correos electronicos ===\n")

validos = 0
invalidos = 0
with open('correos.txt', 'r') as archivo:
    for linea in archivo:
        correo = linea.strip() # elimnar espacios en blanco y saltos de linea
        if correo:
            if validar_correo(correo):
                print(f"✓ '{correo}' es un correo válido")
                validos += 1 # Incrementa contador de validos
            else:
                print(f"✗ '{correo}' NO es un correo válido")
                invalidos += 1 # Incrementa contador de invalidos

print("Total de correos validos:", validos)
print("Total de correos invalidos:", invalidos)

plt.bar(["Correos validos", "Correos invalidos"], [validos, invalidos])
plt.ylabel("Cantidad")
plt.title("Validación de Correos Electrónicos")
plt.show()
