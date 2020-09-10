class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        def recur(row, col, word, seen):
            if not word:
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if self.board[row][col]!=word[0] or (row,col) in seen:
                return False
            seen.add((row, col))
            new_word = word[1:]
            ret = recur(row-1,col,new_word,seen) or recur(row+1,col,new_word, seen) or recur(row,col-1,new_word,seen) or recur(row, col+1, new_word, seen)
            seen.remove((row,col))
            return ret
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if recur(i, j, word, visited):
                    return True
        return False
                
        