# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                         Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

meat_type = input("Qual foi a carne comprada? F-filé duplo, A-alcatra, P-picanha ")
meat_quantity = input('Qual foi a quantidade de carne comprada em quilos? ')
meat_quantity = float(meat_quantity)
payment_method = input('Qual será a forma de pagamento? V-à vista, D-débito, C-crédito, T-tabajara ')
meat = None

file_price_until_5kg = 4.90
file_price_above_5kg = 5.80
alcatra_price_until_5kg = 5.90
alcatra_price_above_5kg = 6.80
picanha_price_until_5kg = 6.90
picanha_price_above_5kg = 7.80
c = 7.80
discount = 1

if payment_method == 'T':
    discount = 1 -  0.05

if meat_quantity > 5:
    file_price = file_price_above_5kg
    alcatra_price = alcatra_price_above_5kg
    picanha_price = picanha_price_above_5kg
else:
    file_price = file_price_until_5kg
    alcatra_price = alcatra_price_until_5kg
    picanha_price = picanha_price_until_5kg

if meat_type == 'F':
    meat = 'Filé Duplo'
    meat_chosen = file_price
elif meat_type == 'A':
    meat = 'Alcatra'
    meat_chosen = alcatra_price
elif meat_type == 'P':
    meat = 'Picanha'
    meat_chosen = picanha_price
else:
    meat = 'Erro'
    print('Erro no tipo de carne')
    quit()

total_price = meat_chosen * meat_quantity

if payment_method == 'V':
    payment_method = 'A vista'
elif payment_method == 'D':
    payment_method = 'Cartão de Débito'
elif payment_method == 'C':
    payment_method = 'Cartão de Crédito'
elif payment_method == 'T':
    payment_method = 'Cartão Tabajara'
else:
    print('Erro no tipo de pagamento')
    quit()

discount_value = total_price - (total_price * discount)
amount_to_pay = total_price - discount_value

print(f'''
            CUPOM FISCAL

Tipo de carne:        {meat}
Quantidade de carne:  {meat_quantity:.2f} Kg
Preço total:          R$ {total_price:.2f}
Tipo de pagamento:    {payment_method}
Valor do desconto:    R$ {discount_value:.2f}
Valor a pagar:        R$ {amount_to_pay:.2f}
''')