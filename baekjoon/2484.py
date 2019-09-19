import collections 

N = int(input())

def calc(arr):
    d = collections.Counter(arr)
    count = sorted(d, key = lambda x: (d[x] , x ), reverse=True)
    
    if len(count) == 1 :
        return 50000 + 5000*count[0]
    elif len(count) == 2 :
        if d[count[0]] == 3 :
            return 10000 + 1000*count[0]
        else :
            return 2000 + (count[0] + count[1])*500
    elif len(count) == 3 :
        return 1000 + 100*count[0]
    elif len(count) == 4 :
        return 100 * count[0]

    return 0
result = 0

for i in range(N):
    arr = list(map(int,input().split()))
    score = calc(arr)
    result = max(result,score)

print(result)


