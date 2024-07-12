from package.maths.terms import Octogono , Decagono

def workspace():
    tm_lados_oc = int(input('Digite o tamanho dos lados do Octógono: '))
    color_oc = str(input('Digite a cor desejada das duas figuras: '))
    tm_lados_dec = int(input('Digite o tamanho dos lados do Decágono: '))
    octogono = Octogono(tm_lados_oc,color_oc)
    decagono= Decagono(tm_lados_dec,octogono)
    octogono.model()
    decagono.model()
    print(f'Logo, podemos concluir que a cor das duas figuras é {decagono.octagono.cor}, o tamanho dos lados do Octágono é {octogono.lados} e por fim o tamanho dos lados do Decágono é {decagono.tamanho_lados} ')
    
    


if __name__ == '__main__':
    print('o arquivo "testebench_octogono_decagono.py" foi envocado como programa')
    print(f'__name__ =={__name__}')
    workspace()

else:
    print('o arquivo "testbench_octogono_decagono.py foi envocado como modelo')
    print(f'__name__ == {__name__}')


