"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda interval: interval.start)
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1]
            current_start = intervals[i]
            if prev_end.end > current_start.start:
                return False
        return True
        

