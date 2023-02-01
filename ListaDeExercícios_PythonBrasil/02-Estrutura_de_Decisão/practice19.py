# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# ENTRADA
# declarar uma variável number que irá receber o número do usuário (especificar que deve ser inteiro, positivo e menor que 1000)
number = input('Informe um número inteiro positivo menor que 1000: ')

# PROCESSAMENTO

# alterar o tipo de variável para inteiro 
# verificar se atende às condições apresentadas no 'input' 
# se o valor informado não corresponder às condições especificadas deve-se imprimir mensagem de erro e encerrar o programa
try:
    number = int(number)
except:
    print('O número informado não atende às condições especificadas! Número não inteiro.')
    quit()

if number < 0:
    print('O número informado não atende às condições especificadas! Número não positivo.')
    exit()
elif number > 1000:
    print('O número informado não atende às condições especificadas! Número maior que 1000.')
    exit()
elif number == 1000:
    print('O número informado não atende às condições especificadas! Número igual a 1000.')
    exit()

# calcular a quatidade de centenas
# declarar uma variável 'centena = None' para a estrutura de decisão a seguir
centena = None
# verificar se o número é maior ou igual a 100
if number >= 100:
# se positivo, calcular a divisão inteira do número informado por 100 e armazenar o resultado na variável 'centena'
    centena = str(number // 100)
# se negativo então manter o valor 'None' para a variável 'centena'
else:
    centena = None
# se a divisão inteira do número informado por 100 for igual a 1 então deve-se adicionar a palavra 'centena' ao valor da variável
if (number // 100) == 1:
    centena = centena + ' centena'
# nos demais casos adicionar a palavra 'centenas' ao valor da variável 
elif (number // 100) > 1:
    centena = centena + ' centenas'

# calcular a quantidade de dezenas
# declarar uma variável 'dezena = None' para a estrutura de decisão a seguir
dezena = None
# se o número informado no início for maior que 100: 
if number >= 100:
# subtrair o valor do número informado do valor da divisão inteira do número informado por 100
    number = number - (100 * (number // 100))
# caso contrário 'continue'

# calcular a divisão inteira do número informado por 10 e armazenar o resultado na variável 'dezena'
if number >= 10:
    dezena = str(number // 10)
# se o número informado no início for menor que 10, então manter o valor 'None' para a variável 'dezena'
else:
    dezena = None
# se a divisão inteira do número informado por 10 for igual a 1 então deve-se adicionar a palavra 'dezena' ao valor da variável
if (number // 10) == 1:
    dezena = dezena + ' dezena'
# se for maior que 1 adicionar a palavra 'dezenas' ao valor da variável 
elif (number // 10) > 1:
    dezena = dezena + ' dezenas'

# calcular a quantidade de unidades 
# declarar uma variável 'unidade = None' para a estrutura de decisão a seguir
unidade = None
# se o número informado no início for maior que 10:
if number >= 10: 
# subtrair o valor do número informado do valor da divisão inteira do número informado por 10
    number = number - (10 * (number // 10))
# caso contrário 'continue'

# armazenar o resultado na variável 'unidade'
if number >= 1:
    unidade = str(number)
# se o número informado no início for menor que 1, então manter o valor 'None' para a variável 'dezena'
else:
    unidade = None
# se valor for 1 então deve-se adicionar a palavra 'unidade' ao valor da variável
if number == 1:
    unidade = unidade + ' unidade'
# se for maior que 1 adicionar a palavra 'unidades' ao valor da variável 
elif number > 1:
    unidade = unidade + ' unidades'

# SAÍDA 
# verificar quais variáveis mantém valor 'none'.
# concatenar as saídas de acordo com os valores, acrescentanto 'e' antes da última variável não 'none' 
# desde mais de uma não sejam 'none'
if centena != None:
    if dezena != None:
        if unidade != None:
            resposta = centena + ', ' + dezena + ' e ' + unidade
            print(resposta)
        else:
            resposta = centena + ' e ' + dezena
            print(resposta)
    else:
        if unidade != None:
            resposta = centena + ' e ' + unidade
            print(resposta)
        else:
            resposta = centena
            print(resposta)
else:
    if dezena != None:
        if unidade != None:
            resposta = dezena + ' e ' + unidade
            print(resposta)
        else:
            resposta = dezena
            print(resposta)
    else:
        if unidade != None:
            resposta = unidade
            print(resposta)
        else:
            resposta = "número não válido."
            print(resposta)