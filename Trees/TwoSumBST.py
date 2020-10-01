# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        tree1_set = set()
        def dfs(node):
            if not node:
                return
            tree1_set.add(node.val)
            dfs(node.left)
            dfs(node.right)
        def search(node):
            if not node:
                return False
            
            if target - node.val in tree1_set:
                return True
            return search(node.left) or search(node.right)
        dfs(root1)
        print(tree1_set)
        return search(root2)
        