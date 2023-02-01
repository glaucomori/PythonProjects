# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

try: # aplicando try/except para melhorar a segurança do código
    letter = ord(input('Informe uma letra: '))
    classification = None
    if letter == 65 or letter == 69 or letter == 73 or letter == 79 or letter == 85: # para vogais maiúsculas
        print('A letra informada é uma vogal.')
    elif letter == 97 or letter == 101 or letter == 105 or letter == 111 or letter == 117: # para vocais minúsculas
        print('A letra informada é uma vogal.')
    elif letter > 64 and letter < 91: # para letras maiúsculas
        print('A letra informada é uma consoante.')
    elif letter > 96 and letter < 123: # para letras minpúsculas
        print('A letra informada é uma consoante.')
    else:
        print('Erro.')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro.')