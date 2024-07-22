import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_para_origem(self):
        #Calcula a distância do ponto para a origem (0, 0).
        return math.sqrt(self.x**2 + self.y**2)

    def distancia_para_ponto(self, outro_ponto):
        #Calcula a distância entre este ponto e outro ponto.
        return math.sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


def capturar_pontos():
    
    pontos = []
    while True:
        try:
            x = float(input("Digite a coordenada x do ponto (ou 'fim' para encerrar): "))
            y = float(input("Digite a coordenada y do ponto: "))
            pontos.append(Point(x, y))
        except ValueError:
            break
    return pontos   

def verificar_distancias(pontos):
    
    
    for ponto in pontos:
        print(f"Distância do ponto {ponto} para a origem: {ponto.distancia_para_origem():.2f}")

    
    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            distancia = pontos[i].distancia_para_ponto(pontos[j])
            print(f"Distância entre o ponto {pontos[i]} e o ponto {pontos[j]}: {distancia:.2f}")           



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
    def __init__(self, r ):
        self.r = r
        
        


    def circulo(self):
        circulo = 2 * 3.14 * self.r
        return circulo
    
    def area(self):
        area = 3.14 * pow(self.r, 2)
        return area
    
    def model(self):
        print(f'Os parâmetros dessa circunferência são: raio={self.r}.')

    def identif(self):
        return 'Círculo'
    
    #def contem_ponto(self, ponto):
     #   distancia = math.sqrt((ponto.x - self.centro.x) ** 2 + (ponto.y - self.centro.y) ** 2)
      #  return distancia <= self.raio

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



class Contem_formas:

    def circulo(coordx_p, coordy_p, coordx_c, coordy_c, raio):
        contem = math.sqrt((coordx_p - coordx_c)**2 + (coordy_p - coordy_c)**2)
        return contem <= raio
    
    def retangulo(inferior_esq_x, inferior_esq_y, largura,altura,pontox,pontoy):
        dentro_x = (inferior_esq_x <= pontox <= inferior_esq_x + largura)
        dentro_y = (inferior_esq_y <= pontoy <= inferior_esq_y + altura)
        return dentro_x and dentro_y