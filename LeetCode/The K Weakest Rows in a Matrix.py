class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        arr = []

        for i in range(len(mat)):
            arr.append([sum(mat[i]), i])

        arr = sorted(arr, key= lambda item:item[0])

        return [i[1] for i in arr][:k]