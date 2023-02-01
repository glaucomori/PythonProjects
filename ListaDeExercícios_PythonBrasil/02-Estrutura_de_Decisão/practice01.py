# Faça um Programa que peça dois números e imprima o maior deles.

try: # aplicando try/except para melhorar a segurança do código
    numbers = input('Informe dois números: ').split()
    maxNumber = max(numbers)
    print(f'O maior número é {maxNumber}')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro.')