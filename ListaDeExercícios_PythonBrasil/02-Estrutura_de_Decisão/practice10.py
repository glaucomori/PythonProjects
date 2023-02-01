# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

try: # aplicando try/except para melhorar a segurança do código
    studentJourney = input('\nEm que turno você estuda? (M-matutino ou V-Vespertino ou N-Noturno) >> ')
    if studentJourney == 'M':
        print('\nBom dia!\n')
    elif studentJourney == 'V':
        print('\nBoa tarde!\n')
    elif studentJourney == 'N':
        print('\nBoa noite!\n')
    else:
        print('\nValor Inválido!\n')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro')