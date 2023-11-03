# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use sliding window algorithm
        # use set instead of a list to store the unique substring of character and reduce complexity to O(1) instead of O(n)
        # use two pointer to indicate the start and end of the substring (left and right)
        # use max to store the max length of the substring
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result
    

        # Other solution from leetcode using sliding window algorithm as well
        # left = 0
        # seen = {}
        # output = 0
        
        # for right, curr in enumerate(s):
        #     if curr in seen:
        #         left = max(left, seen[curr] + 1)
        #     output = max(output, right - left + 1)
        #     seen[curr] = right

        # return output


print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("")) # 0
print(Solution().lengthOfLongestSubstring(" ")) # 1
print(Solution().lengthOfLongestSubstring("aab")) # 2
print(Solution().lengthOfLongestSubstring("cdd")) # 2