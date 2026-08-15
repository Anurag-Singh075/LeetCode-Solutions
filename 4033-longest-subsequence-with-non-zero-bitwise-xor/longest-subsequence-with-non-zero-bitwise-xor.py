class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        total = reduce(lambda a, b: a ^ b, nums, 0)
        if total != 0:
            return n
        if any(x != 0 for x in nums):
            return n - 1
        return 0
        