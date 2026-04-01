class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                res = max(res, min(heights[l], heights[r])*(r - l))
        return res
            