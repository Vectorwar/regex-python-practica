"""Example 2 """
import re
class Token:
    def __init__(self, tipo, valor,linea,columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna #ayuda a identificar la posicion del token en la linea
    # Ayuda a imprimir el token de manera legible
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor}, {self.linea})"

class AnalizadorLexico:
    def __init__(self, codigo): # Inicializa el analizador léxico con el código fuente
        self.codigo = codigo # Codigo fuente a analizar
        self.pos = 0 # Posicion actual en el codigo fuente
        self.linea = 1 # Numero de linea actual
        self.columna = 1
        
        # diccionario de patrones para los tokens
        self.patrones = [
            ('KEYWORD', r'\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b'),            
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), #identificadores
            ('NUMBER', r'\d+(\.\d+)?'), #números enteros y flotantes
            ('OPERATOR', r'[+\-*/=<>!]'), #operadores aritméticos y de asignación
            ('SEPARATOR', r'[;,\(\)\{\}]'), #dos puntos, comas, paréntesis, llaves
            ('WHITESPACE', r'\s+'),# Espacios en blanco (se ignoran)
            ('COMMENT', r'//.?$|/\.?\/'), #comentarios de una y varias lineas            
            ('NEWLINE', r'\n'),# saltos de línea
            ('ERROR', r'.') #cualquier otro caracter no reconocido
        ]
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
                        self.columna = 1
                    elif tipo not in ['WHITESPACE']: # Ignorar espacios en blanco
                        tokens.append(Token(tipo, valor, self.linea,self.columna))
                        
                    self.pos = match.end(0) # Avanzar la posición en el código fuente
                    encontrado = True #true si se encontro un patron
                    break
            if not encontrado: # Si no se encuentra ninguna coincidencia, avanzar un caracter
                self.pos += 1
        return tokens
    
print("\n" + "=" * 50)
print("EJEMPLO 4: Programa completo")
print("=" * 50)

codigo4 = """int suma = 0;
for (i = 1; i < 10; i = i + 1) {
    suma = suma + i;
}
return suma;"""

lexer4 = AnalizadorLexico(codigo4)
tokens4 = lexer4.tokenizar()

print(f"Código fuente:\n{codigo4}")
print(f"\nTotal de tokens generados: {len(tokens4)}")
print("\nTokens generados:")
for token in tokens4:
    print(token)