class Stats:
    def promedio(self, numeros):
        # Verifica si la lista no está vacía
        if numeros:
            return sum(numeros) / len(numeros)
        return 0
        
    
    def mediana(self, numeros):
        # Verifica si la lista no está vacía
        if numeros:
            numeros.sort() # Ordena la lista de forma ascendente
            longitud = len(numeros)
            mid = longitud // 2 # Encuentra el valor exacto del medio

            # Si la longitud es par, retorna el promedio de los dos valores centrales
            if longitud % 2 == 0:
                return (numeros[mid - 1] + numeros[mid]) / 2
            else:
                # Si es impar, retorna el valor central
                return numeros[mid]
        return 0
        
    
    def moda(self, numeros):
        # Verifica si la lista no está vacía
        if numeros:
            cantidad = {} # Diccionario para contar cantidad de veces
            for num in numeros:
                if num in cantidad:
                    cantidad[num] += 1 # Incrementa el contador de apariciones
                else:
                    cantidad[num] = 1 # Inicializa contador

            # Encuentra el número con la máxima frecuencia
            maximaFrecuencia = max(cantidad.values())
            for num in numeros:
                if cantidad[num] == maximaFrecuencia:
                    return num
        return None
        
    
    def desviacion_estandar(self, numeros):
        desviacion = 0 # Inicializa la desviación estándar

        # Verifica si la lista no está vacía
        if numeros:
            promedio = self.promedio(numeros) # Calcula el promedio
            for x in numeros:
                # Calcula la suma de las diferencias al cuadrado
                desviacion += (x - promedio) ** 2

            # Divide por el número de elementos y saca la raíz cuadrada
            desviacion = (desviacion / len(numeros)) ** 0.5
        return desviacion
        
    
    def varianza(self, numeros):
        varianza = 0 # Inicializa la varianza
        
        # Verifica si la lista no está vacía
        if numeros:
            promedio = self.promedio(numeros)
            for x in numeros:
                # Calcula la suma de las diferencias al cuadrado
                varianza += (x - promedio) ** 2

            # Divide por el número de elementos
            varianza /= len(numeros)
        return varianza
    
    
    def rango(self, numeros):
        rango = 0 # Inicializa el rango

        # Verifica si la lista no está vacía
        if numeros:
            # Calcula el rango como la diferencia entre el máximo y mínimo
            rango = max(numeros) - min(numeros)
        return rango