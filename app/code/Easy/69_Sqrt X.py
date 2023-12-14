# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x == 0):
            return 0
        res = x
        while not res * res - x < 1:
            res = (res + x / res) / 2
        return int(res)
        

    #     # use binary search using recursion
    #     left, right = 1, x
    #     return self.binarySearch(x, left, right)
    # def binarySearch(self, x, left, right):
    #     if (left <= right):
    #         mid = (left + right) // 2
    #         if (mid * mid <= x < (mid + 1) * (mid + 1)):
    #             return mid
    #         elif (mid * mid < x):
    #             return self.binarySearch(x, mid + 1, right)
    #         else:
    #             return self.binarySearch(x, left, mid - 1)
    #     else:
    #         return right


        # left = 1
        # right = x
        # while (left <= right):
        #     mid = (left + right) // 2
        #     if (mid * mid == x):
        #         return mid
        #     elif (mid * mid < x):
        #         left = mid + 1
        #     else:
        #         right = mid - 1



print(Solution().mySqrt(4)) # 2
print(Solution().mySqrt(8)) # 2
print(Solution().mySqrt(9)) # 3