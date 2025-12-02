#435. Non-overlapping Intervals

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        lastEnd = intervals[0][1]
         for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else:
                count += 1
                lastEnd = min(end, lastEnd)

        return count

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print("Output is : ", sol.eraseOverlapIntervals(intervals))

    intervals2 = [[1,2],[1,2],[1,2]]
    print("Output is : ", sol.eraseOverlapIntervals(intervals2))
