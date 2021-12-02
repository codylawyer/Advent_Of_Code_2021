f = open('input.txt')
line = f.readline().strip()

distance = 0
depth = 0
while line:
    line = line.split(' ')
    direction = line[0]
    amount = int(line[1])
    if direction=='forward':
        distance += amount
    if direction=='up':
        depth -= amount
    if direction=='down':
        depth += amount

    line = f.readline().strip()

print(distance*depth)
