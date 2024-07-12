from package.maths.terms import Quadrado

def workspace():
    quadrado_1 = Quadrado(3,2)
    quadrado_1.model()
    print(f'perimetro: {quadrado_1.perimetro()}')
    print(f'area: {quadrado_1.area()}')

if __name__ == '__main__':
    print('o arquivo "testebench_quadrado.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_quadrado.py foi envocado como modelo')
    print(f'__name__ == {__name__}')

