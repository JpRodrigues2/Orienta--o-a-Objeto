class Professor:
    def __init__(self, nome):
        self.nome = nome


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []


    def adicionar_prof(self, professor):
        self.professores.append(professor)


    def mostrar_professores(self):
        for prof in self.professores:
            print(prof.nome)


class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.deptos = []


    def adicionar_depto(self, depto):
        novo_depto = Departamento(depto)
        self.deptos.append(novo_depto)


uni = Universidade("UnB")
uni.adicionar_depto("FGA")
uni.adicionar_depto("CIC")

prof1 = Professor("Glauco")
prof2 = Professor("Maria")

#uni.deptos[0].adicionar_prof(prof1)
#uni.deptos[1].adicionar_prof(prof2)

#print(uni.nome)
#for dp in uni.deptos:
#    print("Os profs do Depto "+ dp.nome + "são: ")
#    dp.mostrar_professores()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print( endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado



cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')


cliente2 = Cliente('Maria',55)
cliente2.insere_endereco('Salvador','BA')
cliente2.insere_endereco('Rio de Janeiro','RJ')

cliente3 = Cliente('Joao', 19)
cliente3.insere_endereco('São Paulo','SP')







