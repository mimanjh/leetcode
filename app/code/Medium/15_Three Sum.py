# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from itertools import combinations


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        # Split nums into three lists: negative numbers, positive numbers, and zeros
        negative, positive, zero = [], [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0: 
                negative.append(num)
            else:
                zero.append(num)

        # Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(negative), set(positive)

        # If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if zero:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
            if len(zero) >= 3:
                res.add(tuple([0, 0, 0]))

        # For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists in the positive number set
        for x, y in combinations(negative, 2):
            target = -1 * (x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))
        # For all pairs of positive numbers (1, 1), check to see if their complement (-2) exists in the negative number set
        for x, y in combinations(positive, 2):
            target = -1 * (x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]

        

print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([0,1,1])) # []
print(Solution().threeSum([0,0,0])) # [[0,0,0]]