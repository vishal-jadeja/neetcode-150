class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, cnt in freq.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != []:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        return res        