class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if not nums:
            return []
        sets = set(nums)
        m = k
        while m in sets:
            m = m + k
        return m