"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mpp = {None: None}
        temp = head
        while temp:
            newNode = Node(temp.val)
            mpp[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            copy = mpp[temp]
            copy.next = mpp[temp.next]
            copy.random = mpp[temp.random]
            temp = temp.next
        
        return mpp[head]