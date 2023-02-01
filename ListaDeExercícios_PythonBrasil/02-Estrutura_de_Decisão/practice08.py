# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato

try: # aplicando try/except para melhorar a segurança do código
    product1 = float(input('Informe o preço do produto 1: '))
    product2 = float(input('Informe o preço do produto 2: '))
    product3 = float(input('Informe o preço do produto 3: '))

    priceList = [product1 , product2 , product3]
    cheapestPrice = min(priceList)

    if cheapestPrice == product1:
        print('O produto mais barato é o produto 1')
    elif cheapestPrice == product2:
        print('O produto mais barato é o produto 2')
    else:
        print('O produto mais barato é o produto 3')

except: # aplicando try/except para melhorar a segurança do código
    print('erro')