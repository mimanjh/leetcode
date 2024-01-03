# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # backtracking
        letters = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        result = [''] if digits else []

        # go through each digits and append each of the letters to the result
        for digit in digits:
            result = [a + b for a in result for b in letters[digit]]
        return result
    
    # a different method using recursion
    # # dictionary of letters
    #     letters = {
    #         '2': ['a','b','c'],
    #         '3': ['d','e','f'],
    #         '4': ['g','h','i'],
    #         '5': ['j','k','l'],
    #         '6': ['m','n','o'],
    #         '7': ['p','q','r','s'],
    #         '8': ['t','u','v'],
    #         '9': ['w','x','y','z'],
    #     }
    #     result = []
    #     # if digits is empty, return empty list
    #     if not digits:
    #         return []
    #     # if digits is one digit, return the letter combinations of that digit
    #     if len(digits) == 1:
    #         return letters[digits]
    #     # otherwise, go through each digit and call the function combine to append each of the letters
    #     for digit in digits:
    #         result = self.combine(result, letters[digit])
    #     return result
    
    # def combine(self, result, letters):
    #     """
    #     :type result: List[str]
    #     :type letters: List[str]
    #     :rtype: List[str]
    #     """
    #     # if result is empty, return letters
    #     if not result:
    #         return letters
    #     # otherwise, go through each letter in letters and append it to each of the strings in result
    #     new_result = []
    #     for letter in letters:
    #         for string in result:
    #             new_result.append(string + letter)
    #     return new_result
        

print(Solution().letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations("")) # []
print(Solution().letterCombinations("2")) # ["a","b","c"]
print(Solution().letterCombinations("7")) # ["p","q","r","s"]
print(Solution().letterCombinations("234")) # ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
