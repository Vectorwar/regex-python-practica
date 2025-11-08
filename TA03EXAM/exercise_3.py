"""Ejercicio 3: Cadenas sin subcadena "11"
Diseñar un AFD que acepte todas las cadenas sobre el alfabeto {0, 1} que 
NO contengan la subcadena "11" (es decir, que no tengan dos unos consecutivos)."""

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
    'alfabeto': {'0', '1'},
    # Estados del automata
    'estados': {'q0', 'q1', 'q2'},
    # Transiciones del automata
    'transiciones': {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'}  
    },
    # Estado inicial y final
    'estado_inicial': 'q0',
    'estado_final': {'q0','q1'} 

}

# Programa principal
palabra = input("Ingresa palabra sobre el alfabeto {0,1}:Considera que esta para ser aceptada NO debe contener una subcadena {11} consecutiva\n")

print(f"\nEvaluando la palabra: {palabra}\n")
resultado = validar(AFD, palabra)
print(f"\nResultado: {resultado}")