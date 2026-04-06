class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r
        while l <= r:
            mid = l + (r - l)//2
            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(float(p)/mid)
            if (timeTaken > h):
                l = mid + 1
            elif (timeTaken <= h):
                speed = mid
                r = mid - 1
        return speed