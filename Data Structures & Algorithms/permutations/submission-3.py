class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = [0] * (len(nums))
        def dfs(subset, freq):
            if (len(subset) == len(nums)):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if (freq[i] == 0):
                    subset.append(nums[i])
                    freq[i] = 1
                    dfs(subset, freq)
                    subset.pop()
                    freq[i] = 0
        dfs([], freq)
        return res