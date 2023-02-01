# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

numbers = input('Informe dois números: ').split()
number1 = numbers[0]
number1 = int(number1)
number2 = numbers[1]
number2 = int(number2)
operation = input('Qual operação você deseja realizar? adição(1), subtração(2), multiplicação(3) ou divisão(4) >> ')
operation = int(operation)
if operation == 1:
    result = number1 + number2
elif operation == 2:
    result = number1 - number2
elif operation == 3:
    result = number1 * number2
elif operation == 4:
    result = number1 / number2
else:
    print('Houve um erro.')
    quit()

if result % 2 == 0:
    answer = 'O resultado é um número par, '
else:
    answer = 'O resultado é um número ímpar, '

if result > 0:
    answer = answer + 'positivo e '
elif result < 0:
    answer = answer + 'negativo e '
else:
    answer = 'O resultado é 0.'
    print(answer)
    quit()

rounded = round(result)
if result == rounded:
    answer = answer + 'inteiro.'
else:
    answer = answer + 'decimal.'

print(result)
print(answer)