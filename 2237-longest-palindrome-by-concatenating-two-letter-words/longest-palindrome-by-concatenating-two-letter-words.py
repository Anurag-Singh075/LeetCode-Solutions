class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cont = Counter(words)
        length = 0
        has_center = False
        for w in cont:
            if w[0] == w[1]:
                pairs = cont[w] // 2
                length += pairs * 4
                if cont[w] % 2 == 1:
                    has_center = True
            else:
                rev = w[1] + w[0]
                if w < rev:
                    length += 4 * min(cont[w], cont.get(rev, 0)) 
        if has_center:
            length += 2
        return length