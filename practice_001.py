# Practice 001 - List Changer

# Contexto
# Deve-se criar um programa que irá manipular uma lista de números conforme instruções abaixo:
# Serão passados como parâmetros dois itens: o primeiro é uma lista contendo números (tamanho variável) e o segundo será uma lista contendo
# em cada elemento um par de números (tratando-se de uma matriz de duas colunas, mas com quantidade de linhas variável).
# O primeiro item, que se trata da lista, será a base desse programa e sobre a qual serão feitas as interações.
# O segundo item, que se trata da matriz, serão os critérios para as alterações no primeiro item.
# Em cada par de números do segundo item são passadas as posições iniciais e finais da uma lista intermediária dentro do primeiro item 
# e que deve ser invertida (com essas posições incluídas nessa lista intermediária).
# O processo deve se repetir até que todos os pares do segundo item tenham feito as alterações no primeiro item.

# Exemplo: passados os parâmetros: (1, 2, 3, 4, 5), ( (2, 4) , (1, 3) ), o código irá pegar a lista como a lista que será ordenada
# e a matriz, que contém os valores (2, 4) e (1, 3) e irá alterar a lista. Na primeira linha da matriz temos os elementos (2, 4), então
# temos os números 2 e 4, o que significa que a parte da lista que será invertida está contida entre os elementos nas posições 2 e 4,
# com essas posições incluidas. Então na lista (1, 2, 3, 4, 5) os elementos entre as posições acima são: (3, 4, 5) que serão invertidos
# e o restante ficará inalterado. Como resultado da inversão teremos (5, 4, 3) e o restante que ficou inalterado é (1, 2) então a lista após
# primeira interação fica: (1, 2, 5, 4, 3) e vamos para a segunda interação. O processo deverá se repetir para todos os pares de elementos
# presentes no segundo parâmetro. 


# Input
# input_01 >> ((9, 8, 7, 6, 5, 4, 3, 2, 1, 0),((0, 9), (4, 5), (3, 6), (2, 7), (1, 8), (0, 9)))
# input_02 >> ((1, 2, 3, 2, 1),((1, 3), (0, 4), (2, 2)))
# input_03 >> ((5, 2, 5, 1, 4),((1, 3), (0, 4), (2, 2)))

# Output previsto
# output_01 >> (9, 1, 7, 3, 5, 4, 6, 2, 8, 0)
# output_02 >> (1, 2, 3, 2, 1)
# output_03 >> (4, 2, 5, 1, 5)


######################################## Practice_001 ########################################

def listChanger (arr, mat):
    principalArray = arr # atribuir uma variável para o parâmetro passado
    regulationPairs = mat # atribuir uma variável para o parâmetro passado
    for i in range(len(regulationPairs)): # determinar a recursividade da função
        leftMark = int(regulationPairs[i][0]) # definir marcadores para indicar o início da lista que será alterada
        rightMark = int(regulationPairs[i][1]) # definir marcadores para indicar o final da lista que será alterada
        leftList = principalArray[:leftMark] # definir uma variável para ser a primeira parte da lista inalterada, que conterá os itens até o 1º marcador
        toChangeList = principalArray[leftMark:rightMark+1] # definindo a lista que será alterada, incluindo o marcador inicial e o final (no caso do final precisa colocar +1 para incluí-lo nessa lista)
        changedList = toChangeList[::-1] # invertendo a lista que seria alterada e atribuindo a outra variável
        rightList = principalArray[rightMark+1:] # definir uma variável para ser a segunda parte da lista inalterada, que conterá os itens após o 2º marcador
        principalArray = leftList + changedList + rightList # concatenando as alterações para termos o resultado de cada recursividade
    return principalArray # retornar a lista principal após ter sido alterada conforme a função estabelecia


# Check para o primeiro input
print(listChanger((9, 8, 7, 6, 5, 4, 3, 2, 1, 0),((0, 9), (4, 5), (3, 6), (2, 7), (1, 8), (0, 9)))) # input 01
print('(9, 1, 7, 3, 5, 4, 6, 2, 8, 0)') # output previsto 01
print()

# Check para o segundo input
print(listChanger((1, 2, 3, 2, 1),((1, 3), (0, 4), (2, 2)))) # input 02
print('(1, 2, 3, 2, 1)') # output previsto 02
print()

# Check para o terceiro input
print(listChanger((5, 2, 5, 1, 4),((1, 3), (0, 4), (2, 2)))) # input 03
print('(4, 2, 5, 1, 5)') # output previsto 03
print()