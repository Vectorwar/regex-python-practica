""" Ejercicio 5: Analizador y Formateador de Fechas
Autor: Jose Juan Padilla"""

import re
from datetime import datetime # Importa datetime para manejar fechas

def analizar_y_formatear_fechas(texto):
    #  Meses a numeros para facilitar la conversión
    meses_a_numeros = {
        'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
        'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
        'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12',
        'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04', 'may': '05', 'jun': '06',
        'jul': '07', 'ago': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'
    }
    
    # Patrones de expresiones regulares para diferentes formatos de fecha
    patrones = [
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # DD/MM/YYYY
        r'\b\d{4}-\d{1,2}-\d{1,2}\b',  # YYYY-MM-DD
        r'\b\d{1,2}-[a-zA-Z]{3}-\d{4}\b',  # DD-MMM-YYYY
        r'\b[a-zA-Z]+ \d{1,2}, \d{4}\b' # Mes DD, YYYY
    ]
    
    fechas_encontradas = []
    
    # Unir todos los patrones en uno solo
    patron_general = re.compile('|'.join(patrones), re.IGNORECASE)
    
    for match in patron_general.finditer(texto): # Itera sobre todas las coincidencias
        fecha_original = match.group(0) # Fecha encontrada
        
        # Reemplazar nombres de meses por números para el análisis
        fecha_temporal = fecha_original
        for mes, num in meses_a_numeros.items(): # Reemplaza cada mes por su número
            fecha_temporal = re.sub(r'\b' + mes + r'\b', num, fecha_temporal, flags=re.IGNORECASE) # Reemplazo insensible a mayisculas
        
        try:
            # Detectar y convertir la fecha
            if re.match(r'\b\d{1,2}/\d{1,2}/\d{4}\b', fecha_original): 
                fecha_objeto = datetime.strptime(fecha_temporal, '%d/%m/%Y') 
            elif re.match(r'\b\d{4}-\d{1,2}-\d{1,2}\b', fecha_original):
                fecha_objeto = datetime.strptime(fecha_temporal, '%Y-%m-%d')
            elif re.match(r'\b\d{1,2}-[a-zA-Z]{3}-\d{4}\b', fecha_original):
                fecha_objeto = datetime.strptime(fecha_temporal, '%d-%m-%Y')
            elif re.match(r'\b[a-zA-Z]+ \d{1,2}, \d{4}\b', fecha_original):
                fecha_objeto = datetime.strptime(fecha_temporal.replace(',', ''), '%m %d %Y')
            else:
                continue

            fecha_estandar = fecha_objeto.strftime('%Y-%m-%d') # Formatea la fecha a YYYY-MM-DD
            
            fechas_encontradas.append({ # Guarda la fecha original y la estandarizada
                "original": fecha_original,
                "estandar": fecha_estandar
            })

        except ValueError:
            # Ignorar si el formato no es válido (ej. 30 de febrero)
            continue 
            
    return fechas_encontradas # Retorna la lista de fechas encontradas y convertidas

# --- Interfaz de usuario ---
print("¡Bienvenido al Analizador y Formateador de Fechas!")
print("Introduce un texto con fechas en diferentes formatos.")
print("Escribe 'salir' para terminar el programa.")
print("-" * 50)

while True:
    texto_usuario = input("Ingresa tu texto: ") # Solicita texto al usuario
    
    if texto_usuario.lower() == 'salir': # Permite salir del programa
        print("¡Hasta luego! 👋")
        break

    resultados = analizar_y_formatear_fechas(texto_usuario) # Procesa el texto del usuario
    
    if not resultados:
        print("No se encontraron fechas válidas en el texto.") 
    else:
        print("\nFechas encontradas y convertidas:")
        for fecha in resultados: # Muestra cada fecha original y su formato estandarizado
            print(f"- Formato original: {fecha['original']} → Estándar: {fecha['estandar']}")
    
    print("-" * 50)