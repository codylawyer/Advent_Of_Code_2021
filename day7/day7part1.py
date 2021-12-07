f = open('input.txt')
crabs = [int(x) for x in f.readline().strip().split(',')]
minFuel=99999999999
minPos =-1
for pos in range(0,max(crabs)+1):
    fuelUsed = sum([abs(x-pos) for x in crabs])
    if fuelUsed < minFuel:
        minFuel = fuelUsed
        minPos = pos

print(minFuel)
