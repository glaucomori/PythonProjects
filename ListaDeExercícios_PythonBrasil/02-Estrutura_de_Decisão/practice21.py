# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# ENTRADA
# Receber do usuário o valor a ser sacado
valor = input("Informe o valor a ser sacado: ")
valor = int(valor)

# PROCESSAMENTO
# conferir se o valor atende às restrições (entre 10 e 600)
# caso não atenda às restrições deve-se armazenar uma mensagem de retorno para o usuário na variável 'resposta'
if valor < 10:
    mensagem = 'O valor mínimo é de 10 reais.'
    print(mensagem)
    quit()
elif valor > 600:
    mensagem = 'O valor máximo é de 600 reais'
    print(mensagem)
    quit()
# declarar as variáveis para cada classe de nota: 100, 50, 10, 5 e 1
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0
# para cada variavel o programa deve verificar se existe a possibilidade de fornecer notas no respectivo valor e subtratir essa quantia do valor atual
# prosseguir para as demais variáveis
if valor > 99:
    notas100 = valor // 100
valor = valor - (100 * (valor // 100))
if valor > 49:
    notas50 = valor // 50
valor = valor - (50 * (valor // 50))
if valor > 9:
    notas10 = valor // 10
valor = valor - (10 * (valor // 10))
if valor > 4:
    notas5 = valor // 5
valor = valor - (5 * (valor // 5))
if valor > 0:
    notas1 = valor
# concatenar as notas numa variável 'resposta'
resposta = f'''{notas100} nota(s) de 100
{notas50} nota(s) de 50
{notas10} nota(s) de 10
{notas5} nota(s) de 5
{notas1} nota(s) de 1'''

# SAÍDA
# Imprimir para o usuário a 'resposta'
print(resposta)