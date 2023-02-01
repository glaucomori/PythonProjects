class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        elif n == 2:
            res = 2
        else:
            count = 3
            res_prev = 2
            res = 3
            while count < n:
                temp = res + res_prev
                res_prev = res
                res = temp
                count += 1
        return res
# Código para determinar o enésimo elemento da sequencia de Fibonacci

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
