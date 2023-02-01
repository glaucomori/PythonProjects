# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

values = input('Informe as notas: ').split()
valuesAsNumbers = (int(number) for number in values)
average = sum(valuesAsNumbers)/len(values)
print(f'A média das notas é: {average}')