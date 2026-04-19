class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-s for s in stones]
        heapq.heapify(res)

        while len(res) > 1:
            first = -(heapq.heappop(res))
            second = -(heapq.heappop(res))
            if first > second:
                heapq.heappush(res, -(first - second))

        if not len(res): return 0
        return -(res[0])