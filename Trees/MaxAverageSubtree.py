# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_avg = -sys.maxsize
        def recur(node):
            if not node:
                return (-sys.maxsize, 0)
            curr_sum = node.val
            curr_count = 1
            left_sum, left_count = recur(node.left)
            right_sum, right_count = recur(node.right)
            left_avg = -sys.maxsize
            right_avg = -sys.maxsize
            if left_count != 0:
                curr_sum+=left_sum
                curr_count+=left_count
                left_avg = left_sum/left_count
            if right_count != 0:
                curr_sum+=right_sum
                curr_count+=right_count
                right_avg = right_sum/right_count
            self.max_avg = max((self.max_avg, curr_sum/curr_count, left_avg, right_avg))
            return (curr_sum, curr_count)
        recur(root)
        return self.max_avg