from package.maths.terms import circle

def workspace():
    circulo_1 = circle(1, 2, 3)
    circulo_1.model()
    print(f'circunferencia: {circulo_1.circulo()}')
    print(f'area: {circulo_1.area()}')

if __name__ == '__main__':
    print('o arquivo "testebench_02.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_02.py foi envocado como modelo')
    print(f'__name__ == {__name__}')