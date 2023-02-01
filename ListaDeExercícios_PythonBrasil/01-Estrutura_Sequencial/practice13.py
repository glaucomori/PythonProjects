# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

height = float(input('Qual é a sua altura? '))
idealWeightFemale = height * 62.1 - 44.7
idealWeightMale = height * 72.7 - 58

print(f'O peso ideal para homens com essa altura é: {idealWeightMale:.2f} Kg')
print(f'O peso ideal para mulheres com essa altura é: {idealWeightFemale:.2f} Kg')