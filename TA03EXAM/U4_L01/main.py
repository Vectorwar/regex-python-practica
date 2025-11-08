
"""Ejemplo práctico:

Entrada: float precio = 99.99;

Salida del analizador léxico:"""

import re
#Esta es la definicion de los patrones para los tokens
class Token:
    def __init__(self, tipo, valor,linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
    # Ayuda a imprimir el token de manera legible
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor}, {self.linea})"

class AnalizadorLexico:
    def __init__(self, codigo): # Inicializa el analizador léxico con el código fuente
        self.codigo = codigo # Codigo fuente a analizar
        self.pos = 0 # Posicion actual en el codigo fuente
        self.linea = 1 # Numero de linea actual
        
        # diccionario de patrones para los tokens
        self.patrones = [
            ('KEYWORD', r'\b(float|int|if|else|while|return)\b'),#palabras reservadas
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), #identificadores
            ('NUMBER', r'\d+(\.\d+)?'), #números enteros y flotantes
            ('OPERATOR', r'[+\-*/=<>!]'), #operadores aritméticos y de asignación
            ('SEPARATOR', r'[;,\(\)\{\}]'), #dos puntos, comas, paréntesis, llaves
            ('WHITESPACE', r'\s+'),# Espacios en blanco (se ignoran)d
            ('NEWLINE', r'\n'),# saltos de línea
            ('ERROR', r'.') #cualquier otro caracter no reconocido
        ]
    # Metodo para tokenizar el codigo fuente
    def tokenizar(self):
        tokens = [] # Lista para almacenar los tokens generados
        while self.pos < len(self.codigo): # Mientras no se alcance el final del codigo fuente
            encontrado = False # Bandera para verificar si se encontro un patron
            for tipo, patron in self.patrones: # Iterar sobre los patrones definidos
                regex = re.compile(patron)
                match = regex.match(self.codigo, self.pos)
                
                if match: # Si se encuentra una coincidencia
                    valor = match.group(0)
                    if tipo == 'NEWLINE': # Manejar saltos de línea
                        self.linea += 1
                    elif tipo not in ['WHITESPACE']: # Ignorar espacios en blanco
                        tokens.append(Token(tipo, valor, self.linea))
                        
                    self.pos = match.end(0) # Avanzar la posición en el código fuente
                    encontrado = True #true si se encontro un patron
                    break
            if not encontrado: # Si no se encuentra ninguna coincidencia, avanzar un caracter
                self.pos += 1
        return tokens
    
# Ejemplo de uso del ejemplo teorico
print("=" * 50)
print("Ejemplo práctico de Analizador Lexico")
print("=" * 50)

codigo1 = "float precio = 99.99;" #Codigo fuente de ejemplo
lexer1 = AnalizadorLexico(codigo1)
tokens1 = lexer1.tokenizar()

print(f"Codigo fuente \n{codigo1}\n")
print("\nTokens generados:")
for token in tokens1: # Imprimir cada token generado
        print(token)