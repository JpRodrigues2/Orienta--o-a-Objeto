from package.maths.terms import Poligonos, Lados

def workspace():
    poli1 = str(input('Digite o nome do polígono 1: '))
    color1 = str(input('Digite a cor desejada: '))
    num_lados1 = int(input('Digite a quantidade de lados do polígono 1: '))
    poligono1= Poligonos(poli1,color1)
    poligono1.quantos_lados(num_lados1)

    poli2 = str(input('Digite o nome do polígono 2: '))
    color2 = str(input('Digite a cor desejada: '))
    num_lados2 = int(input('Digite a quantidade de lados do polígono 2: '))
    poligono2 = Poligonos(poli2,color2)
    poligono2.quantos_lados(num_lados2)

    print(f'você gerou o {poligono1.nome}')
    print(f'você gerou o {poligono2.nome}')
    poligono1.lista_quantos_lados()
    poligono2.lista_quantos_lados()
    print('Respectivamente')





if __name__ == '__main__':
    print('o arquivo "testebench_poligonos_lados.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testebench_poligonos_lados.py foi envocado como modelo')
    print(f'__name__ == {__name__}')