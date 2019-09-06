import collections
N = int(input())

words = []

size = 0
for i in range(N) :
    l = list(input())
    l.reverse()
    size = max(size,len(l))
    words.append(l)

alphabets = [0] * size

for i in range(size):
    arr = []
    for j in range(N):
        try :
            value = words[j][i]
            arr.append(value)
        except :
            pass
    alphabets[i] = arr

d= collections.defaultdict(int)
for i in range(size):
    level = alphabets[i]
    for alphabet in level :
        d[alphabet] += 10 ** i

resultDict = collections.defaultdict(int)
number = 9
for alphabet in sorted(d,key = d.get,reverse = True):
    resultDict[alphabet] = number
    number -= 1

result = 0
for k in d:
    result += d[k] * resultDict[k]

print(result)




