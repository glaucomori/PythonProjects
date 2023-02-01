# Faça um Programa que peça dois números e imprima a soma.

inputList = input('Informe os números a serem somados: ').split()
numbers = (int(number) for number in inputList)
result = sum(numbers)
print(f'A soma dos números é: {result}')