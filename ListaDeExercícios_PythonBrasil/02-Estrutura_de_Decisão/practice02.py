# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

try: # aplicando try/except para melhorar a segurança do código
    number = float(input('Informe um número: '))
    if number > 0:
        print('O número informado é positivo.')
    elif number < 0:
        print('O número informado é negativo.')
    else:
        print( 'O número informado não é positivo nem negativo.')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro.')