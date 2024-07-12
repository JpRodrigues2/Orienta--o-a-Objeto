from package.maths.terms import Hexagono

def workspace():
    color = str(input('Digite a cor desejada: '))
    tm_lados = int(input('Digite o tamanho dos lados: '))
    hexagono_1 = Hexagono(tm_lados,color)
    hexagono_1.model()
    print(f'O hexágono é {hexagono_1.color()}')
    print(f'Área: {hexagono_1.area()}')
    


if __name__ == '__main__':
    print('o arquivo "testebench_hexagono.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_hexagono.py foi envocado como modelo')
    print(f'__name__ == {__name__}')