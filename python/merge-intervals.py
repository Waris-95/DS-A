# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort()

        # Initialize stack with the first interval
        merged = [intervals[0]]

        # Iterate over the intervals starting from the second
        for i in range(1, len(intervals)):
            # Get the last interval in the merged list
            last_merged = merged[-1]

            # Check if the current interval overlaps with the last merged interval
            if intervals[i][0] <= last_merged[1]:  # Overlapping intervals
                # Merge intervals by updating the end time to the maximum end time
                last_merged[1] = max(last_merged[1], intervals[i][1])
            else:  # No overlap
                # Add the current interval to the merged list
                merged.append(intervals[i])

        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals))
# Output: [[1,6],[8,10],[15,18]]
