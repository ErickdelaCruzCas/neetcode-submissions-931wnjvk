class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        init = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < init[1]:
                count += 1
            else:
                init = intervals[i]

        return count
