class Escritor:                    #setter
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None


    @property        #getter
    def nome(self):
        return self.__nome
    
    @property                 #getter
    def ferramenta(self):
        return self.__ferramenta 
    
    @ferramenta.setter                #setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta
    

class Caneta:
    def __init__(self,marca):       #setter
        self.__marca = marca

    @property                       #getter
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta esta escrevendo...')
    


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo')




escritor = Escritor('joao')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()


#escritor.ferramenta = caneta
#escritor.ferramenta = maquina

#escritor.ferramenta.escrever()

#---------------------------------------------------------------------------------------------------------------------------------------------

from typing import Type

class Interruptor:
    def __init__(self,comodo):
        self.__comodo = comodo

    def acender(self):
        print('acendendo {}'.format(self.__comodo))

    def apagar(self):
        print('apagando {}'.format(self.__comodo))


class Pessoa:
    def acender_luz(self,interruptor : Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self,interruptor : Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


#joao = Pessoa()
#interruptor_quarto = Interruptor('quarto')
#interruptor_quarto.acender()

#-------------------------------------------------------------------------------------------


class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


endereco = Endereco("Rua A", 123, "Cidade X")
pessoa = Pessoa("João", endereco)

print(pessoa.nome)
print(pessoa.endereco.numero)