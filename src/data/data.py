class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        invertida = []
        for item in lista:
            invertida.insert(0, item) # Agrega cada nuevo valor antes del anterior
        return invertida
    

    def buscar_elemento(self, lista: list, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    

    def eliminar_duplicados(self, lista: list):
        listaSinDobles = []
        vistos = []

        for elemento in lista:
            if (elemento, type(elemento)) not in vistos:
                vistos.append((elemento, type(elemento)))
                listaSinDobles.append(elemento)
        return listaSinDobles
    

    def merge_ordenado(self, lista1, lista2):
        listaUnion = sorted(lista1 + lista2)
        return listaUnion
    

    def rotar_lista(self, lista: list, k):
        if not lista:
            return []
        
        listaRodada = lista[:]
        for _ in range(k):
            ultimo = listaRodada.pop() # Saca el ultimo elemento de la lista y lo almacena
            listaRodada.insert(0, ultimo) # Inserta el elemento "ultimo" en la primera posicion
        return listaRodada
    

    def encuentra_numero_faltante(self, lista):
        elementosEsperados = len(lista) + 1 # Falta un elemento, por eso se coloca un + 1
        sumaEsperada = elementosEsperados * (elementosEsperados + 1) // 2
        sumaLista = sum(lista)
        return sumaEsperada - sumaLista
    

    def es_subconjunto(self, conjunto1: list, conjunto2: list):
        return all(elemento in conjunto2 for elemento in conjunto1)
    

    def implementar_pila(self):
        pila = []

        def isEmpty():
            return len(pila) == 0
        
        def push(elemento):
            pila.append(elemento)
        
        def peek():
            if not isEmpty():
                return pila[-1]
            
        def pop():
            return pila.pop()
            
        dictPila = {
            "is_empty":isEmpty,
            "push":push,
            "peek":peek,
            "pop":pop
        }
        return dictPila
    

    def implementar_cola(self):
        cola = []

        def isEmpty():
            return len(cola) == 0
        
        def enqueue(elemento):
            cola.append(elemento)
            
        def dequeue():
            return cola.pop(0)
        
        def peek():
            if not isEmpty():
                return cola[0]
        
        dictCola = {
            "is_empty":isEmpty,
            "enqueue":enqueue,
            "dequeue":dequeue,
            "peek":peek
        }
        return dictCola
    

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        
        filas = len(matriz) # Cantidad de filas
        columnas = len(matriz[0]) # Cantidad de columnas por fila

        matrizTranspuesta = []
        for j in range(columnas): # Recorrido de las columnas originales
            nuevaFila = []
            for i in range(filas): # Recorrido de las filas originales
                nuevaFila.append(matriz[i][j]) # Se agregan los valores de las columnas x:y con indice igual
            matrizTranspuesta.append(nuevaFila) # Se agrega la matriz final a la transpuesta
        return matrizTranspuesta