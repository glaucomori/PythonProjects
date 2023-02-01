# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 >> o produto do dobro do primeiro com metade do segundo.
# 2 >> a soma do triplo do primeiro com o terceiro.
# 3 >> o terceiro elevado ao cubo.
# 
# 1 >> resultado = (primeiro * 2) * (segundo / 2) >> simplificando fica >> resultado = primeiro * segundo
# 2 >> resultado = (primeiro * 3) + terceiro
# 3 >> resultado = terceiro**3

numbers = input('Informe 2 números inteiros e 1 número real: ').split()

number1 = int(numbers[0])
number2 = int(numbers[1])
number3 = float(numbers[2])

result1 = number1 * number2
result2 = number1 * 3 + number3
result3 = number3**3

print(f'o produto do dobro do primeiro com metade do segundo é: {result1}')
print(f'a soma do triplo do primeiro com o terceiro é: {result2}')
print(f'o terceiro elevado ao cubo é: {result3}')