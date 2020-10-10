class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indices = []
        vals = []
        max_rect = 0
        for i in range(len(heights)):
            if not vals:
                vals.append(heights[i])
                indices.append(i)
            if heights[i] <= vals[-1]:
                index_to_add = i
                while vals and heights[i] <= vals[-1]:
                    max_rect = max(vals[-1] * (i - indices[-1]), max_rect)
                    index_to_add = min(index_to_add, indices[-1])
                    indices.pop()
                    vals.pop()
                vals.append(heights[i])
                indices.append(index_to_add)
            else:
                vals.append(heights[i])
                indices.append(i)
        while vals:
            max_rect = max(max_rect, (len(heights) - indices[-1]) * vals[-1])
            vals.pop()
            indices.pop()
        return max_rect