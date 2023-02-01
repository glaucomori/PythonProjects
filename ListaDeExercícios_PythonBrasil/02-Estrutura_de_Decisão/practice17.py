# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

try:
    # Pedir o ano para o usuário e atribuir a uma variável
    year = input('Informe o ano: ')
    # alterar o tipo da variável para o tipo inteiro
    year = int(year)
    # declarar uma variável 'bissexto' para receber o resultado das estruturas de decisão
    leapYear = None
    # verificar se o ano é múltiplo de 100
    if (year%100) == 0 :
    # se for múltiplo de 100 deve-se verificar se é divisível por 400
        if (year%400) == 0:
    # se for divisível por 400 o ano é bissexto, então atribuir o valor 'True' para a variável 'bissexto'
            leapYear = True
    # se for indivisível por 400 o ano não é bissexto, então atribuir o valor 'False" para a variável 'bissexto'
        else:
            leapYear = False
    # se não for múltiplo de 100 deve-se verificar se é divisível por 4
    else:
        if (year%4) == 0:
    # se for divisível por 4 o ano é bissexto, então atribuir o valor 'True' para a variável 'bissexto'
            leapYear = True
    # se for indivisível por 4 a ano não é bissexto, então atribuir o valor 'False" para a variável 'bissexto'
        else:
            leapYear = False
    # imprimir na tela o resultado da decisão
    if leapYear == True:
        print('O ano informado é bissexto.')
    else:
        print('O ano informado não é bissexto.')
except:
    print('Erro!')