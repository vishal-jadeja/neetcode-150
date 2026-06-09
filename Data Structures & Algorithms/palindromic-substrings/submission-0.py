class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += self.countPali(s, i, i)
            total += self.countPali(s, i, i + 1)
        return total

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res