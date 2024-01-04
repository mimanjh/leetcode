# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 
# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # Depth First Search
        result = []
        self.dfs(result, '', 0, 0, n)
        return result
    
    def dfs(self, result, current, open, close, max):
        # base case
        if len(current) == max * 2:
            result.append(current)
            return
        # recursive case
        if open < max:
            self.dfs(result, current + '(', open + 1, close, max)
        if close < open:
            self.dfs(result, current + ')', open, close + 1, max)
        

print(Solution().generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(1)) # ["()"]
print(Solution().generateParenthesis(0)) # []
print(Solution().generateParenthesis(4)) # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]




































