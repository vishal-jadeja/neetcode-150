class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        newIntervalStart = newInterval[0]
        newIntervalEnd = newInterval[1]
        while i < n and intervals[i][1] < newIntervalStart:
            res.append(intervals[i])
            i += 1

        while i < n and newIntervalEnd >= intervals[i][0]:
            newIntervalStart = min(newIntervalStart, intervals[i][0])
            newIntervalEnd = max(newIntervalEnd, intervals[i][1])
            i += 1
        res.append([newIntervalStart, newIntervalEnd])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res