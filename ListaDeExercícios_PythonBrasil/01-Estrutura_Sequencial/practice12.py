# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte 
# fórmula: (72.7*altura) - 58

height = float(input('Informe a sua altura: '))
idealWeight = 72.7 * height - 58
print(f'O seu peso ideal é: {idealWeight:.2f} Kg')