# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # if the len of the str are different, they cannot be anagrams
    if len(s) != len(t): 
      return False
    
    # create dictionaries to count the frequency of each char
    count_s= {}
    count_t= {}

    # count the chars in the first string
    for char in s:
      if char in count_s:
        count_s[char] += 1
      else:
        count_s[char] = 1

    # count the chars in the second string
    for char in t:
      if char in count_t:
        count_t[char] += 1
      else: 
        count_t[char] = 1

    return count_s == count_t
  
sol = Solution()

# Example 1
print(sol.isAnagram("racecar", "carrace"))  # Output: True

# Example 2
print(sol.isAnagram("jar", "jam"))  # Output: False

    

