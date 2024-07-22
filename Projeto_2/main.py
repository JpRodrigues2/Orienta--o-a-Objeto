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
        print('[4] - Verificar interferência entre as formas geométricas')
        print('[5] - Remover figura geométrica')
        print('[6] - Listar figuras geométricas')
        print('[7] - Encerrar programa')

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
            circulo = circle(raio, None)
            circulo.model
            print(f'\nA área desse círculo é: {circulo.area()}')
            print('\n[Círculo criado com sucesso!!]\n')
            formas.add_forma(circulo)

        elif resposta == 4:
            print('\n[1] - Verificar ditância entre dois pontos')
            print('[2] - Verificar interferência entre Retângulo e ponto')
            print('[3] - Verificar interferência entre Círculo e ponto')
            print('[4] - Verificar interferência entre ponto e reta')
            form_select = int(input('Digite sua escolha\n'))
            if form_select== 1:
                print('Digite as coordenadas dos pontos desejados')
                pontos = capturar_pontos()
                verificar_distancias(pontos)


            if form_select == 2:
                print('Digite a coordenada x do ponto')
                pontox = int(input())
                print('Digite a coordenada y do ponto')
                pontoy = int(input())
                print('Digite a coordenada x do retângulo')
                retx = int(input())
                print('Digite a coordenada y do retângulo')
                rety = int(input())
                print('Digite a altura do retângulo')
                altura = int(input())
                print('Digite a largura do retângulo')
                largura = int(input())
                if Contem_formas.retangulo(retx,rety,largura,altura,pontox,pontoy):
                    print('O ponto está dentro do retângulo')
                else:
                    print('O ponto não está dento do retângulo')
            
            
            if form_select == 3:
                print ('Digite a coordenada x do ponto')
                coordenadax_p = int(input())
                print('Digite a coordenada y do ponto')
                coordenaday_p = int(input())
                print('Digite a coordenada x do centro do círculo')
                coordenadax_c = int(input())
                print('Digite a coordenada y do centro do círculo')
                coordenaday_c = int(input())
                print('Digite o raio desse círculo')
                raio= int(input())
                if Contem_formas.circulo(coordenadax_p, coordenaday_p,coordenadax_c, coordenaday_c,raio):
                    print('O ponto está dentro da circunferência')
                else:
                    print('O ponto não está dentro da circunferência')

           


        #REMOVE FORMAS
        elif resposta == 5:
            formas.listar_formas()
            key = int(input('Selecione o número da forma geométrica que deseja deletar'))
            if formas.remove_formas(key):
                print(f'\nForma {key} foi deletada')

            else:
                print('\n Não foi possível encontrar a forma geométrica {key}')


        #LISTAR AS FORMAS
        elif resposta == 6:
            print('As formas geométricas criadas são: \n')
            formas.listar_formas()
            print('\n')





        elif resposta == 7:
            print('Programa encerrado')
            break
        else:
            print('Opção inválida')
            input('Pressione Enter para continuar...')



main()