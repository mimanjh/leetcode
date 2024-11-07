# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # numsMap = {}

        # for i, num in enumerate(numbers):
        #     diff = target - num

        #     if diff in numsMap:
        #         return [numsMap[diff], i + 1]

        #     numsMap[num] = i + 1

        # return None

        i = 0
        j = len(numbers) - 1

        while i < j:
            res = numbers[i] + numbers[j]
            if res < target:
                i += 1
            elif res > target:
                j -= 1
            else:
                return [i + 1, j + 1]

        return None


print(Solution().twoSum([2, 7, 11, 15], 9))  # [1,2]
print(Solution().twoSum([2, 3, 4], 6))  # [1,3]
print(Solution().twoSum([-1, 0], -1))  # [1,2]
