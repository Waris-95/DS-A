# Duplicate Integer
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an empty set to store the numbers we've seen so far
        seen_numbers = set()
        # iterate through each number in the list
        for number in nums:
            if number in seen_numbers:
                # if it is, that means we've found a duplicate, so return true
                return True
            # if the number is not in the set, add it to the set
            seen_numbers.add(number)

        # if we finish the loop without finding any duplicates, return false
        return False
 
solution = Solution()

# Test Case 1
nums = [1, 2, 3, 3]
print(solution.hasDuplicate(nums))  # Output: True

# Test Case 2
nums = [1, 2, 3, 4]
print(solution.hasDuplicate(nums))  # Output: False
