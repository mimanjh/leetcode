# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        # go through each character in the string
        # for each character, check if it is the middle of the palindrome
        # if it is, then check if the left and right are the same
        # use max to store the longest palindrome
        for i in range(len(s)):
            result = max(result, self.helper(s, i, i), self.helper(s, i, i+1), key=len)
        return result
        
    def helper(self, s, i, j):
        # i and j are the middle index of the substring
        # palindrome logic: if the left and right are the same, then it is a palindrome
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
        

print(Solution().longestPalindrome("babad")) # "bab"
print(Solution().longestPalindrome("cbbd")) # "bb"
print(Solution().longestPalindrome("a")) # "a"
print(Solution().longestPalindrome("ac")) # "a"
print(Solution().longestPalindrome("ccc")) # "ccc"
print(Solution().longestPalindrome("aacabdkacaa")) # "aca"