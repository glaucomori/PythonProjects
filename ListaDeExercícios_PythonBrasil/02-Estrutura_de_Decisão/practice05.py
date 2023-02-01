# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

try: # aplicando try/except para melhorar a segurança do código
    studentScore = input('Informe as duas notas parciais do aluno: ').split()
    scoreMain = (float(studentScore[0]) + float(studentScore[1])) / 2
    if scoreMain == 10:
        print(f'Média >> {scoreMain}\nAprovado com Distinção')
    elif scoreMain >= 7:
        print(f'Média >> {scoreMain}\nAprovado')
    else:
        print(f'Média >> {scoreMain}\nReprovado')

except: # aplicando try/except para melhorar a segurança do código
    print(scoreMain)