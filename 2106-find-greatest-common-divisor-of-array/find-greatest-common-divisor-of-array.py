class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        print(maxi,mini)
        while maxi>0 and mini>0:
            if maxi>mini:
                maxi=maxi%mini
            else:
                mini=mini%maxi
        if maxi==0:
            return mini
        return maxi



        # return gcd(max(nums), min(nums))