# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

FahrenheitTemperature = float(input('Qual é a temperatura em °F? '))
CelciusTemperature = 5 * ((FahrenheitTemperature-32) / 9)
print(f'Essa temperatura equivale a {CelciusTemperature:.2f}°C.')