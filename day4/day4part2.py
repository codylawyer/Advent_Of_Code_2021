def checkBoard(board):
    cols = [[],[],[],[],[]]
    for row in board:
        if sum(row) == -5:
            return True
        for idx,num in enumerate(row):
            cols[idx].append(num)
    for col in cols:
        if sum(col) == -5:
            return True
    return False

def markBoard(board,draw):
    for i,row in enumerate(board):
        for j,num in enumerate(row):
            if num==draw:
                board[i][j]=-1
    return board 

f = open('input.txt')
line = f.readline()

drawing = [int(x) for x in line.strip().split(',')]

boards = []
line = f.readline()
line = f.readline()
currentBoard = []
while line:
    line = line.strip()
    if line == '':
        boards.append(currentBoard)
        currentBoard = []
    else:
        row = []
        line = line.split(' ')
        for num in line:
            if num != '':
                row.append(int(num))
        currentBoard.append(row)
    line = f.readline()

boards.append(currentBoard)
for draw in drawing:
    for idx,board in enumerate(boards):
        boards[idx] = markBoard(board,draw)
    winners = []
    for idx,board in enumerate(boards):
        winner = checkBoard(board)
        if winner:
            winners.append(board)
            if len(boards) == 1:
                boardSum = 0
                for row in board:
                    for num in row:
                        if num != -1:
                            boardSum += num
                print(boardSum)
                print(draw)
                print(boardSum*draw)
    for winner in winners:
        boards.remove(winner)

