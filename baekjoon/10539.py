N = int(input())
arr = list(map(int,input().split()))
sumArr = []
A = []

A.append(arr[0])
sumArr.append(arr[0])

for i in range(1,N):
    
    A.append(arr[i] * (i+1) - sumArr[i-1])
    sumArr.append(sumArr[i-1] + A[i] )

print(' '.join(map(str,A)))