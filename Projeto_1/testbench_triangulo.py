from package.maths.terms import Triangulo


def workspace():
    triangulo_1 = Triangulo(5,10)
    triangulo_1.model()
    print(f'area: {triangulo_1.area()}')

if __name__ == '__main__':
    print('o arquivo "testebench_triangulo.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_triangulo.py foi envocado como modelo')
    print(f'__name__ == {__name__}')

    
    
