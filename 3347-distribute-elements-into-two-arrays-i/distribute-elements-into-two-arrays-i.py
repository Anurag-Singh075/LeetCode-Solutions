class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2=[nums[1]]
        for i in range(2,len(nums)):
            last1 = (arr1 + [])[-1] 
            last2 = (arr2 + [])[-1]
            if last1>last2:
                arr1 = arr1+[nums[i]]
            else:
                arr2 = arr2+[nums[i]]
        result = []
        for x in arr1:
            result.append(x)
        for x in arr2:
            result.append(x)
    
        return result