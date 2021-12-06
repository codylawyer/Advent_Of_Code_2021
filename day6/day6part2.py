f = open('testinput.txt')
lanternfish = [int(x) for x in f.readline().strip().split(',')]

daysToSimulate = 256
for day in range(1,daysToSimulate+1):
    lanternfishToAppend = 0
    numLanternfish = len(lanternfish)
    for idx in range(numLanternfish):
        lanternfish[idx] -= 1
        if lanternfish[idx] == -1:
            lanternfishToAppend += 1
            lanternfish[idx] = 6
            lanternfish.append(8)

print(len(lanternfish))
