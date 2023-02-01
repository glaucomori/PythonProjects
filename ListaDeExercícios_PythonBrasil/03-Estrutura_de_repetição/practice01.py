# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

repeat = 'on'
while repeat == 'on':
    nota = input('Informe uma nota entre zero e dez: ')
    nota = int(nota)
    if nota > 10:
        repeat = 'on'
        print('O valor informado não é válido. Vamos tentar novamente.')
    elif nota < 0:
        repeat = 'on'
        print('O valor informado não é válido. Vamos tentar novamente.')
    else:
        repeat = 'off'
        print('O valor informado é válido. Parabéns.')