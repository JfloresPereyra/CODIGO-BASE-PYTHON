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
                estado = 1  # Identificador
            elif c.isdigit():
                estado = 2  # Número (entero)
            elif c in operadores:
                estado = 4  # Operador
            else:
                return "No válido / Desconocido"

        elif estado == 1:  # Procesando identificador
            if not (c.isalnum() or c == '_'):
                return "Identificador no válido"

        elif estado == 2:  # Procesando número
            if c == '.':
                estado = 3  # Transición a decimal
            elif not c.isdigit():
                return "Número no válido"

        elif estado == 3:  # Procesando parte decimal
            if not c.isdigit():
                return "Número decimal no válido"

        elif estado == 4:  # Procesando operador
            return "Operador no válido (demasiados caracteres)"

        i += 1

    # Clasificación final según el estado en el que terminó
    if estado == 1:
        return "Identificador válido"
    elif estado in (2, 3):
        return "Número válido"
    elif estado == 4:
        return "Operador válido"
    return "Cadena no válida"


# --- Pruebas ---
entradas = ["variable1+", "125", "45.67", "+", "_contador", "99num", "++"]
for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")
