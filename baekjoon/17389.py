N = int(input())
arr = input()

score = 0
bonus = 0
for i,c in enumerate(arr):
    if c == "O":
        score += i+1 + bonus
        bonus += 1
    else :
        bonus = 0



print(score)