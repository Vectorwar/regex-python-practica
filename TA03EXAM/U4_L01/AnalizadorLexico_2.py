"""Example 2 - Analizador Léxico Mejorado"""
import re
import os 

class Token:
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna
    
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor}, Linea: {self.linea}, Columna: {self.columna})"

class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1
        self.columna = 1
        
        # Mapeos para categorías
        self.categorias = {
            'KEYWORD': 'PALABRA_RESERVADA',
            'IDENTIFIER': 'IDENTIFICADOR',
            'NUMBER': 'NUMERO',
            'OPERATOR': 'OPERADOR',
            'SEPARATOR': 'SEPARADOR',
            'COMMENT': 'COMENTARIO'
        }
        
        # Mapeos para tipo_a_nombre
        self.tipo_a_nombre = {
            'IDENTIFIER': 'ID',
            'NUMBER': 'NUM',
            'COMMENT': 'COMENTARIO'
        }
        
        # Nombres de tokens
        self.nombres_tokens = {
            '(': 'PA',
            ')': 'PC',
            '{': 'LLA',
            '}': 'LLC',
            ';': 'PYC',
            ',': 'COMA',
            '+': 'MAS',
            '-': 'MENOS',
            '*': 'MULTIPLICACION',
            '/': 'DIVISION',
            '%': 'MODULO',
            '=': 'ASIGNACION',
            '==': 'IGUAL',
            '!=': 'DIFERENTE',
            '<': 'MENOR',
            '>': 'MAYOR',
            '<=': 'MENOR_IGUAL',
            '>=': 'MAYOR_IGUAL',
            '&&': 'AND',
            '||': 'OR',
            '!': 'NOT',
            '++': 'INCREMENTO',
            '--': 'DECREMENTO'
        }
        
        # Mapeos para operadores_categoria
        self.operadores_categoria = {
            '+': 'OPERADOR_ARITMETICO',
            '-': 'OPERADOR_ARITMETICO',
            '*': 'OPERADOR_ARITMETICO',
            '/': 'OPERADOR_ARITMETICO',
            '%': 'OPERADOR_ARITMETICO',
            '==': 'OPERADOR_RELACIONAL',
            '!=': 'OPERADOR_RELACIONAL',
            '<': 'OPERADOR_RELACIONAL',
            '>': 'OPERADOR_RELACIONAL',
            '<=': 'OPERADOR_RELACIONAL',
            '>=': 'OPERADOR_RELACIONAL',
            '&&': 'OPERADOR_LOGICO',
            '||': 'OPERADOR_LOGICO',
            '!': 'OPERADOR_LOGICO',
            '=': 'OPERADOR_ASIGNACION',
            '+=': 'OPERADOR_ASIGNACION',
            '-=': 'OPERADOR_ASIGNACION',
            '*=': 'OPERADOR_ASIGNACION',
            '/=': 'OPERADOR_ASIGNACION',
            '++': 'OPERADOR_INCREMENTO',
            '--': 'OPERADOR_DECREMENTO'
        }
        
        # Patrones para los tokens 
        self.patrones = [
            ('COMMENT', r'/\*[\s\S]*?\*/|//.*'),  
            ('KEYWORD', r'\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NUMBER', r'\d+(\.\d+)?'),
            ('OPERATOR', r'(\+\+|--|<<|>>|<=|>=|==|!=|&&|\|\||[+\-*/%=<>!&|^~])'),
            ('SEPARATOR', r'[;,\(\)\{\}]'),
            ('WHITESPACE', r'\s+'),
            ('NEWLINE', r'\n'),
            ('ERROR', r'.')
        ]

    def tokenizar(self):
        tokens = []
        linea_actual = 1
        
        # Dividir el código en líneas para mejor rastreo
        lineas = self.codigo.split('\n')
        
        for num_linea, linea in enumerate(lineas, start=1):
            columna = 1
            pos_en_linea = 0
            
            while pos_en_linea < len(linea):
                encontrado = False
                
                for tipo, patron in self.patrones:
                    if tipo in ['NEWLINE', 'WHITESPACE']:
                        # Manejar espacios en blanco
                        regex = re.compile(r'\s+')
                        match = regex.match(linea, pos_en_linea)
                        if match:
                            columna += len(match.group(0))
                            pos_en_linea = match.end(0)
                            encontrado = True
                            break
                    else:
                        regex = re.compile(patron)
                        match = regex.match(linea, pos_en_linea)
                        
                        if match:
                            valor = match.group(0)
                            
                            if tipo == 'COMMENT':
                                # Ignorar comentarios, no agregar a tokens
                                columna += len(valor)
                            elif tipo != 'ERROR':
                                # Agregar token con línea y columna correctas
                                tokens.append(Token(tipo, valor, num_linea, columna))
                                columna += len(valor)
                            
                            pos_en_linea = match.end(0)
                            encontrado = True
                            break
                
                if not encontrado:
                    # Caracter no reconocido, avanzar
                    pos_en_linea += 1
                    columna += 1
        
        return tokens

    def obtener_nombre_token(self, token):
        """Obtiene el nombre del token según su tipo y valor"""
        if token.tipo == 'KEYWORD':
            return token.valor.upper()
        
        if token.tipo in ('SEPARATOR', 'OPERATOR'):
            return self.nombres_tokens.get(token.valor, token.valor)
        
        return self.tipo_a_nombre.get(token.tipo, token.tipo)

    def obtener_categoria(self, token):
        """Obtiene la categoría del token"""
        if token.tipo == 'SEPARATOR':
            return 'AGRUPACION'
        
        if token.tipo == 'OPERATOR':
            return self.operadores_categoria.get(token.valor, 'OPERADOR')
        
        return self.categorias.get(token.tipo, token.tipo)

    def generar_tabla_simbolos(self, tokens, archivo_salida='tabla_simbolos.txt'):
        """Genera la tabla de símbolos en un archivo de texto"""
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            # Header
            f.write("=" * 80 + "\n")
            f.write("TABLA DE SÍMBOLOS\n")
            f.write("=" * 80 + "\n\n")
            
            # Títulos de las columnas
            f.write(f"{'Renglón':<10} {'Lexema':<25} {'Token':<20} {'Categoría':<25}\n")
            f.write("-" * 80 + "\n")
            
            # Contenido de la tabla
            for token in tokens:
                if token.tipo != 'COMMENT':
                    nombre_token = self.obtener_nombre_token(token)
                    categoria = self.obtener_categoria(token)
                    f.write(f"{token.linea:<10} {token.valor:<25} {nombre_token:<20} {categoria:<25}\n")
            
            # Footer
            f.write("\n" + "=" * 80 + "\n")
            f.write(f"Total de tokens: {len([t for t in tokens if t.tipo != 'COMMENT'])}\n")
            f.write("=" * 80 + "\n")
        
        print(f"\nTabla de símbolos generada en: {archivo_salida}")


def leer_archivo(ruta_archivo):
    """Lee el contenido del archivo"""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def procesar_codigo(codigo, nombre_base):
    """Procesa el código y genera la tabla de símbolos"""
    print("\n" + "=" * 60)
    print("CÓDIGO FUENTE:")
    print("=" * 60)
    print(codigo)
    print("=" * 60)

    # Analizar
    lexer = AnalizadorLexico(codigo)
    tokens = lexer.tokenizar()  
    print(f"\nTokens generados: {len(tokens)}")
    
    # Generar tabla de símbolos
    archivo_salida = f"{nombre_base}_tabla_simbolos.txt"
    lexer.generar_tabla_simbolos(tokens, archivo_salida)

def menu_principal():
    """Menú del analizador léxico"""
    print("=" * 60)
    print("ANALIZADOR LÉXICO - PARTE 2")
    print("Lectura de archivos y generación de tabla de tokens")
    print("=" * 60)
    
    # Mostrar carpeta actual y archivos disponibles
    carpeta_actual = os.getcwd()
    print(f"\nCarpeta actual: {carpeta_actual}")
    print("\nArchivos disponibles en esta carpeta:")
    archivos = [f for f in os.listdir('.') if os.path.isfile(f)]
    if archivos:
        for archivo in archivos[:10]:  # Mostrar máximo 10 archivos
            print(f"  - {archivo}")
        if len(archivos) > 10:
            print(f"  ... y {len(archivos) - 10} archivos más")
    else:
        print("  (No hay archivos en esta carpeta)")
    
    print("\nEjemplos de rutas válidas:")
    print("  - Misma carpeta: codigo.c")
    print("  - Subcarpeta: archivos/codigo.c")
    print("  - Ruta absoluta: C:/Users/TuUsuario/codigo.c")
    print("-" * 60)
    
    while True:
        ruta = input("\nIngresa la ruta del archivo (o 'salir' para terminar): ").strip()
        
        if ruta.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not ruta:
            print("Error: Debes ingresar una ruta válida")
            continue
        
        # Mostrar ruta absoluta para verificar
        ruta_abs = os.path.abspath(ruta)
        print(f"\nBuscando archivo en: {ruta_abs}")
        
        if not os.path.exists(ruta):
            print(f"❌ El archivo no existe en esa ubicación")
            print(f"\n¿Deseas intentar con otra ruta? (s/n): ", end='')
            if input().lower() != 's':
                break
            continue
        
        # Verificar si es una carpeta en lugar de un archivo
        if os.path.isdir(ruta):
            print(f"❌ Error: '{ruta}' es una carpeta, no un archivo")
            print("\nArchivos disponibles en esta carpeta:")
            archivos_c = [f for f in os.listdir(ruta) if f.endswith(('.c', '.txt', '.cpp'))]
            if archivos_c:
                for archivo in archivos_c:
                    print(f"  - {archivo}")
                print(f"\nEjemplo de ruta correcta: {os.path.join(ruta, archivos_c[0])}")
            else:
                print("  (No hay archivos .c, .cpp o .txt en esta carpeta)")
            print(f"\n¿Deseas intentar con otra ruta? (s/n): ", end='')
            if input().lower() != 's':
                break
            continue
        
        codigo = leer_archivo(ruta)
        
        if codigo:
            nombre_base = os.path.splitext(os.path.basename(ruta))[0]
            procesar_codigo(codigo, nombre_base)
            break
        
if __name__ == "__main__":
    menu_principal()