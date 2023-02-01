# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

height = input('Qual é a sua altura? ')
gender = str(input('você é homem ou mulher? '))
try: # aplicando try/except para melhorar a segurança do código
    if gender.lower() == 'homem':
        weight = 72.7 * float(height) - 58
        print(f'O peso ideal é: {weight:.2f} Kg')
    elif gender.lower() == 'mulher':
        weight = 62.1 * float(height) - 44.7
        print(f'O peso ideal é: {weight:.2f} Kg')
    else:
        print('Não foi possível calcular seu peso ideal com a informação fornecida')
except: # aplicando try/except para melhorar a segurança do código
    print('Não foi possível calcular seu peso ideal com a informação fornecida')