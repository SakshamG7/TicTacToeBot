# Author: Saksham Goel
# Version: 2024-03-13-r1
# Email: mail@sakshamg.com

board = [[None,None,None],
         [None,None,None],
         [None,None,None]]

def getScore(b: list):
    if (b[0][0] == b[1][1] == b[2, 2]) or (b[0][2] == b[1][1] == b[2, 0]):
        if b[1][1]:
            return 1
        else:
            return -1

    full = True

    for i in range(3):
        if (b[i][0] == b[i][1] == b[i][2]) or (b[0][i] == b[1][i] == b[2][i]):
            if b[i][0] or b[0][i]:
                return 1
            else:
                return -1
        if full:
            for j in range(3):
                if b[i][j] is None:
                    full = False
                    break
    if full:
        return 0
    else:
        return False

def getMove(b, highScore, move):
    if highScore is not False:
        return highScore
    
    moves = []
    
    for i in range(3):
        for j in range(3):
            if b[i][j] is None:
                moves.append((i, j))
    
    score = 2
    for p in moves:
        tempB = b.copy()
        tempB[p[0]][p[1]] = True
        s = getScore(tempB)
        if s is False or s == 1:
            continue
        for e in moves:
            if p == e:
                continue
            tempB[e[0]][e[1]] = False
            s = getScore(tempB)
            if s is False or s == 1:
                continue
            elif s < score:
                score = s
    if score == -1:
        return move
                
        
print("You are X. Play by typing cordinates, `0, 0` is the top left corner, `2, 2` is the bottom right.")
while True:
    pX, pY = map(int, input("> ").split(", "))
    board[pY][pX] = True
    change = getScore(board.copy())
    if change is False:
        eY, eX = getMove(board.copy(), change)
        board[eY][eX] = False
    else:
        print(change)
        break
