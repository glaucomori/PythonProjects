# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total 
# do seu salário no referido mês.

hourlyPayment = float(input('Quanto você ganha por hora? '))
monthlyHours = float(input('Quantas horas você trabalhou no mês? '))
wage = hourlyPayment * monthlyHours
print(f'O seu salário para esse mês será de: R${wage:.2f}')