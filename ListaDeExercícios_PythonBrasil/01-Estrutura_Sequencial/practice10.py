# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# F = (C*(9 / 5)) + 32

celsiusTemperature = float(input('Qual é a temperatura em °C? '))
fahrenheitTemperature = (celsiusTemperature * (9 / 5)) + 32
print(f'Essa temperatura equivale a {fahrenheitTemperature:.2f}°F.')