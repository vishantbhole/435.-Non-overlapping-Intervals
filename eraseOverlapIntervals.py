#435. Non-overlapping Intervals

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        lastEnd = intervals[0][1]
