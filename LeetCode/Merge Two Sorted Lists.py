# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        merged_list = ListNode()
        # como a resposta precisa ser dada no formato ListNode vamos declarar uma variável com esse tipo
        current_node = merged_list
        # como se trata de nós e precisaremos retornar todos ordenados vamos criar outra variável para receber os demais valores
        # sem perder a referência do início da lista de nós
        while True:
            # definição de um loop infinito até a ordem de 'break'
            if list1 is None:
                # se a lista 1 estiver vazia, a lista 2 será o restante da lista
                current_node.next = list2
                # então o próximo nó da lista será o nó atual da lista 2 e ele direcionará para os demais nós da lista 2 que já estão ordenados
                break
                # considerando que a lista 1 já está vazia e a lista 2 já foi adicionada ao resultado, não é necessário mais operações
            if list2 is None:
                # se a lista 2 estiver vazia, a lista 1 será o restante da lista
                current_node.next = list1
                # então o próximo nó da lista será o nó atual da lista 1 e ele direcionará para os demais nós da lista 1 que já estão ordenados
                break
                # considerando que a lista 2 já está vazia e a lista 1 já foi adicionada ao resultado, não é necessario mais operações
            if list1.val >= list2.val:
                # no caso de as listas não estarem vazia vamos comparar os nós iniciais de cada lista
                # se o nó da lista 1 foi igual ou maior ao nó da lista 2...
                current_node.next = list2
                # então o próximo nó do resultado será o nó da lista 2
                list2 = list2.next
                # como o nó da lista 2 já foi adicionado ao resultado precisamos avançar para o próximo nó
            else:
                # caso as condições acima não sejam satisfeitas significa que o nó da lista 1 é menor que o nó da lista 2
                current_node.next = list1
                # então o próximo nó do resultado será o nó da lista 1
                list1 = list1.next
                # como o nó da lista 1 já foi acidionado ao resultado precisamos avançar para o próximo nó
            current_node = current_node.next
            # o valor que esse loop encontrou é anexado ao resultado e o loop irá definir o próximo nó para o resultado
        return merged_list.next
        # como o código trabalhou com a variavel current_node e current_node.next precisamos retornar o primeiro nó da lista
        # por isso o retorno é a variável inicial, porque ela indica qual é o nó que começa o resultado
        # mas como a variável era o current_node vamos direcionar a resposta da função para o nó seguinte à variavel inicial
        # que se refere ao primeiro nó do laço while do código