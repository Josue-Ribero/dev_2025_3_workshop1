class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto: str):
        texto = texto.lower().replace(" ", "")
        textoInvertido = texto[::-1]
        return texto == textoInvertido
        
    
    def invertir_cadena(self, texto):
        texto = texto[::-1]
        return texto
    
    
    def contar_vocales(self, texto: str):
        vocales = "aeiou"
        texto = texto.lower()
        contador = 0
        for vocal in texto:
            if vocal in vocales:
                contador += 1
        return contador
        
    
    def contar_consonantes(self, texto: str):
        consonantes = "bcdfghjklmnpqrstvwxyz"
        texto = texto.lower()
        contador = 0
        for consonante in texto:
            if consonante in consonantes:
                contador += 1
        return contador
        
    
    def es_anagrama(self, texto1: str, texto2: str):
        # Ordena, coloca en minuscula y elimina espacios
        texto1 = sorted(texto1.lower().replace(" ", ""))
        texto2 = sorted(texto2.lower().replace(" ", ""))

        if texto1 == texto2:
            return True
        return False
        
    
    def contar_palabras(self, texto: str):
        # Elimina espacios al inicio y al final, y divide por espacios
        texto = texto.split()
        return len(texto)
    
    def palabras_mayus(self, texto: str):
        if texto == "":
            return ""
        
        # Convierte cada palabra a mayúscula manteniendo los espacios
        palabras = texto.split(" ")
        resultado = []
        for palabra in palabras:
            if palabra:
                # Convierte la primera letra a mayúscula y el resto a minúscula
                resultado.append(palabra.capitalize())
            else:
                # Agrega un espacio al final si el texto no estaba vacío
                resultado.append("")
        
        # Une las palabras con un espacio
        return " ".join(resultado)
    
    
    def eliminar_espacios_duplicados(self, texto: str):
        # Revisa si la cadena está vacía
        if texto == "":
            return ""
        
        # Lista para construir la nueva cadena sin espacios duplicados
        resultado = []
        anteriorEspacio = False

        # Recorre cada carácter en el texto
        for letra in texto:
            # Si hay un espacio y el anterior no era espacio, lo añade
            if letra == " ":
                if not anteriorEspacio:
                    resultado.append(letra)
                    anteriorEspacio = True

            # Si no es espacio, lo añade y resetea el indicador
            else:
                resultado.append(letra)
                anteriorEspacio = False

        # Une la lista en una cadena y la retorna como
        return "".join(resultado)
        
    
    def es_numero_entero(self, texto):
        # Verifica si la cadena se puede convertir a numero entero
        try:
            int(texto)
            return True
        # Si no se puede convertir, retorna False
        except ValueError:
            return False
        
    
    def cifrar_cesar(self, texto, desplazamiento):
        # Se inicializa la cadena resultado
        resultado = ""

        # Recorre cada letra del texto
        for letra in texto:
            # Si es letra, se desplaza; si no, se deja igual
            if 'a' <= letra <= 'z':
                # convierte la letra en ASCII, la desplaza y vuelve a convertir a caracter
                resultado += chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))

            elif 'A' <= letra <= 'Z':
                # convierte la letra en ASCII, la desplaza y vuelve a convertir a caracter
                resultado += chr((ord(letra) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                resultado += letra
        return resultado
        
    
    def descifrar_cesar(self, texto, desplazamiento):
        # Se inicializa la cadena resultado
        resultado = ""

        # Recorre cada letra del texto
        for letra in texto:
            # Si es letra, se desplaza; si no, se deja igual
            if 'a' <= letra <= 'z':
                # convierte la letra en ASCII, la desplaza y vuelve a convertir a caracter
                resultado += chr((ord(letra) - ord('a') - desplazamiento) % 26 + ord('a'))

            elif 'A' <= letra <= 'Z':
                # convierte la letra en ASCII, la desplaza y vuelve a convertir a caracter
                resultado += chr((ord(letra) - ord('A') - desplazamiento) % 26 + ord('A'))
            else:
                resultado += letra
        return resultado
        
    
    def encontrar_subcadena(self, texto, subcadena):
        # Verifica si la subcadena está vacía
        if not subcadena:
            return []
        
        # Lista para almacenar las posiciones donde se encuentra la subcadena
        posiciones = []
        longitudTexto = len(texto)
        longitudSubcadena = len(subcadena)

        # Recorre el texto hasta donde la subcadena puede caber
        for i in range(longitudTexto - longitudSubcadena + 1):
            
            # Compara la subcadena con la porción del texto
            if texto[i:i + longitudSubcadena] == subcadena:
                posiciones.append(i)
        return posiciones