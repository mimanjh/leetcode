# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # iterative solution
        dummy = cur = ListNode(0)
        # loop through both lists, comparing the elements of each list one by one until one reaches the end
        # add the smaller element to cur
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            # move cur to the next node
            cur = cur.next
        # add the rest of whichever list is not None to cur
        cur.next = list1 or list2
        return dummy.next

        # # loop through recursively, comparing the first elements of each list
        # # running recursively here is not a good idea, because it will take up too much memory
        # if not list1 or not list2:
        #     return list1 or list2
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

lst1 = ListNode(1)
lst1.next = ListNode(2)
lst1.next.next = ListNode(4)
lst2 = ListNode(1)
lst2.next = ListNode(3)
lst2.next.next = ListNode(4)
merged_list = Solution().mergeTwoLists(lst1, lst2)
while merged_list:
    print(str(merged_list.val), end = ' -> ')
    merged_list = merged_list.next
print(merged_list) # [1,1,2,3,4,4]