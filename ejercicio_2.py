"""Extractor de numeros de telefono con Regex
Autor: Jose Juan Padilla"""
import re # Importa el modulo de expresiones regulares

def extraer_numeros(texto):
    patrones = [
        r'\(\d{3}\) \d{3}-\d{4}',  # (123) 456-7890
        r'\d{3}-\d{3}-\d{4}',      # 123-456-7890
        r'\d{3}\s\d{3}\s\d{4}',    # 123 456 7890
        r'\b\d{10}\b'              # 1234567890
    ]
    numeros_encontrados = [] # Lista para almacenar todos los numeros encontrados
   
    for patron in patrones:
        encontrados = re.findall(patron, texto)  # Encuentra todas las coincidencias
        numeros_encontrados.extend(encontrados)  # Agrega a la lista principal    
    
    numeros_unicos = []
    for numero in numeros_encontrados:  # Elimina duplicados
        if numero not in numeros_unicos:  # Verifica si ya está en la lista
            numeros_unicos.append(numero)  # Agrega si no está
    return numeros_unicos

def validar_numero(numero):
    digitos = re.sub(r'\D', '', numero)  # Elimina todo excepto digitos
    return len(digitos) == 10  # Valida que tenga 10 digitos

print("=== Extractor de numeros de telefono ===\n")
print("¿Deseas usar el texto de ejemplo? (s/n): ", end="")
opcion = input().strip().lower()

if opcion == 's':
    texto = "Contacta a Juan al 646-123-4567 o a María al (664) 987-6543. También puedes llamar al 5551234567."
    print(f"\nTexto de ejemplo:\n'{texto}'")
else:
    print("\nIngresa el texto (presiona Enter dos veces para finalizar):\n")
    lineas = []
    contador_enter = 0 # Contador para detectar dos enters consecutivos
    
    while True:
        linea = input()
        if linea == "":
            contador_enter += 1 # Incrementa el contador de enters
            if contador_enter >= 2:  # Dos enters consecutivos para terminar
                break
        else:
            contador_enter = 0  # Resetea el contador si hay texto
            lineas.append(linea)
    
    texto = "\n".join(lineas) # Une las lineas en un solo texto
    
    if not texto.strip():  # Si el texto esta vacio
        print("\n⚠️  No se ingresó ningún texto. Finalizando programa.")
        exit()

# Procesa el texto (ya sea de ejemplo o ingresado)
telefonos = extraer_numeros(texto)
print(f"\n{'='*30}")  # Separador

if telefonos:
    print(f"Números de teléfono encontrados: {len(telefonos)}\n")  # Cuenta los numeros encontrados
    for numero in telefonos:
        validez = "✓ Válido" if validar_numero(numero) else "✗ Inválido"
        digitos = re.sub(r'\D', '', numero)  # Elimina todo excepto digitos
        print(f"{numero:20} -> {validez}")  # Alinea a la izquierda
   
    print(f"\nLista: {telefonos}")
else:
    print("No se encontraron numeros de teléfono.")

print(f"{'='*30}\n")  # Separador

if __name__ == "__main__":
    pass  # Evita ejecución al importar