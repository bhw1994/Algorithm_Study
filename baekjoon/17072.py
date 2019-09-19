N , M  = map(int,input().split())

result = ""
def calc(r,g,b):
    return 2126*r + 7152*g + 722*b

def transform(value):
    if 0 <= value and value < 510000 :
        return "#"
    elif 510000 <= value and value < 1020000 :
        return "o"
    elif 1020000 <= value and value < 1530000 :
        return "+"
    elif 1530000 <= value and value < 2040000 :
        return "-"
    elif 2040000 <= value :
        return "."
    else :
        return -1
for i in range(N):
    raw = list(map(int , input().split()))

    for i in map(lambda x : x*3,range(M)):
        value = calc(raw[i],raw[i+1],raw[i+2])
        c = transform(value)
        
        result+=c
        if (i // 3) % M == M - 1 :
            result+= "\n"
        

print(result)