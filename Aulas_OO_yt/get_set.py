class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def desconto (self,percentual):
        self.preco = self.preco - (self.preco * (percentual /100) )


    #Getter                  get apenas o metodo que esta dando ' erro', nesse caso o valor
    @property
    def preco(self):
        return self._preco   #tem o '_' para n criar um loopingm, se ja for privado ou protegido so repete
    
    #setter                  set o mesmo metodo usado no get
    @preco.setter
    def preco(self,valor):
        if isinstance(valor, str):                      #isistance valida se 'valor' é uma str
            valor = float(valor.replace('R$', ''))      #float transforma em numero, replace 'troca' oq for desejado

        self._preco = valor



    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome = valor.replace('@', 'a')



p1 = Produto('C@miseta', 50)    #formato correto ('Camiseta', 50)
p1.desconto(10)
print(p1.nome , p1.preco)

p2 = Produto ('caneca', 'R$15')   #da erro por causa da string 'R$'
p2.desconto(10)
print(p2.nome, p2.preco)