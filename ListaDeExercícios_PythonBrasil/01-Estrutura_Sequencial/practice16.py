# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

size = int(input('\nQual o tamanho em metros quadrados da área a ser pintada? '))
if size > 3:
    if size % 3 == 0:
        amountOfInk = size // 3
    else:
        amountOfInk = (size // 3) + 1
else:
    amountOfInk = 1
if amountOfInk > 18:
    if amountOfInk % 18 == 0:
        quantity = amountOfInk // 18
    else:
        quantity = (amountOfInk // 18) + 1
else:
    quantity = 1
value = int(quantity) * 80
print(f'''
Quantidade de latas de tinta a comprar: {quantity:.0f}
Valor total a pagar: R$ {value:.2f}
''')