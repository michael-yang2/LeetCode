class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        paren = 0
        lst = list(S)
        for i in range(len(lst)):
            if lst[i] == '(':
                if paren == 0:
                    lst[i] = None
                paren+=1
            elif lst[i] == ')':
                paren-=1
                if paren == 0:
                    lst[i] = None
        to_return = ""
        for val in lst:
            if val != None:
                to_return += val
        return to_return
            