""" Ejercicio 4: Extracción de URLs y Dominios
Autor: Jose Juan Padilla"""

import re

def extraer_urls(texto):

    # Expresion regular para detectar URLs en diferentes formatos
    patron = re.compile(r'(?P<protocolo>https?://)?(?P<dominio>[a-zA-Z0-9.-]+.[a-zA-Z]{2,})(?P<ruta>/[^\s]*)?')
    
    urls_encontradas = []
    
    # Usa finditer para encontrar todas las coincidencias en el texto
    for match in patron.finditer(texto):
        url_completa = match.group(0)
        
        # Obtener los componentes usando los nombres de grupo usando match
        protocolo = match.group('protocolo')
        dominio = match.group('dominio')
        ruta = match.group('ruta') 
        
        # Guardar la informacion en un diccionario y agregar a la lista
        url_info = {
            "url_completa": url_completa,
            "protocolo": protocolo if protocolo else "No especificado",
            "dominio": dominio if dominio else "No encontrado",
            "ruta": ruta if ruta else "No especificada"
        }
        
        urls_encontradas.append(url_info)
        
    return urls_encontradas # Retorna la lista de URLs encontradas

# --- Interfaz de usuario ---

print("¡Bienvenido al extractor de URLs y dominios!")
print("Puedes ingresar una o varias URLs en un texto.")
print("Escribe 'salir' en cualquier momento para terminar.")

print("*" * 50)

print("Ejemplos de URLs que puedes probar: Visita https://www.google.com o http://github.com/usuario. También puedes ir a www.python.org para más info.)")

print("*" * 50)

while True:
    texto_usuario = input("Introduce un texto con URLs: ") # Solicita texto al usuario
    
    if texto_usuario.lower() == 'salir': # Permite salir del programa
        print("¡Gracias por usar el extractor! 👋")
        break
    
    # Procesa el texto del usuario
    urls_extraidas = extraer_urls(texto_usuario)
    
    if not urls_extraidas:
        print("😔 No se encontraron URLs válidas en el texto ingresado.")
    else:
        for i, url in enumerate(urls_extraidas):
            print(f"\n--- URL {i+1} ---")
            print(f"URL Completa: {url['url_completa']}")
            print(f"  - Protocolo: {url['protocolo']}")
            print(f"  - Dominio: {url['dominio']}")
            
            # Muestra la ruta solo si existe
            if url['ruta'] != "No especificada":
                print(f"  - Ruta: {url['ruta']}")
    
    print("*" * 50)