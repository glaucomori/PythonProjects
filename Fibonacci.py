# ### Entrada de Dados ###
# Não é necessária a entrada de dados por parte do usuário.
# Os dados iniciais para funcionamento do código são, respectivamente, o 11º e 12º números da Sequência de Fibonacci – 89 e 144.
#  Esses números podem ser atribuídos a duas variáveis quaisquer, que aqui chamarei de ‘n1’ e ‘n2’ respectivamente.

# ### Processamento de Dados ###
# Criar um laço de repetição que repita a operação 10 vezes:
# 	Realizar a soma das variáveis n1 e n2
# 	Armazenar o resultado da soma em uma variável ‘n3’
# 	Imprimir na tela a variável ‘n3’
# 	Atribuir à variável ‘n1’ o valor da variável ‘n2’ ( n1 = n2 )
# 	Atribuir à variável ‘n2’ o valor da variável ‘n3’ ( n2 = n3 )
 
# ### Saída de Dados ###
# A saída dos dados já foi incluída dentro do laço de repetição, então não é necessária uma outra saída ao final do programa


### Entrada de Dados ###
n1 = 89
n2 = 144

### Processamento de Dados ###
for i in range(10):
	n3 = n1 + n2
	print(n3)
	n1 = n2
	n2 = n3

### Saída de Dados ###
