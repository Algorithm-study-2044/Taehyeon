# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
            
        queue = [root]
        view = []
        while queue:
            temp = []
            _ = len(queue)
            for __ in range(_):
                temp.append(queue.pop(0))
            for now in temp:
                if now and now.left:
                    queue.append(now.left)
                if now and now.right:
                    queue.append(now.right)
            view.append(temp[-1].val)

        return view