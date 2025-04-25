import numpy as np

n=8
board = np.zeros((n,n))

def check_column(board,row,column):
    for i in range(row,-1,-1):
        if board[i,column] == 1:
            return False
        
    return True
    
def check_diagonal(board,row,column):
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
        if board[i,j] == 1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(column,n)):
        if board[i,j] == 1:
            return False
        
    return True

def is_safe(board,row,column):
    return check_column(board,row,column) and check_diagonal(board,row,column)

solutions=[]

def solve(board,row,solutions):
    if row >= n:
        solutions.append(np.copy(board))
        return
    
    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row,col] = 1
            solve(board,row+1,solutions)
            board[row,col] = 0

solve(board,0,solutions)

for solution in solutions:
    print(solution)