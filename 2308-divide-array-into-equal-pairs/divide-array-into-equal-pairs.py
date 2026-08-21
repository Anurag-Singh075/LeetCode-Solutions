class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        '''n=len(nums)
        w=[False]*n
        for i in range(n):
            if w[i]:
                continue
            found=False
            for j in range(i+1,n):
                if not w[j] and nums[j]==nums[i]:
                    w[i]=True
                    w[j]=True
                    found=True
                    break
            if not found:
                return False
        return True'''
        s=set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return len(s)==0
        