f = open('input.txt')
crabs = [int(x) for x in f.readline().strip().split(',')]
minFuel=99999999999
minPos =-1
for pos in range(0,max(crabs)+1):
    fuelUsed = sum([sum([y for y in range(1,abs(x-pos)+1)]) for x in crabs])
    if fuelUsed < minFuel:
        minFuel = fuelUsed
        minPos = pos

print(minFuel)
