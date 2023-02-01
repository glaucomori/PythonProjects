# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

try:
# ENTRADA
# Receber um número (que deve ser entre 1 e 7) que deve ser um número inteiro
# retornar 'valor inválido' caso a entrada seja diferente da esperada
    number = int(input('Informe um número >> '))
    
# PROCESSAMENTO
# para cada número, retornar um dia da semana seguindo a ordem (1-Domingo, 2- Segunda, etc.)
# criar uma lsita contendo os retornos esperados nas respectivas posições dos números
# #atribuir a uma variável final o valor correspondente desejadp 
    position = None
    if number >= 1 and number <= 7:
        position = number
    else: 
        position = 0
    weekDay = ('Valor inválido', 'Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado')
    final = weekDay[position]

# SAÍDA
# imprimir na tela a variável final
    print(final)
    
except:
    print('Erro"')