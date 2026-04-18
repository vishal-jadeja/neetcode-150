# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None
            root = preorder[preStart]
            inRoot = inorder.index(root)
            leftEle = inRoot - inStart

            node = TreeNode(root)
            node.left = dfs(preStart + 1, preStart + leftEle, inStart, inRoot - 1)
            node.right = dfs(preStart + leftEle + 1, preEnd, inRoot + 1, inEnd)
            return node

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)