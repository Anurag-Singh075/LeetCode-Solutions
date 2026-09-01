class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        best = 0
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i != j:
                    best = max(best, digits[i] * digits[j])
        return best