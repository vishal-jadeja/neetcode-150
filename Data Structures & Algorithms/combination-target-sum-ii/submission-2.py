class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(pos, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                cur.append(candidates[i])
                dfs(i + 1, total + candidates[i], cur)
                cur.pop()

        dfs(0, 0, [])
        return res