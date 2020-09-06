from copy import deepcopy
import numpy as np
def suraksha_hi_savdhani_hai(chessboard,row):
    truth=[True]*n
    if row==n:
        return True
    for k in range(len(chessboard[row])):
        for i in range(0,row):
            for j in range(len(chessboard[i])):
                if chessboard[i][j] == 1 and (j == k or i-j == row-k or i+j == row+k):
                    truth[k]=False
    return any(truth)
def issafe(chessboard,row,col):
    for i in range(row):
        for j in range(len(chessboard[i])):
            if chessboard[i][j] == 1 and (j == col or i-j == row-col or i+j == row+col):
                return False
    return True



def solvenqueensproblem(chessboard,row):
    if row==n:
        print(np.matrix(chessboard))
        print("\n")
        return
    for j in range(len(chessboard[row])):
        if issafe(chessboard,row,j):
            chessboard[row][j]=1
            if suraksha_hi_savdhani_hai(chessboard,row+1):
                solvenqueensproblem(chessboard, row+1)
            else:
                chessboard[row][j] = 0
            chessboard[row][j] = 0
    return



if __name__ == "__main__":
    n=int(input())
    chessboard = [[0]*n for _ in range(n)]
    chessboard=deepcopy(chessboard)
    solvenqueensproblem(chessboard,0)
