class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenSquare = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in seenRow[i] 
                or board[i][j] in seenCol[j] 
                or board[i][j] in seenSquare[(i//3, j//3)]):
                    return False
                seenRow[i].add(board[i][j])
                seenCol[j].add(board[i][j])
                seenSquare[(i//3, j//3)].add(board[i][j])
        return True