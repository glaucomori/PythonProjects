# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00 (aqui existe um conflito, o enundiado pede contriuição sindical e no exemplo mostra INSS)
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

try: # aplicar try/except para maior segurança do código
    hourlyPayment = input('Qual o valor da sua hora de trabalho? ') # perguntar ao usuário o valor de sua hora de trabalho e atribuir a uma variável
    hourlyPaymentConverted = float(hourlyPayment) # alterar o tipo da variável para float e poder fazer cálculos com ela
    monthlyHours = input('Qual a quantidade de horas trabalhadas no mês? ') # perguntar ao usuário a quantidade de horas trabalhadas no mês e atribuir a uma variável
    monthlyHoursConverted = float(monthlyHours) # alterar o tipo da variável para float e poder fazer cálculos com ela

    # Declarar as variáveis
    # declarar uma variável que irá receber o salário bruto
    grossSalary = None
    # declarar uma variável que irá receber o percentual de desconto do imposto de renda
    IRpercent = None
    # declarar uma variável que irá receber o valor do imposto de renda
    IRvalue = None
    # declarar uma variável que irá receber a contribuição sindical
    tradeUnion = None
    # declarar uma variável que irá receber o valor do FGTS
    FGTSvalue = None
    # declarar uma variável que irá aglutinar o total de descontos
    totalDiscounts = None
    # declarar uma variável que irá receber o salário líquido
    netSalary = None

    # Calcular o valor do salário bruto e atribuir à variável
    # atribuir o valor do salário bruto a sua respectiva variável que é o produto do valor das horas trabalhadas com a quantidade de horas trabalhadas no mês
    grossSalary = hourlyPaymentConverted * monthlyHoursConverted
    
    # Calcular o valor do imposto de renda e atribuir à variável
    # o IR é calculado com base na tabela de desconto do IR mostrada no enunciado
    # Se o salário bruto for de até 900 (inclusive) não haverá desconto para o IR (o percentual de desconto do imposto de renda receberá valor igual a zero)
    if grossSalary <= 900:
        IRpercent = 0
    # Se o salário bruto for de até 1500 (inclusive) o desconto será de 5% (o percentual de desconto do imposto de renda receberá o valor igual a 0.05)
    elif grossSalary <= 1500:
        IRpercent = 0.05
    # Se o salário bruto for de até 2500 (inclusive) o desconto será de 10% (o percentual de desconto do imposto de renda receberá o valor igual a 0.10)
    elif grossSalary <= 2500:
        IRpercent = 0.10
    # Se o salário bruto for superior a 2500 o desconto será de 20% (o percentual de desconto do imposto de renda receberá valor igual a 0.20)
    else:
        IRpercent = 0.20
    # Após a definição do IR calcular o valor do imposto através do produto do IR com o salário bruto
    IRvalue = grossSalary * IRpercent

    # Calcular o valor da contribuição sindical e atribuir à variável
    # Conforme o enunciado o valor da contribuição sindical será de 3%
    # então a respectiva variável receberá o produto do salário bruto com o percentual da contribuição sindical (0.03)
    tradeUnion = grossSalary * 0.03

    # Calcular o valor total dos descontos e atribuir à variável
    # atribuir à respectiva variável o total de descontos que se refere à soma dos seguintes descontos: imposto de renda e contribuição sindical
    totalDiscounts = IRvalue + tradeUnion

    # Calcular o valor do FGTS e atribuir à variável
    # o valor do FGTS é fixo em 11%, então a respectiva variável receberá o produto do salátio bruto com a contribuição do FGTS (0.11)
    FGTSvalue = grossSalary * 0.11

    # Calcular o valor do salário líquido e atribuir à variável
    # o salário líquido é a diferença do salário bruto com o total de descontos
    # Atribuir o resultado dessa diferênça à respectiva variável do salário líquido
    netSalary = grossSalary - totalDiscounts

    # Imprimir na tela os valores solicitados de acordo com a formatação indicada no enunciado
    #         Salário Bruto: (5 * 220)        : R$ 1100,00
    #         (-) IR (5%)                     : R$   55,00  
    #         (-) INSS ( 10%)                 : R$  110,00 (aqui existe um conflito, o enundiado pede contriuição sindical e no exemplo mostra INSS)
    #         FGTS (11%)                      : R$  121,00
    #         Total de descontos              : R$  165,00
    #         Salário Liquido                 : R$  935,00
    print(f'''
Salário Bruto:            : R$ {grossSalary:7.2f}
(-) IR                    : R$ {IRvalue:7.2f}
(-) Trade Union           : R$ {tradeUnion:7.2f}
FGTS                      : R$ {FGTSvalue:7.2f}
Total de descontos        : R$ {totalDiscounts:7.2f}
Salário Liquido           : R$ {netSalary:7.2f}
    ''')

except: # aplicar try/except para maior segurança do código
    print('Erro!')