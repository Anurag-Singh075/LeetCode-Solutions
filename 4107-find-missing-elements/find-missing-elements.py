class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        res = []
        for i in range(1,len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if curr-prev>1:
                res.extend(range(prev+1,curr))
        return res

