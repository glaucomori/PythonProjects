# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: 
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
# o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

fuelvolume = input('Qual foi o volume de combustível? ')
fuelvolume = float(fuelvolume)
fueltype = input('Qual foi o combustível usado? (A-álcool, G-gasolina) ')
alcohol_discount_until_20 = 1 - 0.03
alcohol_discount_above_20 = 1 - 0.05
gasoline_discount_until_20 = 1 - 0.04
gasoline_discount_above_20 = 1 - 0.06
alcohol_price_per_liter = 1.90
gasoline_price_per_liter = 2.50

if fueltype == 'A':
    if fuelvolume > 20:
        cost = alcohol_price_per_liter * fuelvolume * alcohol_discount_above_20
    else:
        cost = alcohol_price_per_liter * fuelvolume * alcohol_discount_until_20
if fueltype == 'G':
    if fuelvolume > 20:
        cost = gasoline_price_per_liter * fuelvolume * gasoline_discount_above_20
    else:
        cost = gasoline_price_per_liter * fuelvolume * gasoline_discount_until_20

print(f'O valor final é de R$ {cost:.2f}')