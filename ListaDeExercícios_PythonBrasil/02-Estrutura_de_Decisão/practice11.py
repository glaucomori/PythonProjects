# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
#  o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

try: # aplicando try/except para melhorar a segurança do código
    entrySalary = input('Informe o seu salário >> ') # atribuir o valor do salário para uma variável usando a função 'input'
    salary = float(entrySalary) # converter o valor para o tipo 'float'
    newSalaryChange = None # declarar uma variável que receberá o valor do reajuste do salário
    
    if salary <= 280: # se o salário for até 280 ...
        newSalaryChange = 0.2 # ... o reajsute será de 20%
    elif salary <= 700: # se o salário for até 700 ...
        newSalaryChange = 0.15 # ... o reajsute será de 15%
    elif salary <= 1500: # se o salário for até 1500 ...
        newSalaryChange = 0.1 # ... o reajsute será de 10%
    else: # caso nenhuma das condições acima aconteçe (ou seja, for maior que 1500) ...
        newSalaryChange = 0.05 # ... o reajsute será de 5%
    
    salaryAdd = salary * newSalaryChange # o valor do aumento será o produto do salário com o percentual de reajuste
    newSalary = salary + salaryAdd # o novo salário será a soma do salário anterior com o valor do aumento do salário

    # informar na tela os valores solicitados no enunciado da questão
    print(f'''
Salário anterior:  R$ {salary:7.2f}
Reajuste aplicado:    {newSalaryChange:7.2f} %
Valor do aumento:  R$ {salaryAdd:7.2f}
Novo salário:      R$ {newSalary:7.2f}
    ''')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro')