/* 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

EX)
Input: nums = [3,2,4], target = 6
Output: [1,2]
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    if (nums.length == 2) {
        return ([0, 1])
    }
    
    hashTable = {}
    
    for (var i = 0; i < nums.length; i++) {
        var val = target - nums[i]
        
        if (val in hashTable) {
            if (i > hashTable[val]) {
                return ([hashTable[val], i])
            } else {
                return ([i, hashTable[val]])
            }
        }
        
        hashTable[nums[i]] = i
    }
};
