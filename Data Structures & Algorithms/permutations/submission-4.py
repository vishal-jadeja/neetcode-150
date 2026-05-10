class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index):
            if (index == len(nums)):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        dfs(0)
        return res