# Faça um Programa que leia três números e mostre o maior deles.

try: # aplicando try/except para melhorar a segurança do código
    numbers = input('Informe três números: ').split()
    bigger = max(numbers)
    print(f'O maior dos números informados é: {bigger}')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro')