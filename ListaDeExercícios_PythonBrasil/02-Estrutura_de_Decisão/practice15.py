# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

try:
    # pedir os três lados de um triangulo e armazenar em uma lista
    sides = input('Informe as medidas dos três lados: ').split()
    # ordenar os lados por tamanho dentro da lista
    sidesOrdered = sorted(sides)
    # armazenar cada lado em uma variável
    side1 = float(sidesOrdered[0])
    side2 = float(sidesOrdered[1])
    side3 = float(sidesOrdered[2])
    # declarar uma mensagem como NONE por enquanto para armazenar o resultado da estrutura de decisão
    message = None
    # verificar se a soma dos dois lados menores é maior que o lado maior
    if side1 + side2 > side3 :
    # em caso positivo aramzenar na variavel mensagem a informação de que os lados podem formar um triangulo
        message = 'Os lados informados podem formar um triângulo.'
    ## Se a mensagem foi posivita verificar o tipo do triangulo com base nas condições a seguir
    ## se todos os lados tiverem o mesmo tamanho >> Equilátero
        if side1 == side2 == side3 :
            triangleType = 'equilátero'
    ## se dois lados tiverem o mesmo tamanha >> Isóceles
        elif side1 == side2 :
            triangleType = 'isóceles'
        elif side2 == side3 :
            triangleType = 'isóceles'
    ## se todos os lados tiverem tamanhos diferente >> Escaleno
        elif side1 != side2 != side3 :
            triangleType = 'escaleno'
        else:
            triangleType = 'Erro'
    # em caso negativo aramzenar na variavel mensagem a informação de que os lados não podem formar um triangulo
    else:
        message = 'Os lados informados não podem formar um triângulo.'
    # Retornar as informações para o usuário
    print(f'{message}')
    if message == 'Os lados informados podem formar um triângulo.':
        print(f'O trinângulo é {triangleType}')

except:
    print('Erro')