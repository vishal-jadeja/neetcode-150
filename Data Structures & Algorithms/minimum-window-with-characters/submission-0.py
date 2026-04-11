class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = [0]*256
        if len(t) > len(s): return ""
        for ch in t:
            count[ord(ch) - ord("a")] += 1
        
        l = 0
        totalChar = 0
        res = ""
        for r in range(len(s)):
            index = ord(s[r]) - ord("a")
            count[index] -= 1
            if count[index] >= 0:
                totalChar += 1
            while totalChar == len(t):
                if res == "" or len(res) > r - l + 1: 
                    res = s[l: r + 1]
                lIndex = ord(s[l]) - ord("a")
                count[lIndex] += 1
                if (count[lIndex] > 0):
                    totalChar -= 1
                l += 1
        return res

