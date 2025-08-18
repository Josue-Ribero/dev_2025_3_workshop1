class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        posicion = 0
        actual = 0
        siguiente = 1
        while posicion < n:
            temporal = actual + siguiente
            actual = siguiente
            siguiente = temporal
            posicion += 1
        return actual
    
    def secuencia_fibonacci(self, n):
        posicion = 0
        actual = 0
        siguiente = 1
        secuencia = []
        while posicion < n:
            secuencia.append(actual)
            temporal = actual + siguiente
            actual = siguiente
            siguiente = temporal
            posicion += 1
        return secuencia
        
    
    def es_primo(self, n: int):
        # Si es menor que 2, no es primo
        if n < 2:
            return False
        
        # Verifica si es divisible por algún número desde 2 hasta la raíz cuadrada de n
        for i in range(2, int(n**0.5) + 1):
            # Si es divisible, no es primo
            if n % i == 0:
                return False
        return True
    
    
    def generar_primos(self, n):
        primos = []
        for num in range(2, n):
            if self.es_primo(num):
                primos.append(num)
        return primos
        
    
    def es_numero_perfecto(self, n):
        # Ni los numeros perfectos ni 0 o 1 son numeros perfectos
        if n < 2:
            return False
        
        # Contador del valor de la suma de divisores
        sumaDivisores = 0

        # Recorrido de 1 hasta n - 1
        for i in range(1, n):
            # Verifica si i es divisor de n
            if n % i == 0:
                # Se suma el valor del divisor al contador
                sumaDivisores += i
        
        # Se retorna un valor booleano de si n es igual a la suma de sus divisores
        return sumaDivisores == n
        
    
    def triangulo_pascal(self, filas):
        # Lista que contendra el triangulo
        triangulo = []

        # Itera la cantidad de filas necesarias
        for i in range(filas):
            fila = [1] # Siempre empieza con 1

            if i > 0:
                # Obtiene la fila anterior para calcular las sumas
                filaAnterior = triangulo[i - 1]

                # Calcula los valores internos
                for j in range(1, i):
                    fila.append(filaAnterior[j - 1] + filaAnterior[j])
                
                # Cada fila termina con 1
                fila.append(1)
            
            # Agrega a la fila generada el triangulo completo
            triangulo.append(fila)
        
        return triangulo
    
    
    def factorial(self, n):
        # Retorna el factorial de 0
        if n == 0:
            return 1

        contador = 1
        for i in range(1, n + 1):
            # Multiplica el valor inicial del contador con los valores de 1 hasta n
            contador *= i
        return contador
    
    
    def mcd(self, a, b):
        # Toma el mayor de los dos para iterar
        for i in range(1, max(a, b) + 1):
            # Si el divisor en ambos casos da un resultado entero lo toma
            if a % i == 0 and b % i == 0:
                # Toma el mayor valor que cumpla la condicion
                mcd = i
        return mcd
    
    
    def mcm(self, a, b):
        # Caso donde alguno de los dos sea 0
        if a == 0 or b == 0:
            return 0
        
        # Se multiplican, se halla su maximo comun divisor y se hace una division entera entre el
        return (a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n: int):
        cadena = str(n)
        digitos = []
        for digito in cadena:
            digitos.append(int(digito))
        return sum(digitos)
        
    
    def es_numero_armstrong(self, n):
        cadena = str(n)
        numDigitos = len(cadena)
        digitos = []
        for digito in cadena:
            digito = int(digito) ** numDigitos
            digitos.append(digito)
        
        return sum(digitos) == n
    
    
    def es_cuadrado_magico(self, matriz: list):
        # Es la cantidad de elementos que tiene la matriz
        longitud = len(matriz)

        # Determina que la matriz sea cuadrada
        for fila in matriz:
            if len(fila) != longitud:
                return False
        
        # Suma los valores de la primera fila
        sumaObjetivo = sum(matriz[0])

        # Verifica que todas las filas den la misma suma
        for fila in matriz:
            if sum(fila) != sumaObjetivo:
                return False
        
        for i in range(longitud):
            sumaColumnas = 0
            for j in range(longitud):
                sumaColumnas += matriz[j][i]
            if sumaColumnas != sumaObjetivo:
                return False
        
        sumaDiagonal1 = 0
        for i in range(longitud):
            sumaDiagonal1 += matriz[i][i]
        if sumaDiagonal1 != sumaObjetivo:
            return False
        
        sumaDiagonal2 = 0
        for i in range(longitud):
            sumaDiagonal2 += matriz[i][longitud - 1 - i]
        if sumaDiagonal2 != sumaObjetivo:
            return False
        
        return True