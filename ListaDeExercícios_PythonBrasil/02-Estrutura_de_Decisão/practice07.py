# Faça um Programa que leia três números e mostre o maior e o menor deles.

try: # aplicando try/except para melhorar a segurança do código
    numbers = input('Informe três números: ').split()
    biggest = max(numbers)
    smallest = min(numbers)
    print(f'O maior número é {biggest} e o menor número é {smallest}')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro')
