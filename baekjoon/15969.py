N = int(input())
scores = list(map(int,input().split()))

minimum = min(scores)
maximum = max(scores)

print(maximum - minimum)