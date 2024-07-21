from package.maths.terms import *

def main():
    formas = Listar_formas()



    while True:
    
        print('-' * 20)
        print('Menu de interação')
        print('-' * 20)
        print('Estão disponíveis para serem geradas as formas geométricas abaixo: ')
        print()
        print('Selecione: ')
        print()
        print('[1] - Retângulo ')
        print('[2] - Triângulo ')
        print('[3] - Círculo')
        print('[4] - Remover figura geométrica')
        print('[5] - Listar figura geométrica')
        print('[6] - Encerrar programa')

        resposta = int(input("Digite a sua escolha: "))   
        if resposta == 1:
            lado = int(input('Digite o tamannho do lado do retângulo: '))
            base = int(input('Digite o tamannho da base do retângulo: '))
            retangulo = Retangulo(lado, base)
            retangulo.model()
            print(f'\nA área desse retângulo é: {retangulo.area()}')
            print('\n[Retângulo criado com sucesso!!]\n')
            formas.add_forma(retangulo)
            

        elif resposta == 2:
            base = int(input('Digite o tamannho da base do triângulo: '))
            altura = int(input('Digite o tamannho da altura desse triângulo: '))
            triangulo = Triangulo(base,altura)
            triangulo.model()
            print(f'\nA área desse triângulo é: {triangulo.area()}')
            print('\n[Triângulo criado com sucesso!!]\n')
            formas.add_forma(triangulo)
            

        elif resposta == 3:
            raio = int(input('Digite o raio desse círculo: '))
            x = int(input('Digite a coordenada x desse círculo: '))
            y = int(input('Digite a coordenada y desse círculo: '))
            circulo = circle(raio,x,y)
            circulo.model
            print(f'\nA área desse círculo é: {circulo.area()}')
            print('\n[Círculo criado com sucesso!!]\n')
            formas.add_forma(circulo)
            

        elif resposta == 4:
            formas.listar_formas()
            key = int(input('Selecione o número da forma geométrica que deseja deletar'))
            if formas.remove_formas(key):
                print(f'\nForma {key} foi deletada')

            else:
                print('\n Não foi possível encontrar a forma geométrica {key}')

        elif resposta == 5:
            print('As formas geométricas criadas são: \n')
            formas.listar_formas()
            print('\n')





        elif resposta == 6:
            print('Programa encerrado')
            break
        else:
            print('Opção inválida')
            input('Pressione Enter para continuar...')



main()