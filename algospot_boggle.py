testCaseNumber = int( input() )
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

def solution() :
    board = []
    result = []
    def isInBoundary(y,x):
        if 0 <= y and y < 5 and 0 <= x and x < 5 :
            return True
        else :
            return False

    def recursive(i,j,word):
        nonlocal board
        if len(word) == 0 :
            return True
        elif isInBoundary(i,j) == False :
            return False
        elif board[i][j] != word[0] :
            return False

        for k in range(0,8) :
            if recursive(i+dy[k],j+dx[k],word[1:]) == True :
                return True
                
        return False

        

        

    for i in range(0,5) :
        board.append(list(input()))

    words = []
    wordsNumber = int(input())
    for i in range(0,wordsNumber):
        words.append(input())

    for k,word in enumerate(words) :
        for i in range(0,5):
            for j in range(0,5):
                if recursive(i,j,word) == True :
                    result.append("YES")
                    break
            if k + 1 == len(result) :
                break
        if k + 1 != len(result) :
            result.append("NO")


    print(result)
    
    

    
for i in range(0,testCaseNumber):
    solution()



'''
output :

PRETTY YES
GIRL YES
REPEAT YES
KARA NO
PANDORA NO
GIAZAPX YES
'''