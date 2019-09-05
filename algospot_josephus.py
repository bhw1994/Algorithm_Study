import itertools
testCaseNumber = int(input())

def solution():
    N , K = map(int,input().split())

    warriors = []

    for i in range(1,N+1):
        warriors.append(i)
    
    warriors.remove(1)

    index = 0
    while(len(warriors) != 2):
        index += K -1
        index = index % len(warriors)
        warriors.remove(warriors[index])

    
    print(' '.join(map(str,warriors)))
    


for i in range(testCaseNumber):
    solution()

