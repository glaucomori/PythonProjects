# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

# ENTRADA
# solicitar ao usuário que entre com três notas parciais e armazenar em variáveis
notas = input("informe as três notas: ").split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])

# PROCESSAMENTO
# calcular a média das três notas
media = (nota1 + nota2 + nota3) / 3

# SAÍDA
# Imprimir para o usuário a mensagem de retorno da nota.
# Nos casos onde a média não for 10, também imprimir a média alcançada.
if media == 10.00:
    print('Aprovado com Distinção')
elif media >= 7:
    print(f'Aprovado!\nA média atingida foi de {media:.2f}')
elif media < 7:
    print(f'Reprovado!\nA média atingida foi de {media:.2f}')