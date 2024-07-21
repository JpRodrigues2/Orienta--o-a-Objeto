class Reta():


    def __init__(self,a,b):  #construtor 

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')


class circle():
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y


    def circulo(self):
        circulo = 2 * 3.14 * self.r
        return circulo
    
    def area(self):
        area = 3.14 * pow(self.r, 2)
        return area
    
    def model(self):
        print(f'Os parâmetros dessa circunferência são: raio={self.r}, x={self.x}, y={self.y}.')

    def identif(self):
        return 'Círculo'

class Triangulo():
    def __init__(self,base,altura):
        self._base = base
        self._altura = altura
    
    def area(self):
        area= (self._base * self._altura) / 2
        return area    
    
    def model(self):
        print(f'Os parâmetros desse triângulo são: base={self._base}, altura={self._altura}')

    def identif(self):
        return 'Triângulo'

class Point():
    pass





class Retangulo():
    def __init__(self , lado, base):
        self.__lado = lado
        self.__base = base
    
    def perimetro(self):
        perimetro = 2*self.__lado + 2*self.__base
        return perimetro
    
    def area(self):
        area = self.__lado*self.__base
        return area
    
    def model(self):
        print(f'Os parâmetros desse retangulo são: lado={self.__lado}, base={self.__base}')

    def identif(self):
        return 'Retângulo'

class Quadrado(Retangulo):
    def __init__(self,lado,base):
        super().__init__(lado,base)


class Hexagono():
    def __init__(self,lados,cor):
        self.__lados = lados
        self.__cor = cor

    def color(self):
        color = self.__cor
        return color
    
    def area(self):
        import math
        area = (3*self.__lados*math.sqrt(3))/2
        return area

    def model(self):
        print(f'Os parâmetros desse Hexágono são: lados={self.__lados}')

class Octogono:
    def __init__(self,lados,cor):
        self.lados= lados
        self.cor = cor
        

    def model(self):
        print(f'Os parâmetros desse Octógono são: lados={self.lados} e cor {self.cor}')

class Decagono():
    def __init__(self,tamanho_lados,octagono):
        self.tamanho_lados = tamanho_lados
        self.octagono = octagono

    def model(self):
        print(f'Os parâmetros desse Decágono são: lados={self.tamanho_lados} e cor {self.octagono.cor}')


class Poligonos:
    def __init__ (self, nome , cor):
        self.nome = nome
        self.cor = cor
        self.lados = []

    def quantos_lados(self,arestas):
        self.lados.append(Lados(arestas))

    def lista_quantos_lados(self):
        for lados in self.lados:
            print(f'Esse polígono possui {lados.arestas} lados') 

class Lados:
    def __init__(self,arestas):
        self.arestas = arestas


class Listar_formas:
    def __init__(self):
        self.formas = {}
        self.count = 0

    def add_forma(self, new_form):
        self.count += 1
        self.formas[self.count] = new_form

    def remove_formas(self,key):
        if key in self.formas:
            del self.formas[key]
            return True
        else:
            return False

    def listar_formas(self):
        if not self.formas:
            print('Não existe nenhuma forma geométrica criada')
        else:
            for chave, formas in self.formas.items():
                print(f"{chave}: {formas.identif()}")


    


    



    
    

        















    
        