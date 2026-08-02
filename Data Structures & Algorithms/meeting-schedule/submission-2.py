"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur.start >= start and cur.start < end:
                return False
            end = cur.end

        return True



