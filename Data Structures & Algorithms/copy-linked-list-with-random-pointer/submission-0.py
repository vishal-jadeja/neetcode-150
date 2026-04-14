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
        mpp = {}
        temp = head
        while temp:
            newNode = Node(temp.val)
            mpp[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            copiedNode = mpp[temp]
            copiedNode.next = mpp[temp.next] if temp.next else None
            copiedNode.random = mpp[temp.random] if temp.random else None
            temp = temp.next
        
        return mpp[head] if head else None