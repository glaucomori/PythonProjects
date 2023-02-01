# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

number = input('Informe um número inteiro: ')
number = int(number)
oddNumber = number % 2

if oddNumber == 0:
    print('PAR')
else:
    print('ÍMPAR')