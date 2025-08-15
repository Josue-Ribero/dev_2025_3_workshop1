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
        decimal = abs(decimal)
        if decimal == 0:
            return "0"
        
        binario = ""
        while decimal > 0:
            residuo = decimal % 2
            binario += str(residuo)
            decimal //= 2
        return binario
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        pass
    
    # Conversiones de numero a alfabeto
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        pass
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    # Conversiones de texto a morse
    def texto_a_morse(self, texto: str):
        texto
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

        textoSeparado = []
        textoEnMorse = []
        textoSeparado.append(texto.split(''))
        for item in textoSeparado:
            if item in morse.keys():
                textoEnMorse.append(morse.values())
                str(textoEnMorse)
        return textoEnMorse

        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass