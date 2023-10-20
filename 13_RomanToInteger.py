# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a variable to hold the total
        total = 0;
        # for every character in the string s, add an equivalent integer to the total
        for i in range(len(s)):
            if s[i] == 'I':
                total += 1;
            elif s[i] == 'V':
                total += 5;
            elif s[i] == 'X':
                total += 10;
            elif s[i] == 'L':
                total += 50;
            elif s[i] == 'C':
                total += 100;
            elif s[i] == 'D':
                total += 500;
            elif s[i] == 'M':
                total += 1000;
        # if the string contains IV, IX, XL, XC, CD, or CM, subtract the value of the first character from the total
        if 'IV' in s:
            total -= 2;
        if 'IX' in s:
            total -= 2;
        if 'XL' in s:
            total -= 20;
        if 'XC' in s:
            total -= 20;
        if 'CD' in s:
            total -= 200;
        if 'CM' in s:
            total -= 200;
        
        return total;

print(Solution().romanToInt("III")); # 3
print(Solution().romanToInt("LVIII")); # 58
print(Solution().romanToInt("MCMXCIV")); # 1994
