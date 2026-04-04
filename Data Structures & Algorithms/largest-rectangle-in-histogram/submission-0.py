class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, curHeight in enumerate(heights):
            start = i
            while stack and stack[-1][1] > curHeight:
                index, eleHeight = stack.pop()
                maxArea = max(maxArea, eleHeight * (i - index))
                start = index
            stack.append((start, curHeight))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
