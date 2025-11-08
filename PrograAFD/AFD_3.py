
"""Diseño de un AFD que acepte todas las cadenas sobre {a,b} que contengan un numero 
par de a's. incluyendo 0 a's."""

def validar(AFD, palabra):
    estado_actual = AFD['estado_inicial']
    for simbolo in palabra:
        if simbolo not in AFD['alfabeto']:
            return False, f"El simbolo {simbolo} no es parte del alfabeto"
        estado_actual = AFD['transiciones'][estado_actual][simbolo]
        print(f"El simbolo: {simbolo} --> Estado actual: {estado_actual}")
    
    if estado_actual == AFD['estado_final']:
        print(f"La cadena {palabra} es aceptada")
        return True
    else:
        print(f"La cadena {palabra} no es aceptada")
        return False

AFD = {
    'alfabeto': {'a', 'b'},
    'estados': {'q0', 'q1'},
    'transiciones': {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q0', 'b': 'q1'}
     },
    'estado_inicial': 'q0',
    'estado_final': 'q0'
}

palabra = input("Ingresa una palabra sobre el alfabeto {a,b}: considera que la cantidad de a's debe ser par\n")
print(f"\nEvaluando la palabra: {palabra}\n")
resultado = validar(AFD, palabra)
print(f"\nResultado: {resultado}")