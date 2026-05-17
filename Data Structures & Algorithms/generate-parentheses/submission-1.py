class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openC, closeC, s):
            if openC == closeC == n:
                res.append(s)
            
            if openC < n:
                dfs(openC + 1, closeC, s + "(")
            if closeC < openC:
                dfs(openC, closeC + 1, s + ")")

        dfs(0, 0, "")
        return res