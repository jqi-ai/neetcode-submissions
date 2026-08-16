"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals):
            if i + 1 >= len(intervals):
                break
            next_start = intervals[i + 1].start
            curr_end = interval.end
            if curr_end > next_start:
                return False
        return True