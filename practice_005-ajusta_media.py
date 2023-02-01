# Practice 001 - 'Average adjust'

# Contexto
# Dada uma média entre dois números, deve-se determinar qual o terceiro elemento para ajustar a média para um valor desejado

# Exemplo:
# Dado o enunciado: A média de idade de Ana e Carlos é de 75 anos. A média de idade de Ana, Carlos e Laura é 80 anos.
# Qual a idade de Laura? A resposta esperada é 90.


# Input
# input_01 >> (85, 90)
# input_02 >> (75, 80)
# input_03 >> (85, 75)

# Output previsto
# output_01 >> 100
# output_02 >> 90
# output_03 >> 55


######################################## Practice_001 ########################################

def average2to3(number1, number2):
    result = (number2*3)-(2*number1)
    return result

# Check para o primeiro input
print(average2to3(85, 90)) # input 01
print('100') # output previsto 01
print()

# Check para o segundo input
print(average2to3(75, 80)) # input 02
print('90') # output previsto 02
print()

# Check para o terceiro input
print(average2to3(85, 75)) # input 03
print('55') # output previsto 03
print()

print(average2to3(85, 75))