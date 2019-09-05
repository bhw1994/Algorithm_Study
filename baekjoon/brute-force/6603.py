import itertools
while True:

    row = input()
    if row == "0":
        break


    arr = list(map(int,row.split()))
    N = arr[0]
    numbers = arr[1:]
    
    combinations = itertools.combinations(numbers,6)
    for c in combinations:
        l = list(map(str,c))
        print(' '.join(l))


    print("")
