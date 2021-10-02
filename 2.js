/* 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

EX
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
*/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

 var addTwoNumbers = function(l1, l2) {
    // set default variables
    let dummyHead = new ListNode(0);
    let p1 = l1;
    let p2 = l2;
    let current = dummyHead;
    let carry = 0;
    
    while (p1 !== null || p2 !== null) {
        let x = (p1 !== null) ? p1.val : 0;
        let y = (p2 !== null) ? p2.val : 0;
        let sum = x + y + carry;
        
        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;
        
        if (p1 !== null) {
            p1 = p1.next;
        }
        if (p2 !== null) {
            p2 = p2.next;
        }
    }
    if (carry > 0) {
        current.next = new ListNode(1);
    }
    return dummyHead.next;
};