class Professor:
    def __init__(self, nome):
        self.nome = nome


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_prof(self, professor):
        self.professores.append(professor)


depart = Departamento("FGA")
prof1 = Professor("João")
prof2 = Professor("Maria")


depart.adicionar_prof(prof1)
depart.adicionar_prof(prof2)


#print(depart.nome)
#for prof in depart.professores:
#    print(prof.nome)

#-----------------------------------------------------------------------------------------------------------------------------------------


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self,produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self,nome,valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone',10000)
p3 = Produto('Caneca',15)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)



carrinho.lista_produto()
print(carrinho.soma_total())