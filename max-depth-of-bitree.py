# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        
        def find(root):
            if not root:
                return 0
            else:
                return max(1+find(root.left), 1+find(root.right))
        
        return find(root)