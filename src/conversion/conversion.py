class Conversion:
    # Conversiones de temperatura
    def celsius_a_fahrenheit(self, celsius):

        farenheit = (celsius * 9/5) + 32
        return farenheit

    def fahrenheit_a_celsius(self, fahrenheit):

        celsius = (fahrenheit - 32) * 5/9
        return celsius
    

    #Conversiones de distancia
    def metros_a_pies(self, metros):

        pies = (metros * 3.28084)
        return pies
    
    def pies_a_metros(self, pies):

        metros = (pies / 3.28084)
        return metros
    

    #Conversiones de sistemas numericos
    def decimal_a_binario(self, decimal):
        # Caso donde se coloca 0
        if decimal == 0:
            return "0"
        
        #String a retornar
        binario = ""
        # Se hace division para tomar los residuos
        while decimal > 0:
            # Se halla el residuo de la division por 2 (1 o 0)
            residuo = decimal % 2

            # Se agrega el numero al inicio de la cadena
            binario = str(residuo) + binario

            # Se actualiza el valor de la variable decimal
            decimal = decimal // 2
        return binario
        
    
    def binario_a_decimal(self, binario):
        decimal = 0
        longitud = len(binario)

        # Se itera n veces segun el tamano del string
        for i in range(longitud):
            # Se le asigna el valor de la posicion en el texto
            digito = int(binario[i])

            # Calcula la potencia de dos que corresponde
            decimal += digito * (2 ** (longitud - 1 - i))
        return decimal
    

    # Conversiones de numero a alfabeto
    def decimal_a_romano(self, numero):
        # Diccionarios de equivalencias
        unidades = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
            6: "VI", 7: "VII", 8: "VIII", 9: "IX"
        }

        decenas = {
            1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L",
            6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"
        }

        centenas = {
            1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D",
            6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"
        }

        millares = {
            1: "M", 2: "MM", 3: "MMM"
        }

        # Determina si un numero tiene miles por una division entera
        millar = numero // 1000

        # Determina si un numero tiene centenas por una division entera
        centenar = (numero % 1000) // 100

        # Determina si un numero tiene decenas por una division entera
        decena = (numero % 100) // 10

        # Determina si un numero tiene unidades por una division entera
        unidad = numero % 10

        romano = ""

        # Si tiene miles
        if millar > 0:
            romano += millares[millar]
        
        # Si tiene centenas
        if centenar > 0:
            romano += centenas[centenar]

        # Si tiene decenas
        if decena > 0:
            romano += decenas[decena]

        # Si tiene unidades
        if unidad > 0:
            romano += unidades[unidad]
        
        return romano
    
    def romano_a_decimal(self, romano):

        # Diccionarios de equivalencias invertidos
        valores = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
        }

        # Valor que retornara
        total = 0
        # Iterador
        i = 0
        longitud = len(romano)

        # Itera una vez menos que la longitud
        while i < longitud:
            # Si no es el ultimo caracter y el valor actual es menor que el siguiente, se resta
            if i + 1 < longitud and valores[romano[i]] < valores[romano[i + 1]]:
                total += valores[romano[i + 1]] - valores[romano[i]]
                i += 2 # Avanza de a dos caracteres
            
            # Si es el ultimo caracter o el actual no es menor que el siguiente
            else:
                total += valores[romano[i]]
                i += 1
        return total
    

    # Conversiones de texto a morse
    def texto_a_morse(self, texto: str):
        # En caso de que este vacio
        if texto == "":
            return ""
        morse = {
            # Letras
            'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
            'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
            'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
            'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
            'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',

            # Números y espacio
            '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
            '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
            '8': '---..',  '9': '----.', ' ': '/'
        }

        textoEnMorse = []
        # Normaliza los caracteres en mayuscula
        for caracter in texto.upper():
            if caracter in morse:
                # Inserta el valor que encuentra dentro del diccionario
                textoEnMorse.append(morse[caracter])
        # Retorna un string con los valores de la lista
        return ' '.join(textoEnMorse)
    
    
    def morse_a_texto(self, morse: str):
        # En caso de que este vacio
        if morse == "":
            return ""

        # Diccionario de morse a texto
        morse_invertido = {
            # Letras
            '.-': 'A',     '-...': 'B',   '-.-.': 'C',   '-..': 'D',
            '.': 'E',      '..-.': 'F',   '--.': 'G',    '....': 'H',
            '..': 'I',     '.---': 'J',   '-.-': 'K',    '.-..': 'L',
            '--': 'M',     '-.': 'N',     '---': 'O',    '.--.': 'P',
            '--.-': 'Q',   '.-.': 'R',    '...': 'S',    '-': 'T',
            '..-': 'U',    '...-': 'V',   '.--': 'W',    '-..-': 'X',
            '-.--': 'Y',   '--..': 'Z',

            # Números y espacio
            '-----': '0',  '.----': '1',  '..---': '2',  '...--': '3',
            '....-': '4',  '.....': '5',  '-....': '6',  '--...': '7',
            '---..': '8',  '----.': '9',  '/': ' '
        }

        # Separacion del codigo solo por espacios
        simbolos = morse.strip().split(" ")
        morseEnTexto = []
        for simbolo in simbolos:
            # Revisa si existe ese codigo
            if simbolo in morse_invertido:
                # Inserta el valor que encuentra dentro del diccionario
                morseEnTexto.append(morse_invertido[simbolo])
        # Retorna un string con los valores de la lista
        return ''.join(morseEnTexto)