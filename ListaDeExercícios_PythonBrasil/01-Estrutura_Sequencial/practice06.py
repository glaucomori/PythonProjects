# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# área de um círculo >> A = pi * raio**2

import math

radius = input('Informe o raio do círculo: ')
circleArea = math.pi * float(radius)**2
print(f'A área desse círculo é de: {circleArea:.2f}')