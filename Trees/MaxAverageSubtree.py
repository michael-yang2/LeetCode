# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def avg_at_node(self, node):
            if not node:
                return (-sys.maxsize, 0)
            curr_avg = node.val
            curr_count = 1
            left_avg, left_count = self.avg_at_node(node.left)
            right_avg, right_count = self.avg_at_node(node.right)
            if left_count != 0:
                curr_avg = (left_avg*left_count + node.val)/(left_count+curr_count)
                curr_count+=left_count
            if right_count != 0:
                curr_avg = ((curr_avg*curr_count)+right_avg*right_count)/(curr_count+right_count)
                curr_count+=right_count
            self.max_avg = max((self.max_avg, left_avg, right_avg, curr_avg))
            return (curr_avg, curr_count)
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_avg = -sys.maxsize
        a, b = self.avg_at_node(root)
        return self.max_avg