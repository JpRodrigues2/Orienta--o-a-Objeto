from package.maths.terms import *

def main():
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
        print('[4] - Encerrar programa')

        resposta = int(input("Digite a sua escolha: "))   
        if resposta == 1:
            lado = int(input('Digite o tamannho do lado do retângulo: '))
            base = int(input('Digite o tamannho da base do retângulo: '))
            retangulo = Retangulo(lado, base)
            retangulo.model()
            print(retangulo.area())
            break
        elif resposta == 2:
            print('op2')
            break
        elif resposta == 3:
            print('op3')
            break
        elif resposta == 4:
            print('Programa encerrado')
            break
        else:
            print('Opção inválida')
            input('Pressione Enter para continuar...')



main()