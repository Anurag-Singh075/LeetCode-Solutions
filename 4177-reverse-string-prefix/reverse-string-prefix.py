class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        strs=list(s)
        left= 0
        right =min(k, len(s)) - 1
        while left<right:
            temp = strs[left]
            strs[left]  = strs[right]
            strs[right] = temp
            left=left+1
            right=right-1
        result=""
        for s in strs:
            result=result+s
        return result

