"""Ejercicio 1: Cadenas que contienen "01" y terminan en "0"

Diseñar un AFD que acepte todas las cadenas sobre el alfabeto {0, 1} que contengan la subcadena "01" y además terminen en "0"."""

def validar(AFD, palabra):
    estado_actual = AFD['estado_inicial']
    for simbolo in palabra:
        if simbolo not in AFD['alfabeto']:
            return False, (f"Este {[simbolo]} no es parte del alfabeto")
        
        estado_actual = AFD['transiciones'][estado_actual][simbolo]
        print(f"El simbolo: {simbolo} --> Estado actual: {estado_actual}")
    
    if estado_actual == AFD['estado_final']:
        print(f"La cadena '{palabra}' es aceptada")
        return True
    else:
        print(f"La palabra '{palabra}' no es aceptada")
        return False

# Definición del AFD
AFD = {
    # Alfabeto del automata
    'alfabeto': {'0', '1'},
    # Estados del automata
    'estados': {'q0', 'q1', 'q2', 'q3'},
    # Transiciones del automata
    'transiciones': {
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q1', '1': 'q2'},  
        'q2': {'0': 'q3', '1': 'q2'},
        'q3': {'0': 'q3', '1': 'q2'}
    },
    # Estado inicial y final
    'estado_inicial': 'q0',
    'estado_final': 'q3'
}

# Programa principal
palabra = input("Ingresa palabra sobre el alfabeto {0,1}:Considera que esta para ser aceptada debe contener la subcadena '01' y terminar en 0\n")

print(f"\nEvaluando la palabra: {palabra}\n")
resultado = validar(AFD, palabra)
print(f"\nResultado: {resultado}")