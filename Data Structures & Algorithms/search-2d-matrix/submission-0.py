class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1

        while (top <= bottom):
            row = top + (bottom - top)//2
            if (matrix[row][0] > target):
                bottom = row - 1
            elif (matrix[row][-1] < target):
                top = row + 1
            else:
                break
        row = top + (bottom - top)//2
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False