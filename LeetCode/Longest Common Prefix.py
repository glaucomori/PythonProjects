class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key = lambda x:len(x))
        # para obter uma lista com elementos classificados por tamanho, de forma crescente
        prefix = strs[0]
        # define o primeiro item da lista como sendo o prefixo.
        # como a função anterior classificou por tamanho, esse prefixo será o menor elemento da lista
        for i in range(len(strs[0]),0,-1):
        # dentro de um alcance que começa com o comprimento do primeiro elemento e vai até zero, de forma decrescente:
        # o primeiro elemento é a maior quantidade possível de caracteres que podem coincidir
        # o zero é a menor quantidade possível (no caso, não ter nenhuma coincidência)
        # o -1 indica que esse parte do código ira procurar de forma decrescente, do maior para o menor
            if all([prefix[:i] == strs[j][:i] for j in range(1,len(strs))]):
                # comparar todos os elementos: if all ([...]):
                # verificando se o prefixo até o elemento i 'prefix[:i]'
                # é igual aos caracteres iniciais dos demais elementos '== strs[j][:i]'
                # vai comparar com todos os elementos graças ao 'j' usado em '== strs[j][:i]' e à expressão 'for j in range(1,len(strs))'
                # que significa que vai comparar a partir do segundo elemento até o último elemento que é o comprimento da lista
                # vai comparar o mesmo fragmento graças ao 'i' usado em '== strs[j][:i]'
                return(prefix[:i])
                # so a verificação for positivo irá retornar o prefixo com os caracteres,
                # caso contrário ira repetir a operação, porém com um prefixo contendo um caractere a menos graças ao '-1' no laço for
        return ""
        # caso nenhum caractere corresponda nos demais elementos o programa retornará uma string vazia ""

strs = ["flower","flow","flight"]
output = "fl"
print(Solution.longestCommonPrefix(0,strs))
print(output)
