class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n>=2:
            intervals = sorted(intervals,key=lambda x: x[0])
            prev= intervals[0]
            for each in range(1,n):
                if prev[1]> intervals[each][0]:
                    return False
                prev = intervals[each]
            return True
        else:
            return True

