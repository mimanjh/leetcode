# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # # using string manipulation
        # # convert the number to a string and reverse it, then convert back to an integer
        # # if the number is negative, we'll need to add the negative sign back in
        # reversedX = int(str(abs(x))[::-1])
        # if reversedX.bit_length() < 32:
        #     return reversedX if x >= 0 else -reversedX
        # return 0

        # using integer division and modulo
        # dealing with negative numbers is a bit tricky, so we'll convert to positive
        # and then add the sign back in at the end
        # we'll use the modulo operator to get the last digit of the number
        # and then we'll multiply the current value by 10 and add the last digit
        # ex) 123 % 10 = 3, 0 * 10 + 3 = 3
        # ex) 12 % 10 = 2, 3 * 10 + 2 = 32
        # ex) 1 % 10 = 1, 32 * 10 + 1 = 321
        reversedX = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            lastDigit = x % 10
            reversedX = reversedX * 10 + lastDigit
            x //= 10
        # since this is a 32-bit integer, we need to check its boundaries
        return 0 if reversedX.bit_length() > 31 else reversedX * sign
        

print(Solution().reverse(123)) # 321
print(Solution().reverse(-123)) # -321
print(Solution().reverse(120)) # 21
print(Solution().reverse(1534236469)) # 0
print(Solution().reverse(1563847412)) # 0