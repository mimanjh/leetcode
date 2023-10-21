# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check if the length of the string is odd
        # if so, return false
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        
        # create a mapping of parentheses
        bracketMapping = {'(': ')', '[': ']', '{': '}'}
        resultString = ""

        # iterate through the string 
        for char in s:
            # if the character is an open bracket, add the corresponding closing bracket to the resultString
            if char in bracketMapping:
                resultString += bracketMapping[char]
            # if the character is a closing bracket, and the resultString is empty or the last character in the resultString is not the same as the current character, return false
            elif len(resultString) == 0 or resultString[-1] != char:
                return False
            # else, remove the last character from the resultString
            else:
                resultString = resultString[:-1]
        
        # if the resultString is empty, return true
        if len(resultString) == 0:
            return True
        
        # else, return false
        return False

print(Solution().isValid("()")); # true 
print(Solution().isValid("()[]{}")); # true
print(Solution().isValid("(]")); # false
print(Solution().isValid("([)]")); # false
print(Solution().isValid("{[]}")); # true
