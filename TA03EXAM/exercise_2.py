"""Ejercicio 2: Número impar de 'b's

Diseñar un AFD que acepte todas las cadenas sobre el alfabeto {a, b} que contengan un número impar de 'b's."""

def validar(AFD, palabra):
    estado_actual = AFD['estado_inicial']
    for simbolo in palabra:
        if simbolo not in AFD['alfabeto']:
            return False, (f"Este {[simbolo]} no es parte del alfabeto")
        estado_actual = AFD['transiciones'][estado_actual][simbolo]
        print(f"El simbolo: {simbolo} --> Estado actual: {estado_actual}")
    
    if estado_actual in AFD['estado_final']:
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
    'estados': {'q0', 'q1'},
    # Transiciones del automata
    'transiciones': {
        'q0': {'a': 'q0', 'b': 'q1'},
        'q1': {'a': 'q1', 'b': 'q0'},  
    },
    # Estado inicial y final
    'estado_inicial': 'q0',
    'estado_final': {'q1'} 

}

# Programa principal
palabra = input("Ingresa palabra sobre el alfabeto {a,b}:Considera que esta para ser aceptada debe contener un numero impar de b's\n")

print(f"\nEvaluando la palabra: {palabra}\n")
resultado = validar(AFD, palabra)
print(f"\nResultado: {resultado}")