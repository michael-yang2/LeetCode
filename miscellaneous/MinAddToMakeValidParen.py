class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        extra = 0
        paren = 0
        for char in S:
            if char == '(':
                paren += 1
            if char == ')':
                paren -= 1
                if paren < 0:
                    extra += abs(paren)
                    paren = 0
        return extra + paren