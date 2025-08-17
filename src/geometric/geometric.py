class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base: float, altura: float):
        areaRectangulo = float(base * altura)

        if areaRectangulo  == int(areaRectangulo):
            return int(areaRectangulo)
        return round(areaRectangulo, 1)
    

    def perimetro_rectangulo(self, base, altura):
        perimetroRectangulo = 2 * (base + altura)

        if perimetroRectangulo == int(perimetroRectangulo):
            return int(perimetroRectangulo)
        return perimetroRectangulo
    
    
    def area_circulo(self, radio):
        areaCirculo = 3.141592 * (radio ** 2)
        return round(areaCirculo, 2)
    
    
    def perimetro_circulo(self, radio):
        perimetroCirculo = 2 * 3.141592 * radio
        return round(perimetroCirculo, 2)
    
    
    def area_triangulo(self, base, altura):
        areaTriangulo = (base * altura) / 2

        if areaTriangulo.is_integer():
            return int(areaTriangulo)
        return areaTriangulo
    
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        perimetroTriangulo = lado1 + lado2 + lado3

        if perimetroTriangulo.is_integer():
            return int(perimetroTriangulo)
        return perimetroTriangulo
        
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            return True
        else:
            return False
        
    
    def area_trapecio(self, base_mayor, base_menor, altura):
        areaTrapecio = ((base_mayor + base_menor) * altura) / 2

        if areaTrapecio == int(areaTrapecio):
            return int(areaTrapecio)
        return areaTrapecio
    
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        areaRombo = (diagonal_mayor * diagonal_menor) / 2

        if areaRombo == int(areaRombo):
            return int(areaRombo)
        return areaRombo
    
    
    def area_pentagono_regular(self, lado, apotema):
        areaPentagono = (5 * lado * apotema) / 2

        if areaPentagono == int(areaPentagono):
            return int(areaPentagono)
        return areaPentagono
        
    
    def perimetro_pentagono_regular(self, lado):
        perimetroPentagono = 5 * lado

        if perimetroPentagono == int(perimetroPentagono):
            return int(perimetroPentagono)
        return perimetroPentagono
    
    
    def area_hexagono_regular(self, lado, apotema):
        areaHexagono = (6 * lado * apotema) / 2

        if areaHexagono == int(areaHexagono):
            return int(areaHexagono)
        return areaHexagono
        
    
    def perimetro_hexagono_regular(self, lado):
        perimetroHexagono = 6 * lado

        if perimetroHexagono == int(perimetroHexagono):
            return int(perimetroHexagono)   
        return perimetroHexagono
        
    
    def volumen_cubo(self, lado):
        volumenCubo = lado ** 3

        if volumenCubo == int(volumenCubo):
            return int(volumenCubo)
        return volumenCubo
        
    
    def area_superficie_cubo(self, lado):
        areaSuperficialCubo = 6 * (lado ** 2)

        if areaSuperficialCubo == int(areaSuperficialCubo):
            return int(areaSuperficialCubo)
        return areaSuperficialCubo
        
    
    def volumen_esfera(self, radio):
        volumenEsfera = (4/3) * 3.141592 * (radio ** 3)

        if volumenEsfera == int(volumenEsfera):
            return int(volumenEsfera)
        return round(volumenEsfera, 2)
        
    
    def area_superficie_esfera(self, radio):
        areaSuperficialEsfera = 4 * 3.141592 * (radio ** 2)

        if areaSuperficialEsfera == int(areaSuperficialEsfera):
            return int(areaSuperficialEsfera)
        return round(areaSuperficialEsfera, 2)
        
    
    def volumen_cilindro(self, radio, altura):
        volumenCilindro = 3.141592 * (radio ** 2) * altura

        if volumenCilindro == int(volumenCilindro):
            return int(volumenCilindro)
        return round(volumenCilindro, 2)
        
    
    def area_superficie_cilindro(self, radio, altura):
        areaSuperficialCilindro = 2 * 3.141592 * radio * (radio + altura)

        if areaSuperficialCilindro == int(areaSuperficialCilindro):
            return int(areaSuperficialCilindro)
        return round(areaSuperficialCilindro, 2)
        
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return round(distancia, 2)
        
    
    def punto_medio(self, x1, y1, x2, y2):
        puntoMedioX = (x1 + x2) / 2
        puntoMedioY = (y1 + y2) / 2
        return (round(puntoMedioX, 2), round(puntoMedioY, 2))
    
    
    def pendiente_recta(self, x1, y1, x2, y2):
        pendiente = (y2 - y1) / (x2 - x1)
        return round(pendiente, 2)
    
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        a = y2 - y1
        b = x1 - x2
        c = (x2 * y1) - (x1 * y2)

        tupla = (a, b, c)
        return tupla
    
    
    def area_poligono_regular(self, num_lados: int, lado: float, apotema: float):
        if num_lados == 4:
            areaPoligono = num_lados * lado * apotema
        else:
            areaPoligono = (num_lados * lado * apotema) / 2
        
        if areaPoligono == int(areaPoligono):
            return int(areaPoligono)
        return areaPoligono
    
    
    def perimetro_poligono_regular(self, num_lados, lado):
        perimetroPoligono = num_lados * lado
        if perimetroPoligono == int(perimetroPoligono):
            return int(perimetroPoligono)
        return perimetroPoligono