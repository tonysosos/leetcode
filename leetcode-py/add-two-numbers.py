# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        last = 0
        res = temp = ListNode(0)
        while a or b:
            if not a:
                x = 0
            else:
                x = a.val
            if not b:
                y = 0
            else:
                y = b.val
                
            val = x + y + last
            last = val // 10
            val = val % 10
            
            temp.next = ListNode(val)
            temp = temp.next
            if a: a = a.next
            if b: b = b.next
        
        if last:
            temp.next = ListNode(last)
            
        return res.next