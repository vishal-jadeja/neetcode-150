class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [ -c for c in freq.values()]
        q = deque()
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                updatedFreq = heapq.heappop(maxHeap) + 1
                if updatedFreq:
                    q.append([updatedFreq, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time