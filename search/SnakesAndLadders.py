class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        num_to_row_col = {}
        going_right = True
        curr = (len(board)-1,0)
        for i in range(1,len(board)*len(board)+1):
            num_to_row_col[i] = curr
            if (curr[1] == len(board)-1 and going_right) or (curr[1] == 0 and not going_right):
                curr = (curr[0]-1,curr[1])
                going_right = not going_right
            elif going_right:
                curr = (curr[0],curr[1]+1)
            else:
                curr = (curr[0],curr[1]-1)
        seen = set([1])
        queue = deque()
        queue.append((1,0))
        while queue:
            square, move = queue.popleft()
            row, col, = num_to_row_col[square]
            if board[row][col]!=-1:
                square = board[row][col]
            if square == len(board)*len(board):
                return move
            for i in range(1,7):
                if square+i not in seen:
                    queue.append((square+i, move+1))
                    seen.add(square+i)
        return -1
            