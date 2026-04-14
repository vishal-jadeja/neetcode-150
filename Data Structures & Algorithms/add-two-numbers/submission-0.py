# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        temp = dummy
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry

            carry = val//10
            val = val%10
            newNode = ListNode(val)
            temp.next = newNode
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next