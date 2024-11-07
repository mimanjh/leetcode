# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in numsMap:
                return [numsMap[diff], i]

            numsMap[num] = i

        return None


print(Solution().twoSum([2, 7, 11, 15], 9))  # [0,1]
print(Solution().twoSum([3, 2, 4], 6))  # [1,2]
print(Solution().twoSum([3, 3], 6))  # [0,1]
