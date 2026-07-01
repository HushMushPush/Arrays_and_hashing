class Solution:
    def isValidSudoku(self, board): # List[List[str]] -> bool
        
        k = {}
        for i in range(9):
            for ii in range(9):
                if board[i][ii] in k.keys():
                    return False
                elif board[i][ii] not in k.keys() and board[i][ii] != '.':
                    k[board[i][ii]] = 1
            k = {}

        for ii in range(9):
            for i in range(9):
                if board[i][ii] in k.keys():
                    print(2)
                    return False
                elif board[i][ii] not in k.keys() and board[i][ii] != '.':
                    k[board[i][ii]] = 1
            k = {}
        
        x, y = 0, 0

        for x in (0, 3, 6):
            for y in (0, 3, 6):
                for i in range(3):
                    for ii in range(3):
                        if board[x + i][y + ii] in k.keys():
                            return False
                        elif board[x + i][y + ii] not in k.keys() and board[x + i][y + ii] != '.':
                            k[board[x + i][y + ii]] = 1
                k = {}

        return True
    
board = []
for i in range(9):
    board.append(input().split()) # len( input().split() ) = 9,
                                  # 1 <= input().split() [i] <= 9
                                  # or input().split() [i] = '.'

abs = Solution()

print(abs.isValidSudoku(board))