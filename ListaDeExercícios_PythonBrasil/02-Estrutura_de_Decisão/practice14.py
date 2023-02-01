# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente 
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

try:
    firstGrade = float(input('Informa a sua primeira nota: '))
    secondGrade = float(input('Informa a sua segunda nota: '))
    meanGrade = (firstGrade + secondGrade) / 2
    concept = None

    if meanGrade < 4 :
        concept = 'E'
    elif meanGrade < 6 :
        concept = 'D'
    elif meanGrade < 7.5 :
        concept = 'C'
    elif meanGrade < 9 :
        concept = 'B'
    elif meanGrade < 10 :
        concept = 'A'
    else:
        concept = 'Erro'

    message = None
    if concept == 'E' or concept == 'D' or concept == 'C' :
        message = 'REPROVADO'
    elif concept == 'B' or concept == 'A' :
        message = 'APROVADO'
    else:
        message = 'Erro'

    print(f'''
    RESULTADOS
Sua primeira nota >> {firstGrade:.2f}
Sua segunda nota >> {secondGrade:.2f}
Sua média >> {meanGrade:.2f}
Seu conceito >> {concept}
Seu resultado>> {message}
''')

except:
    print('erro')