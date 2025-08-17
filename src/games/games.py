class Games:
    def piedra_papel_tijera(self, jugador1: str, jugador2: str):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        reglas = {
            "piedra":"tijera",
            "tijera":"papel",
            "papel":"piedra"
        }

        validos = ("piedra", "papel", "tijera")

        # Caso de invalidez
        if jugador1 not in validos or jugador2 not in validos:
            return "invalid"
        
        # Empate
        if jugador1 == jugador2:
            return "empate"
        
        # Gana jugador 1
        if reglas[jugador1] == jugador2:
            return "jugador1"
        
        # Gana jugador 2
        return "jugador2"
    
    
    def adivinar_numero_pista(self, numero_secreto: int, intento: int):
        if intento == numero_secreto:
            return "correcto"
        elif intento < numero_secreto:
            return "muy bajo"
        elif intento > numero_secreto:
            return "muy alto"
        
    
    def ta_te_ti_ganador(self, tablero):

        # Revisar las filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]
        
        # Revisar las columnas
        for columna in range(3):
            if tablero[0][columna] != " " and tablero[0][columna] == tablero[1][columna] == tablero[2][columna]:
                return tablero[0][columna]
        
        # Revisar si es empate o continua
        for fila in tablero:
            if " " in fila:
                return "continua"
        
        # Revisar la primer diagonal
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]
        
        # Revisar la segunda diagonal
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]
        
        # En caso de empate
        return "empate"
    

    def generar_combinacion_mastermind(self, longitud: int, colores_disponibles: list):
        # Importacion de libreria para valor aleatorio
        import random
        if longitud == 0:
            return []

        # Generar combinacion aleatoria
        combinacion = [random.choice(colores_disponibles) for i in range(longitud)]
        return combinacion


    def validar_movimiento_torre_ajedrez(self, desde_fila: int, desde_col: int, hasta_fila: int, hasta_col: int, tablero: list):
        # Verificacion de límites y reglas de movimiento
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        
        # Reglas de movimiento horizontal y vertical
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        # Verificacion de que no este en el mismo lugar
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        # Verificacion de que no haya piezas en el camino
        if desde_fila == hasta_fila: # Movimiento horizontal
            if hasta_col > desde_col:
                paso = 1
            else:
                paso = -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
                
        elif desde_col == hasta_col: # Movimiento vertical
            if hasta_fila > desde_fila:
                paso = 1
            else:
                paso = -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
        
        return True