# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        nodes = deque()
        to_return = []
        levels_added = set()
        nodes.append((root,0))
        while nodes:
            node, level = nodes.popleft()
            if not node:
                continue
            if level not in levels_added:
                levels_added.add(level)
                to_return.append(node.val)
            nodes.append((node.right,level+1))
            nodes.append((node.left, level+1))
        return to_return