from collections import deque
import copy
N = int(input())

board = []

for i in range(N):
    board.append(list(input()))

board2 = copy.deepcopy(board)


dx = [0,1,0,-1]
dy = [-1,0,1,0]
def isIn(y,x):
    if 0 <= y and y < N and 0 <= x and x < N:
        return True
    else:
        return False

def bfs(y,x,board,value):
    board[y][x] = -1
    q = deque()
    q.append([y,x])

    while len(q) != 0 :
        index = q.popleft()
        y = index[0]
        x = index[1]
        
        for i in range(4):
            if isIn(y+dy[i] , x + dx[i]) and board[y+dy[i]][x+dx[i]] in value:
                board[y+dy[i]][x+dx[i]] = -1
                q.append([y+dy[i],x+dx[i]])





count = 0
for i in range(N*N) :
    value = board[i // N][i % N]

    if value != -1 :
        bfs(i // N, i % N  ,board,[value])
        count += 1

count2 = 0
for i in range(N*N) :
    value = board2[i // N][i % N]

    if value != -1 :
        
        if value == "G" or value == "R":
            value = ["R","G"]
        else : 
            value = [value]
        bfs(i // N, i % N  ,board2,value)
        count2 += 1


print(count,count2)