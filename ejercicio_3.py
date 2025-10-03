"""Ejercicio 3: Validador de Contraseñas
Autor: Jose Juan Padilla"""

import re

def validador_contrasena(contrasena): # Funcion para validar la contraseña
    
    # Define la expresión regular para todos los criterios
    patron = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&#])[A-Za-z0-9@$!%*?&#]{8,}$')
    
    # Inicializa las banderas de validacion y la lista de errores
    es_valida = True # Asume que es valida hasta demostrar lo contrario
    errores = [] # Lista para almacenar mensajes de error

    # Se usa la función search() para encontrar el patrón en la cadena
    if not patron.search(contrasena):
        es_valida = False
        
        # Validació=on individual para generar mensajes de error específicos
        if len(contrasena) < 8: #verifica longitud
            errores.append("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[a-z]', contrasena): #verifica minusculas
            errores.append("La contraseña debe contener al menos una letra minuscula.")
        if not re.search(r'[A-Z]', contrasena):#verifica mayusculas
            errores.append("La contraseña debe contener al menos una letra mayuscula.")
        if not re.search(r'[0-9]', contrasena):#verifica numeros
            errores.append("La contraseña debe contener al menos un numero.")
        if not re.search(r'[@$!%*?&#]', contrasena):#verifica caracteres especiales
            errores.append("La contraseña debe contener al menos un caracter especial (@$!%*?&#).")
            
    return es_valida, errores # Retorna si es valida y los errores encontrados

# --- Casos de prueba ---

contrasenas_a_probar = [ # Lista de contraseñas para probar
    "Segura123!", 
    "contrasena",
    "MAYUSCULA123!",
    "P@ssw0rd" ,
]

print("¡Bienvenido al validador de contraseñas seguras!")
print("Introduce 'salir' para finalizar el programa.")
print("-" * 50)
print("Probando contraseñas predefinidas:", contrasenas_a_probar)
print("-" * 50)

while True:
    contrasena_usuario = input("Introduce una contraseña para validar: ")

    if contrasena_usuario.lower() == 'salir':
        print("¡Gracias por usar el validador!")
        break

    valido, errores = validador_contrasena(contrasena_usuario)
    
    if valido:
        print(f'✅ "{contrasena_usuario}" → Contraseña válida. ¡Es segura!')
    else:
        print(f'❌ "{contrasena_usuario}" → Contraseña inválida. Errores:')
        for error in errores:
            print(f'  - {error}')
    
    print("-" * 50)