# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
# na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# excessWeight = weight - 50
# tax = excessWeight * 4

def tax(weight):
    excessWeight = weight - 50
    tax = excessWeight * 4
    if weight > 50:
        return f'\nO peso dos peixes excedeu o limite estabelecido pelo estado de São Paulo.\nO excesso foi de {excessWeight:.2f} Kg.\nO valor da multa é R$ {tax:.2f}.\n'
    else:
        return '\nO peso dos peixes não excedeu o limite estabelecido pelo estado de São Paulo!\n'
    
print(tax(20))
print(tax(50))
print(tax(50.5))
print(tax(51))
print(tax(100))