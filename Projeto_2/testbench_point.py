from package.maths.terms import Point

def workspace():
    cord_x = int(input(f'digite um número inteiro para coordenada x do ponto '))
    cord_y = int(input(f'digite um número inteiro para coordenada y do ponto '))
    if cord_x < 0 or cord_y < 0:
        print("Os valores x ou y devem ser maiores ou iguais a 0")

    else:
        ponto1 = Point(cord_x, cord_y)
        ponto1.coordenadas()
        print(f'a distância entre esse ponto e a origem é {ponto1.distancia_origem()}')



workspace()
    





