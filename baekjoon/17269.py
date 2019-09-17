n , m = map(int,input().split())
first, second = map(list,input().split())

size = max(len(first),len(second))

mix = []
for i in range(size):
    try:
        mix.append(first[i])
    except :
        pass

    try:
        mix.append(second[i])
    except :
        pass


values = list("32124313113132122212111221")
alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


d = {}
def setDict(k,v):
    global d
    d[k] = int(v)

list(map(setDict , alphabets,values))


for i in range(len(mix)):
    mix[i] = d[mix[i]]


now = mix[:]
while True:

    next = []
    for i in range(len(now) - 1):
        sum = now[i] + now[i+1]
        if sum < 10 :
            next.append(sum)
        else :
            next.append( int(str(sum)[1]) )
    if len(next) <= 2:
        break
    now = next[:]
    

print(int(''.join(list(map(str,next)))),"%",sep="")