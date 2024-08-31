
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #  a dictionary to store groups of anagrams
      anagrams = defaultdict(list)
      # iterate  through each string in the input list
      for word in strs:
        # sort chars in the chars and use it as the key
        key = ''.join(sorted(word))
        # append the word to the list corresponding to the sorted key
        anagrams[key].append(word)
      # return the values of the dictionry as list of list 
      return list(anagrams.values())
        