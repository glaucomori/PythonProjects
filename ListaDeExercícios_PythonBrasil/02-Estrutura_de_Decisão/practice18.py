# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

try:
    # pedir a data e atribuir a uma variável (especificando o formato desejado)
    fullDate = input('Informe a data no formado dd/mm/aaaa: ')
    # dividir a variável com base no separador usado no formato desejado
    fullDate = fullDate.split('/')
    # atribuir cada fragmento da variável a uma variavel diferente: dia, mês e ano
    day = fullDate[0]
    month = fullDate[1]
    year = fullDate[2]
    # alterar o tipo das variáveis para inteiro 
    day = int(day)
    month = int(month)
    year = int(year)
    # declarar uma variável 'conditions' atribuindo valor 'None' para podermos considerar as estruturas de decisão
    conditions = None
    # declarar uma variável 'conditionsDay' atribuindo valor 'None' para podermos considerar as estruturas de decisão
    conditionsDay = None
    # declarar uma variável 'conditionsMonth' atribuindo valor 'None' para podermos considerar as estruturas de decisão
    conditionsMonth = None
    # declarar uma variável 'conditionsYear' atribuindo valor 'None' para podermos considerar as estruturas de decisão
    conditionsYear = None
    # estrutura de decisão 1:
    # ano deve ser um valor entre 1 e 9999
    if year >= 1 and year <= 9999 :
    # se positivo, 'conditionsYear' >> 'True'
        conditionsYear = True
    # se falso, 'conditionsYear' >> 'False'
    else:
        conditionsYear = False
    # estrutura de decisão 2:
    # mes deve ser um valor entre 1 e 12
    if month >= 1 and month <= 12 :
    # se positivo, 'conditionsMonth' >> 'True'
        conditionsMonth = True
    # se falso, 'conditionsMonth' >> 'False'
    else:
        conditionsMonth = False
    # estrutura de decisão 3:
    # para decidir sobre o dia é importante sabermos se o ano é bissexto
    #  vamos usar como base o código 'practice17.py' que já fez esse cálculo
    leapYear = None
    if (year%100) == 0 :
        if (year%400) == 0:
            leapYear = True
        else:
            leapYear = False
    else:
        if (year%4) == 0:
            leapYear = True
        else:
            leapYear = False
    # para cada mês o valor para dia muda:
    # se o mês for 2 e o ano for bissexto, então dia deve ser um valor entre 1 e 29
    if month == 2 and leapYear == True and day >= 1 and day <= 29 :
    # se positivo, 'conditionsDay' >> 'True'
        conditionsDay = True
    # se falso, 'conditionsDay' >> 'False'
    else:
        conditionsDay = False
    # se o mês for 4, 6, 9 ou 11, então dia deve ser um valor entre 1 e 30 
    if month == 4 or month == 6 or month == 9 or month == 11 and day >= 1 and day <= 30 :
    # se positivo, 'conditionsDay' >> 'True'
        conditionsDay = True
    # se falso, 'conditionsDay' >> 'False'
    else:
        conditionsDay = False
    # para os demais meses o valor de dia deve ser entre 1 e 31 
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day >= 1 and day <= 31 :
    # se positivo, 'conditionsDay' >> 'True'
        conditionsDay = True
    # se falso, 'conditionsDay' >> 'False'
    else:
        conditionsDay = False
    # Se os valores para 'conditionsDay', 'conditionsMonth' e 'conditionsYear' forem 'True', então 'conditions' recebe 'True'
    if conditionsDay == True and conditionsMonth == True and conditionsYear == True :
        conditions = True
    # caso contrário recebe 'False'
    else:
        conditions = False
    # se conditions for True, então imprimir para o usuário que a data informada é válida
    if conditions == True:
        print('A data informada é válida.')
    # caso contrário imprimir que a data informada não é válida.
    else:
        print('A data informada não é válida.')
except:
    print('Erro.')