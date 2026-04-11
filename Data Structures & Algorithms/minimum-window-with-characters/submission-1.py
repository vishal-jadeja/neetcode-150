class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        count = [0] * 128
        for ch in t:
            count[ord(ch)] += 1

        l = 0
        totalChar = 0
        minLen = float('inf')
        resL, resR = -1, -1

        for r in range(len(s)):
            count[ord(s[r])] -= 1
            if count[ord(s[r])] >= 0:
                totalChar += 1

            while totalChar == len(t):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    resL, resR = l, r
                count[ord(s[l])] += 1
                if count[ord(s[l])] > 0:
                    totalChar -= 1
                l += 1

        return s[resL: resR + 1] if minLen != float('inf') else ""