from time import sleep

contas = True


def adicao():
    
    print('\033[37m')
    
    num = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))

    Csoma = num + num2

    answer = str(input(
        'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

    if answer in 'N':

        Question = str(input(
            'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if Question in 'N':

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {Csoma:.3}')

        else:

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {int(Csoma)}')

    elif answer in 'S':

        maisUm = True

        while maisUm == True:

            num3 = float(input('Digite mais um número: '))

            Csoma = Csoma + num3

            Totconta = Csoma

            answer = str(input(
                'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

            if answer in 'S':

                maisUm == True

            if answer in 'N':

                maisUm = False

                Question = str(input(
                    'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

                if Question in 'N':

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {Totconta:.4}')

                else:

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {int(Totconta)}')


def subtracao():

    print('\033[37m')

    num1 = float(input('Digite um numero: '))

    num2 = float(input('Digite outro numero: '))

    Csub = num1 - num2

    answer = str(input(
        'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

    if answer in 'N':

        Question = str(input(
            'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if Question in 'N':

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {Csub:.3}')

        else:

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {int(Csub)}')

    elif answer in 'S':

        maisUm = True

        while maisUm == True:

            num3 = float(input('Digite mais um número: '))

            Csub = Csub - num3

            Totconta = Csub

            answer = str(input(
                'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

            if answer in 'S':

                maisUm == True

            if answer in 'N':

                maisUm = False

                Question = str(input(
                    'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

                if Question in 'N':

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {Totconta:.4}')

                else:

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {int(Totconta)}')


def divisao():

    print('\033[37m')

    num1 = float(input('Digite um numero: '))

    num2 = float(input('Digite outro numero: '))

    Cdiv = num1 / num2

    answer = str(input(
        'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

    if answer in 'N':

        Question = str(input(
            'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if Question in 'N':

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {Cdiv:.3}')

        else:

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {int(Cdiv)}')

    elif answer in 'S':

        maisUm = True

        while maisUm == True:

            num3 = float(input('Digite mais um número: '))

            Cdiv = Cdiv / num3

            Totconta = Cdiv

            answer = str(input(
                'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

            if answer in 'S':

                maisUm == True

            if answer in 'N':

                maisUm = False

                Question = str(input(
                    'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

                if Question in 'N':

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {Totconta:.4}')

                else:

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {int(Totconta)}')


def multiplicacao():

    print('\033[37m')

    num1 = float(input('Digite um numero: '))

    num2 = float(input('Digite outro numero: '))

    Cmult = num1 * num2

    answer = str(input(
        'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

    if answer in 'N':

        Question = str(input(
            'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if Question in 'N':

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {Cmult:.3}')

        else:

            print('\033[34m=-' * 22)
            print(f'A soma dos valores digitados é igual a {int(Cmult)}')

    elif answer in 'S':

        maisUm = True

        while maisUm == True:

            num3 = float(input('Digite mais um número: '))

            Cmult = Cmult * num3

            Totconta = Cmult

            answer = str(input(
                'Quer digitar mais um número? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

            if answer in 'S':

                maisUm == True

            if answer in 'N':

                maisUm = False

                Question = str(input(
                    'Quer mostrar esse valor em numero inteiro? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

                if Question in 'N':

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {Totconta:.4}')

                else:

                    print('\033[34m=-' * 22)
                    print(
                        f'A soma dos valores digitados é igual a {int(Totconta)}')


while contas == True: 
    
    print('=-' * 22)

    print('\033[37mBem vindo a calculadora feita em Python!')
    print('Escolha o numero da operação desejada na tabela e comece suas contas!')

    print('''

    [1] Adição
    [2] Subtração
    [3] Divisão
    [4] Multiplicação

        ''')

    answer = int(
        input('Digite o numero da operação desejada. (digite 0 para sair) :>>  '))

    if answer not in range(0, 5):
        
        while answer not in range(0, 5):

            answer = int(
            input('\033[31mDesculpe, não entendi, digite o numero da operação desejada. (digite 0 para sair) :>>  '))

    if answer == 1:

        adicao()

        pergunta = str(input(
            'Você quer fazer outra operação? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if pergunta in 'S':

            contas = True

        else:

            contas = False

            print('OK!')
            sleep(1)
            print('Saindo do programa...')
            sleep(1)

            answer = 0

            while answer == 0:

                break

    elif answer == 2:

        subtracao()

        pergunta = str(input(
            'Você quer fazer outra operação? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if pergunta in 'S':

            contas = True

        else:

            contas = False

            print('OK!')
            sleep(1)
            print('Saindo do programa...')
            sleep(1)

            answer = 0

            while answer == 0:

                break

    elif answer == 3:

        divisao()

        pergunta = str(input('Você quer fazer outra operação? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if pergunta in 'S':

            contas = True

        else:

            contas = False

            print('OK!')
            sleep(1)
            print('Saindo do programa...')
            sleep(1)

            answer = 0

            while answer == 0:

                break

    elif answer == 4:

        multiplicacao()

        pergunta = str(input('Você quer fazer outra operação? [Sim/Não]: ')).strip().rstrip().lstrip().upper()[0]

        if pergunta in 'S':

            contas = True

        else:

            contas = False

            print('OK!')
            sleep(1)
            print('Saindo do programa...')
            sleep(1)

            answer = 0

            while answer == 0:

                break

    elif answer == 0:

        contas = False

        print('OK!')
        sleep(1)
        print('Saindo do programa...')
        sleep(1)
