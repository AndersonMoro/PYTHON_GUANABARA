from math import sqrt
from time import sleep

cores = {'vermelho':'\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul' : '\033[1;34m',
         'roxo': '\033[1;35m',
         'limpa': '\033[m'}
escolha1 = 0
n2 = 0
while True:
    print(f'''{cores['amarelo']}ESCOLHA O QUE FAZER:
[ 1 ] DOBRO, TRIPLO OU RAIZ
[ 2 ] CONVERSOR DE MEDIDAS
[ 3 ] TABUADA
[ 4 ] CONVERSOR DE MOEDAS
[ 5 ] PINTURA PAREDE
[ 10 ] PARA SAIR {cores['limpa']}''')
    print('=+'*30)
    sleep(1)
    escolha1 = int(input('\033[1;34mQUAL SUA ESCOLHA: '))
    if escolha1 == 1:
        while True:
            print('''\033[1;31mESCOLHA UMA OPÇÃO:
[ 1 ] DOBRO
[ 2 ] TRIPLO
[ 3 ] RAIZ QUADRADA
[ 4 ] DIGITE [4] PARA SAIR\033[m''')
            print('=+' * 30)
            sleep(1)
            escolha01 = int(input('QUAL SUA ESCOLHA: ' ))
            if escolha01 == 1:
                n1 = int(input('DIGITE UM NÚMERO: '))
                print(f'\033[1;35mO DOBRO DE {n1} é {n1*2}\033[m.')
            if escolha01 == 2:
                print(f'\033[1;35mO TRIPLO DE {n1} É {n1*3}\033[m.')
            if escolha01 == 3:
                print(f'\033[1;35mA RAIZ 4DE {n1} É {sqrt(n1):.2f}\033[m.')
            if escolha01 == 4:
                break
        sleep(1)
        print('*-' * 30)
    if escolha1 == 2:
        print('\033[1;32mCONVERSOR DE MEDIDAS DE METROS PARA KM; CENTIMETROS PARA METROS.\033[m')
        metros = float(input('Digite um número em Metros: '))
        cent = float(input('Digite um número em Centímetros: '))
        print(f'Você digitou \033[1;31m{metros}m\033[m. Agora esse valor fica \033[1;31m{metros/1000}km\033[m.')
        print(f'Você digitou \033[1;31m{cent}cm\033[m. Agora esse valor fica \033[1;31m{cent/100}m\033[m.')
        print('=+' * 30)
        sleep(4)
    if escolha1 == 3:
        n2 = int(input('\033[1;35mDIGITE UM NÚMERO PARA SABER SUA TABUADA OU [0] PARA SAIR\033[m: '))
        while n2 != 0:
            for tabuada in range (1,11):
                print(f'{n2} x {tabuada} = \033[1;34m{n2*tabuada}\033[m')
            n2 = int(input('DIGITE UM NÚMERO PARA SABER SUA TABUADA OU [0] PARA SAIR: '))
        sleep(2)
    if escolha1 == 4:
        print('\033[1;32mCONVERSOR DE MOEDAS (REAIS => DÓLAR)\033[m.')
        reais = float(input('Digite um valor em Reais: R$ '))
        print(f'Você digitou \033[1;34mR$ {reais:.2f}\033[m. Agora esse valor fica \033[1;34mU$ {reais/5.65:.2f}\033[m.')
        print('=+' * 30)
        sleep(4)
    if escolha1 == 5:
        altura = float(input('Qual tamanho da parede em m2: '))
        largura = float(input('Qual tamanho da parede em m2: '))
        parede = altura*largura
        tinta = parede/2
        print(f'A área da parede é \033[1;35m{parede}m2\033[m. Para essa área você vai precisar de \033[1;35m{tinta}\033[m '
              f'litros de tinta. ')
    if escolha1 == 10:
        break


