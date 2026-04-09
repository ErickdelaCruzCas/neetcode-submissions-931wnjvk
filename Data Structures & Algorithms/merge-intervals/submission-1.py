class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x:x[0])
        acum = intervals[0]
        for i in range(1, len(intervals)):
            if acum[1] >= intervals[i][0]:
                acum[:] = [acum[0], max(acum[1], intervals[i][1])]
            else:
                res.append(acum[:])
                acum = intervals[i]
        res.append(acum)
        return res 
