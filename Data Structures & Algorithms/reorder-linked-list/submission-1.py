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
        
        first, second = head, prev
        while first and second:
            temp1Front, temp2Front = first.next, second.next
            first.next = second
            second.next = temp1Front
            first, second = temp1Front, temp2Front