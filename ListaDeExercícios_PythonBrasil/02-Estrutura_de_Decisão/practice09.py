# Faça um Programa que leia três números e mostre-os em ordem decrescente.

try: # aplicando try/except para melhorar a segurança do código
    numbers = input('Informe três números: ').split()
    listOutOfOrder = [int(numbers[0]) , int(numbers[1]) , int(numbers[2])]
    orderedList = sorted(listOutOfOrder)
    finalList = orderedList[::-1]
    print(finalList)

except: # aplicando try/except para melhorar a segurança do código
    print('Erro')