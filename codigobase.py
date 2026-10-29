# NOMBRES: Univ.Flores Pereyra Jairo Jesus
#  		   Univ.Flores Valencia Gonsalo
palabras_reservadas = {
    'if', 'else', 'elif', 'while', 'for', 'int', 'float',
    'return', 'def', 'class', 'print', 'break', 'continue'
}

def analizar_token(cadena):
    cadena = cadena.strip()
    if not cadena:
        return "Cadena vacía"

    estado = 0
    i = 0
    operadores = {'+', '-', '*', '/', '=', '<', '>', '%'}

    while i < len(cadena):
        c = cadena[i]

        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1  # Identificador / palabra reservada
            elif c.isdigit():
                estado = 2  # Número entero
            elif c in operadores:
                estado = 4  # Operador
            else:
                return "No válido / Desconocido"

        elif estado == 1:  # Procesando identificador
            if not (c.isalnum() or c == '_'):
                return "Identificador no válido"

        elif estado == 2:  # Procesando número entero
            if c == '.':
                estado = 3  
            elif not c.isdigit():
                return "Número no válido"

        elif estado == 3:  
            if c.isdigit():
                estado = 5  
            else:
                return "Número real no válido"

        elif estado == 4: 
            return "Operador no válido (demasiados caracteres)"

        elif estado == 5: 
            if not c.isdigit():
                return "Número real no válido"

        i += 1

    # Clasificación final según el estado en el que terminó
    if estado == 1:
        if cadena in palabras_reservadas:
            return "Palabra reservada"
        return "Identificador válido"
    elif estado == 2:
        return "Número entero válido"
    elif estado == 3:
        return "Número real no válido (faltan los numeros despues del .)"
    elif estado == 5:
        return "Número real válido"
    elif estado == 4:
        return "Operador válido"
    return "Cadena no válida"

entradas = ["variable1+", "125", "45.67", "45.", "+", "_contador", "99num", "++", "while", "int", "Int"]
for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")
