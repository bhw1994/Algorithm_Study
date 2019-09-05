'''
1. 두팀으로 나눈다.
2. 능력치를 구한다.
3. 비교한다.
'''

import itertools



N = int(input())

stats = []
for i in range(N):
    stats.append( list(map(int,input().split())) )

members = set(range(N))

combinations = itertools.combinations(members,N // 2)

def calcStat(members):
    stat = 0
    combinations = itertools.combinations(members,2)
    for combination in combinations :
        stat += stats[combination[0]][combination[1]]
        stat += stats[combination[1]][combination[0]]
    return stat



minDx = None
for combination in combinations :
    team1 = set(combination)
    team2 = members - team1

    team1Stat = calcStat(team1)
    team2Stat = calcStat(team2)

    dx = abs(team1Stat - team2Stat)
    if minDx == None :
        minDx = dx
    else :
        minDx = min(minDx,dx)

print(minDx)







