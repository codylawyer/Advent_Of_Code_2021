f = open('input.txt')
lanternfish = [int(x) for x in f.readline().strip().split(',')]

daysToSimulate = 80
for day in range(1,daysToSimulate+1):
    lanternfishToAppend = 0
    for idx in range(len(lanternfish)):
        lanternfish[idx] -= 1
        if lanternfish[idx] == -1:
            lanternfishToAppend += 1
            lanternfish[idx] = 6
    for idx in range(lanternfishToAppend):
        lanternfish.append(8)

print(len(lanternfish))
