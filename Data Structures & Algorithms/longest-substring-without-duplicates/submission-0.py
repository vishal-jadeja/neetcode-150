class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0
        charSet = set()
        l = 0
        cnt = 0
        for r in range(len(s)):
            while (s[r] in charSet):
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            cnt = max(cnt, r - l + 1)
        return cnt