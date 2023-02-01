# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, 
### a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

try:
    # Pedir o valor de 'a' e atribuir a uma variável
    a = input('Informe o valor de a: ')
    # transformar a variável para um tipo numérico, float por exemplo
    a = float(a)
    # verificar se o valor de 'a' é igual a zero.
    if a == 0 :
    # Se for igual a zero >> imprimir uma mensagem ao usuário e encerrar o programa
        print('Essa equação não é de 2º grau')
    # Se for diferente de zero >> continuar com as linhas do programa
    else:
    # Pedir o valor de 'b' e atribuir a uma variável
        b = input('Informe o valor de b: ')
    # transformar a variável para um tipo numérico, float por exemplo
        b = float(b)
    # Pedir o valor de 'c' e atribuir a uma variável
        c = input('Informe o valor de c: ')
    # transformar a variável para um tipo numérico, float por exemplo
        c = float(c)
    # calcular o delta da equação através da fórmula >> delta = b² - 4ac
        delta = b**2 - 4 * a * c
    # verificar o valor de delta e tomar as decisoes seguintes com base na condição:
    # se delta for um valor negativo >> Imprimir uma mensagem ao usuário: 'A equação não possui raízes reais.' e encerrar o programa
        if delta < 0 :
            print('A equação não possui raízes reais.')
    # se delta for igual a zero >> calcular a raiz da equação com base na fórmula: -b / 2 * a e imprimir o resultado para o usuário
        elif delta == 0 :
            solution = ((-b) / (2 * a))
            print(f'A raiz da equação é: {solution:.2f}')
    # se delta for um valor positivo >> calcular as raízes da equação e imprimir o resultado para o usuário
        else:
    # a primeira raiz é >> (-b - delta**(1/2)) / 2 * a
            solution1 = ((-b - delta**(1/2)) / 2 * a)
    # a segunda raiz é >> (-b + delta**(1/2)) / 2 * a
            solution2 = ((-b + delta**(1/2)) / 2 * a)
    # informar as duas raízes ao usuário e encerrar o programa
            print(f'As raízes da equação são: {solution1:.2f} e {solution2:.2f}')
except:
    print('Erro!')