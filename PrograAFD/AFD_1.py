""""Diseño de un AFD que acepte todas las cadenas sobre {a,b
que contengan la subcadena 'aba'.}"""

def validar(AFD, palabra):
    estado_actual = AFD['estado_inicial']
    for simbolo in palabra:
        if simbolo not in AFD['alfabeto']:
            return False, f"Este {simbolo} no es parte del alfabeto"
        
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
    'alfabeto': {'a', 'b'},
    # Estados del automata
    'estados': {'q0', 'q1', 'q2', 'q3'},
    # Transiciones del automata
    'transiciones': {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q1', 'b': 'q2'},  
        'q2': {'a': 'q3', 'b': 'q0'},
        'q3': {'a': 'q3', 'b': 'q3'}
    },
    # Estado inicial y final
    'estado_inicial': 'q0',
    'estado_final': 'q3'
}

# Programa principal
palabra = input("Ingresa palabra sobre el alfabeto {a,b}: Considera que esta para hser aceptada debe contener la subcadena 'aba'\n")
print(f"\nEvaluando la palabra: {palabra}\n")
resultado = validar(AFD, palabra)
print(f"\nResultado: {resultado}")