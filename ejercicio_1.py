"""
Ejercicio 1: Validador de correos electrónicos con Regex
Autor: Jose Juan Padilla
"""
import re

def validar_correo(correo):
    """Valida un correo usando expresiones regulares"""
    patron = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(com|mx|org|net|edu|gob)$'
    return re.match(patron, correo) is not None

# Programa principal
print("=== Validador de correos electronicos ===\n")
correo = input("Ingresa un correo electronico: ")

if validar_correo(correo):
    print(f"✓ '{correo}' es un correo valido")
else:
    print(f"✗ '{correo}' NO es un correo valido")

# Ejemplos de prueba
print("\n--- Ejemplos de prueba ---")
ejemplos = [
    "usuario@ejemplo.com",
    "nombre.apellido@dominio.mx",
    "usuarioejemplo.com",
    "@ejemplo.com"
]
# Validar y mostrar resultados de los ejemplos
for ejemplo in ejemplos:
    resultado = "✓ Valido" if validar_correo(ejemplo) else "✗ Invalido"
    print(f"{ejemplo:30} -> {resultado}") 
