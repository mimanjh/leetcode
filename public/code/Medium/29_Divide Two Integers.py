# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 
# Constraints:

# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # set the sign of the result
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        # remove the sign of the dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        # initialize the quotient
        quotient = 0
        # loop until the dividend is greater than the divisor
        while dividend >= divisor:
            # initialize the temp_divisor variable
            temp_divisor = divisor
            # initialize the multiplier
            multiplier = 1
            # loop until the temp_divisor is less than the dividend
            while temp_divisor <= dividend:
                # update the dividend
                dividend -= temp_divisor
                # update the quotient
                quotient += multiplier
                # update the temp_divisor
                temp_divisor += temp_divisor
                # update the multiplier
                multiplier += multiplier
        # return the result and constrain it to the 32-bit signed integer range
        return min(max(-2**31, sign * quotient), 2**31 - 1)
        

print(Solution().divide(10, 3)) # 3
print(Solution().divide(7, -3)) # -2
print(Solution().divide(0, 1)) # 0
print(Solution().divide(3968492, 6)) # 661415