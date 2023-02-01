# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

try: # aplicando try/except para melhorar a segurança do código
    gender = input('Informe o sexo (F/M): ')
    if gender == 'F':
        print('F - Feminino')
    elif gender == 'M':
        print('M - Masculino')
    else:
        print('Sexo inválido.')

except: # aplicando try/except para melhorar a segurança do código
    print('Erro.')