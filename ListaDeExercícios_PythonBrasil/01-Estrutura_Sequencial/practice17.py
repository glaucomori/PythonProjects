# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.


# perguntar o tamanho em metros quadrados da área a ser pintada e atribuir a uma variável
wallSize = int(input('\nQual é o tamanho em metros quadrados da área a ser pintada? '))

# calcular o volume de tinta necessário considerando que 1 litro de tinta cobrem 6 metros quadrados
if wallSize > 6:
    if wallSize % 6 == 0:
        volumeInk = wallSize // 6
    else:
        volumeInk = (wallSize // 6) + 1
else:
    volumeInk = 1
print(f'Litros de tinta necessários = {volumeInk}')

# Calcular quantas latas de 18 litros serão necessárias para pintar
remainInk = 0
if volumeInk > 18:
    if volumeInk % 18 == 0:
        paintCans = volumeInk // 18
    else:
        paintCans = (volumeInk // 18) + 1
        remainInk = volumeInk % 18
else:
    paintCans = 1
waistedInkOnCans = (18 * paintCans) - volumeInk

# Calcular o valor para essas latas de 18 litros
valueCans = paintCans * 80

# Calcular quantos galões de 3,6 litros serão necessários para pintar
if volumeInk > 3.6:
    if volumeInk % 3.6 == 0:
        paintGallons = volumeInk // 3.6
    else:
        paintGallons = (volumeInk // 3.6) + 1
else:
    paintGallons = 1
waistedInkOnGallons = (3.6 * paintGallons) - volumeInk

# calcular o valor para esses galões de 3,6 litros
valueGallons = paintGallons * 25

# calcular quantos latas e galões serão necessários (juntos) para pintar
together = 0
cansTogether = 0
gallonsTogether = 0
if volumeInk < 18:
    gallonsTogether = paintGallons
else:
    if remainInk == 0:
        cansTogether = paintCans
    else:        
        if remainInk >= 3.6:
            if remainInk % 3.6 == 0:
                gallonsTogether = remainInk // 3.6
            else:
                gallonsTogether = (remainInk // 3.6) + 1
        else:
            gallonsTogether = 1
        cansTogether = paintCans - 1    
together = cansTogether + gallonsTogether
waistedInkTogether = ((cansTogether * 18) + (gallonsTogether * 3.6)) - volumeInk

# calcular o valor dessas latas e galões juntos
valueTogether = (cansTogether * 80) + (gallonsTogether * 25)

# informar as quantidades de tinta e os respectivos valores para cada caso
print(f'''
1ª situação: compranto apenas latas de 18 litros:
Latas a comprar: {paintCans}
Valor total: R$ {valueCans:.2f}
Desperdício de tinta: {waistedInkOnCans:.1f}

2ª situação: compranto apenas galões de 3,6 litros:
Galões a comprar: {paintGallons}
Valor total: R$ {valueGallons:.2f}
Desperdício de tinta: {waistedInkOnGallons:.1f}

3ª situação: compranto latas e galões:
Latas a comprar: {cansTogether}
Galões a comprar: {gallonsTogether}
Valor total: R$ {valueTogether:.2f}
Desperdício de tinta: {waistedInkTogether:.1f}
''')

