class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            ans = 0
            if (height[l] <= height[r]):
                l += 1
                leftMax = max(leftMax, height[l])
                ans += min(leftMax, rightMax) - height[l]
                if (ans > 0): res += ans
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += min(leftMax, rightMax) - height[r]
                if (ans > 0): res += ans
        return res
