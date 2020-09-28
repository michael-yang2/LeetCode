class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            return [-1]
        to_return = [None]*len(intervals)
        intervals_indices = {}
        for i in range(len(intervals)):
            intervals_indices[(intervals[i][0],intervals[i][1])] = i
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            start_idx = intervals_indices[tuple(interval)]
            right_index = bisect.bisect_right(intervals, [interval[1],-sys.maxsize])
            end_index = -1
            if right_index < len(intervals):
                end_index = intervals_indices[tuple(intervals[right_index])]
            to_return[start_idx] = end_index
        return to_return