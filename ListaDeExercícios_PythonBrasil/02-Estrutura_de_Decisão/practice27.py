# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

strawberry_weigth = input('Qual é o peso dos morangos? ')
strawberry_weigth = float(strawberry_weigth)
apple_weight = input('Qual é o peso das maçãs? ')
apple_weight = float(apple_weight)

strawberry_price_until_5kg = 2.50
strawberry_price_above_5kg = 2.20
apple_price_until_5kg = 1.80
apple_price_above_5kg = 1.50
discount = 1

total_weight = strawberry_weigth + apple_weight

if strawberry_weigth > 5:
    strawberry_price = strawberry_weigth * strawberry_price_above_5kg
else:
    strawberry_price = strawberry_weigth * strawberry_price_until_5kg

if apple_weight > 5:
    apple_price = apple_weight * apple_price_above_5kg
else:
    apple_price = apple_weight * apple_price_until_5kg

subtotal_price = apple_price + strawberry_price

if total_weight > 8:
    discount = 1 - 0.10

if subtotal_price > 25:
    discount = 1 - 0.10

total_price = subtotal_price * discount

print(f'O valor final é de R$: {total_price:.2f}')