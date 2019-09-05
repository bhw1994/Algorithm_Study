N = int(input())
result = 0
for i in range(1,N+1):
    s = str(i)
    l = list(map(int,list(s)))

    before = None
    done = True
    for j in range(len(l)-1):
        if before == None :
            before = l[j] - l[j+1]
            continue
        
        dx = l[j] - l[j+1]
        if dx != before :
            done = False
            break
    
    if done == True:
        result += 1
print(result)
           

'''
99
'''