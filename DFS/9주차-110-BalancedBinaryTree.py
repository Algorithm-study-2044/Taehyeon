# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self, root):
        if root == None:
            return 1

        left = self.height(root.left)
        right = self.height(root.right)

        if left and right:
            if abs(left-right) > 1:
                return None

            return max(left, right) + 1
        else:
            return None

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if self.height(root):
            return True
        else:
            return False
        