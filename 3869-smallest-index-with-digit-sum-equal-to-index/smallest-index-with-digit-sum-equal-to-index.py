class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def n_sum(n):
            n=abs(n)
            s=0
            while n>0:
                s = s+n%10
                n=n//10
            return s
        for i, num in enumerate(nums):
            if n_sum(num)==i:
                return i
        return -1
