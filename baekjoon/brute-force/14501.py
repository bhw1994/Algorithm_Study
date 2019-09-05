'''
45
'''

dayNumber = int(input())
calendar = []
for i in range(dayNumber):
    calendar.append( list(map(int,input().split())) )

maxIncome = 0
def recursive(day,expect,income):
    if day >= len(calendar) :
        if len(calendar)  == day  :
            income+= expect
        global maxIncome
        maxIncome = max(maxIncome , income)
        return

    
    income += expect

    # accept
    period = calendar[day][0]
    expect = calendar[day][1]
    if period == 1 :
        recursive(day + 1,0 ,income+expect)
    else:
        recursive(day + period ,expect,income)

    # pass
    recursive(day + 1 , 0 , income)

recursive(0 ,0 ,0)
print(maxIncome)
