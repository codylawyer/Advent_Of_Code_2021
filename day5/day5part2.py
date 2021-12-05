f = open('input.txt')
line = f.readline().strip()

lineSegments = []
while line:
    line = line.split(' -> ')
    lineSegment = []
    for pos in line:
        lineSegment.append([int(x) for x in pos.split(',')])
    lineSegments.append(lineSegment)
    line = f.readline().strip()

dangerousPositions = {}
for lineSegment in lineSegments:
    x1 = lineSegment[0][0] 
    y1 = lineSegment[0][1] 
    x2 = lineSegment[1][0] 
    y2 = lineSegment[1][1] 
    if x1 == x2:
        x = x1
        if y2 > y1:
            for y in range(y1,y2+1):
                if (x,y) in dangerousPositions:
                    dangerousPositions[(x,y)] = dangerousPositions[(x,y)] + 1
                else:
                    dangerousPositions[(x,y)] = 1
        else:
            for y in range(y1,y2-1,-1):
                if (x,y) in dangerousPositions:
                    dangerousPositions[(x,y)] = dangerousPositions[(x,y)] + 1
                else:
                    dangerousPositions[(x,y)] = 1
    elif y1 == y2:
        y = y1
        if x2 > x1:
            for x in range(x1,x2+1):
                if (x,y) in dangerousPositions:
                    dangerousPositions[(x,y)] = dangerousPositions[(x,y)] + 1
                else:
                    dangerousPositions[(x,y)] = 1
        else:
            for x in range(x1,x2-1,-1):
                if (x,y) in dangerousPositions:
                    dangerousPositions[(x,y)] = dangerousPositions[(x,y)] + 1
                else:
                    dangerousPositions[(x,y)] = 1
    else:
        dist = abs(y2-y1)
        dy = (y2-y1)/dist
        dx = (x2-x1)/dist
        for step in range(0,dist+1):
            x = int(x1+step*dx)
            y = int(y1+step*dy)
            if (x,y) in dangerousPositions:
                dangerousPositions[(x,y)] = dangerousPositions[(x,y)] + 1
            else:
                dangerousPositions[(x,y)] = 1


print(sum([x>1 for x in dangerousPositions.values()]))
