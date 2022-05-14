from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contador de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        print('Fim')
        print('-=' * 20)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print('Fim')
        print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('INICIO: '))
fin = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fin, pas)