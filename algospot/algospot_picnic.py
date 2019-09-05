"""
expect :
1
3
4
"""
import itertools


def solution():
    n, m = map(int, input().split())
    relationsList = list(map(int, input().split()))
    relationSet = set()

    for i in map(lambda v: v * 2, range(m)):
        relationSet.add((min(relationsList[i], relationsList[i + 1]),max(relationsList[i], relationsList[i + 1])))

    students = list(range(n))
    result = 0
    def recursive(students):
        if len(students) == 0:
            nonlocal result
            result += 1
            return
        
        nonlocal relationSet
        for i in range(1,len(students)):
            first = students[0]
            other = students[i]
            pair = (first,other)
            if pair in relationSet :
                remained = students[1:]
                remained.remove(other)
                recursive(remained)


                
        
        
    recursive(students)
    print(result)
    return result


testCaseNumber = int(input())

for testCase in range(0, testCaseNumber):
    solution()

