class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count("1")
        zeros = n - ones
        if abs(ones - zeros) > 1:
            return -1
        zero_at_odd = 0 
        one_at_odd = 0  
        for i, c in enumerate(s):
            if i % 2 == 0:
                continue
            if c == "0":
                zero_at_odd += 1
            else:
                one_at_odd += 1
        if zeros == ones:
            return min(zero_at_odd, one_at_odd)
        elif zeros > ones:
            return zero_at_odd
        else:
            return one_at_odd