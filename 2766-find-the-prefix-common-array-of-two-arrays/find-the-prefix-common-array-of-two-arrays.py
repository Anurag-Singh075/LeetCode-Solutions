class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        chekA = [False] * (n + 1)
        chekB = [False] * (n + 1)
        C = [0] * n
        count = 0
        for i in range(n):
            a, b = A[i], B[i]
            chekA[a] = True
            chekB[b] = True
            if a == b:
                count += 1
            else:
                if chekB[a]:
                    count += 1
                if chekA[b]:
                    count += 1
            C[i] = count
        return C