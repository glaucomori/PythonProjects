# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

hourlyPayment = int(input('\nQuanto você ganha por hora? '))
monthlyHours = int(input('Quantos horas você trabalha no mes? '))
monthlySalary = hourlyPayment * monthlyHours
IRtax = monthlySalary * 0.11
INSStax = monthlySalary * 0.08    
laborUniorTax = monthlySalary * 0.05
liquidSalary = monthlySalary - IRtax - INSStax - laborUniorTax
print(f'''
+ Salário Bruto : R$ {monthlySalary:.2f}
- IR (11%) : R$ {IRtax:.2f}
- INSS (8%) : R$ {INSStax:.2f}
- Sindicato (5%) : R$ {laborUniorTax:.2f}
= Salário Liquido : R$ {liquidSalary:.2f}
''')