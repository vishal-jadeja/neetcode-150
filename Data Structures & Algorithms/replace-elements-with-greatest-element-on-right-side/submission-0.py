class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        if not len(arr): return []

        maxi = arr[len(arr) - 1]
        for i in range(len(arr) - 1, 0, -1):
            maxi = max(maxi, arr[i])
            if i > 0: res.append(maxi)
        return res[::-1]
