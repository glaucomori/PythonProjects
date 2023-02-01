# Practice 002 - Missing Letters Game

# Contexto
# O game se inicia com duas strings distintas. O objetivo é que se possa obter a segunda string dentro da primeira string.
# Nesse game é possível remover ou adicionar caracteres na primeira string para adequar à segunda string, mas não é possível ordená-los.
# O programa deverá informar a quantidade mínima de adições que devem ser feitas para poder encontrar a segunda string na primeira.

# Exemplo:
# Simulação 01 >> dadas as strings 'inovação' e 'ação' o programa deve retornar o número '0' pois é possível obter a palavra 'ação'
# sem adicionar nenhum caractere na primeira string.
# Simulação 02 >> dadas as strings 'leão' e 'lobo' o programa deve retornar o número '2' pois é necessário adicionar 2 caracteres
# para poder obter a palavra 'lobo' a partir da palavra 'leão'. Porque na palavra 'leão' pode-se remover os caracteres 'e' e 'ã',
#  'lo' e depois adicionaria 2 caracteres: 'b' e 'o', para obter 'lobo'.


# Input
# input_01 >> ((ab), (abd))
# input_02 >> ((bola), (lagarto))
# input_03 >> ((torneira), (errado))

# Output previsto
# output_01 >> 1
# output_02 >> 5
# output_03 >> 4


######################################## Practice_002 ########################################

def missingLetters(word1, word2):
    basisWord = list(word1) # transformada em lista para pode interagir com cada caractere como um item de uma lista
    objectiveWord = list(word2) # transformada em lista para pode interagir com cada caractere como um item de uma lista

    #  se a primeira letra da palavra1 for igual da palavra 2 eu removo cada uma de sua respectiva lista
    #  se a primeira letra da plavra1 for diferente da palavra 2 eu removo apenas a primeira letra da palavra1
    #  quando as letras da palavra1 acabarem eu conto quantas letras tem na palavra2

    while len(basisWord) != 0: # criando uma condição para fazer a comparação enquanto a palavra1 ainda tiver caracteres
        if basisWord[0] == objectiveWord[0]: # comparando os primeiros caracteres de cada variável
            basisWord = basisWord[1:] # se a condição existir a palavra1 perde o primeiro caractere
            objectiveWord = objectiveWord[1:] # se a condição existir a palavra2 perde o primeiro caractere
        else: # o que faze caso a comparação não se prove verdadeira
            basisWord = basisWord[1:] # se a condição existir a palavra1 perde o primeiro caractere
    
    return len(objectiveWord)

# Check para o primeiro input
print(missingLetters(('ab'), ('abd'))) # input 01
print('1') # output previsto 01
print()

# Check para o segundo input
print(missingLetters(('bola'), ('lagarto'))) # input 02
print('5') # output previsto 02
print()

# Check para o terceiro input
print(missingLetters(('torneira'), ('errado'))) # input 03
print('4') # output previsto 03
print()