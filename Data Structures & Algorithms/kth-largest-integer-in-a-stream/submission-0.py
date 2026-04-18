class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.cap = k
        for i in range(min(k, len(nums))):
            heapq.heappush(self.minHeap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > self.minHeap[0]:
                if len(self.minHeap) == self.cap:
                    heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, nums[i])

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.cap:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            if len(self.minHeap) == self.cap:
                heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return (self.minHeap[0])