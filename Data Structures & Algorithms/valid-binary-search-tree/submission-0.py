# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftMax, rightMax):
            if not node:
                return True
            
            if not (leftMax < node.val < rightMax):
                return False

            left = dfs(node.left, leftMax, node.val)
            right = dfs(node.right, node.val, rightMax)
            return left and right

        return dfs(root, float("-inf"), float("inf"))