# had to get hint on this one because was doing naive way (see day 1)
f = open('input.txt')
lanternfish = [int(x) for x in f.readline().strip().split(',')]

numPerDay = [0] * 9
for fish in lanternfish:
    numPerDay[fish] += 1

daysToSimulate = 256
for day in range(1,daysToSimulate+1):
    numZero = numPerDay.pop(0)
    numPerDay.append(numZero)
    numPerDay[-3] += numZero

print(sum(numPerDay))
