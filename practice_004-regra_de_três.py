# Practice 001 - 'Rule of Three'

# Contexto
# Criar um programa que realize a conta da regra de três automaticamente com base em três números oferecidos

# Exemplo:
# Dado o enunciado: Se o valor de uma biscicleta com 30% de desconto é 280 reais, qual seria o valor dessa 
# biscicleta se o valor original fosse acrescido de 15%? Pela regra de três o resultado é 460.


# Input
# input_01 >> (280, 0.7, 1.15)
# input_02 >> (340, 0.85, 1)
# input_03 >> (360, 0.8, 1.2)

# Output previsto
# output_01 >> 460
# output_02 >> 400
# output_03 >> 540


######################################## Practice_001 ########################################

def ruleOfThree(number1, number2, number3):
    result = number1 * number3 / number2
    return result

# Check para o primeiro input
print(ruleOfThree(280, 0.7, 1.15)) # input 01
print('460') # output previsto 01
print()

# Check para o segundo input
print(ruleOfThree(340, 0.85, 1)) # input 02
print('400') # output previsto 02
print()

# Check para o terceiro input
print(ruleOfThree(360, 0.8, 1.2)) # input 03
print('540') # output previsto 03
print()

print(ruleOfThree(1, 16, 0.38))