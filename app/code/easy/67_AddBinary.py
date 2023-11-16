# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # binary addition rule: 0+0=0, 0+1=1, 1+1=0 carry 1
        # go from right to left of each string
        # add the digits and keep track of carry
        # append the sum%2 to result
        # append carry to result
        # reverse the result and return it
        result = ""
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            result += str(carry%2)
            carry //= 2

        return result[::-1]

        

print(Solution().addBinary("11", "1")) # "100"
print(Solution().addBinary("1010", "1011")) # "10101"