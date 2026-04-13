# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tempFront = second.next
            second.next = prev
            prev = second
            second = tempFront
        
        temp1, temp2 = head, prev
        while temp1 and temp2:
            temp1Front = temp1.next
            temp2Front = temp2.next
            temp1.next = temp2
            temp2.next = temp1Front
            temp1 = temp1Front
            temp2 = temp2Front