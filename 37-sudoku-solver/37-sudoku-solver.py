class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==".":
                        for c in range(1,10):
                            if isValid(i,j,str(c)):
                                board[i][j]=str(c)
                                if solve(board)==True:
                                    return True
                                else:
                                    board[i][j]="."
                        return False
            
            return True
        def isValid(row,col,c):
            for i in range(9):
                if board[i][col]==c:
                    return False
                if board[row][i]==c:
                    return False
                if board[3*int((row/3)) + int(i/3)][3*int((col/3))+i%3]==c:
                    return False
            return True
        solve(board)
        return board
                    
                
                        