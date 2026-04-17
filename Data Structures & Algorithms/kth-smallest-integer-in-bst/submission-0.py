# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(curr):
            if not curr:
                return
            
            left = dfs(curr.left)
            arr.append(curr.val)
            right = dfs(curr.right)

        dfs(root)
        return arr[k - 1]