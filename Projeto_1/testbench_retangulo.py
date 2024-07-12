from package.maths.terms import Retangulo

def workspace():
    retangulo_1 = Retangulo(4,5)
    retangulo_1.model()
    print(f'perimetro: {retangulo_1.perimetro()}')
    print(f'Área: {retangulo_1.area()}')


if __name__ == '__main__':
    print('o arquivo "testebench_retangulo.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_retangulo.py foi envocado como modelo')
    print(f'__name__ == {__name__}')
