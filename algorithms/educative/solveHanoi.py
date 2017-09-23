
record = {
        "diskMoves": 0,
        "pegLog": []
        }

def initialPegBoard(n, peg):
    l = [[], [], []]
    start_peg = list(range(1, n + 1))
    start_peg.reverse()
    l[peg] = start_peg
    return l


def getSparePeg(fromPeg, toPeg):
    if fromPeg + toPeg == 3:
        return 0
    elif fromPeg + toPeg == 2:
        return 1
    else: 
        return 2

moves = 0

def print_moves_and_board(moves, pegBoard):
    print(str(moves) + ':', pegBoard)

def moveDisk(fromPeg, toPeg, pegBoard):
    global moves
    val = pegBoard[fromPeg].pop()
    pegBoard[toPeg].append(val)
    moves += 1
    print_moves_and_board(moves, pegBoard)
    return pegBoard

def solveHanoi(numDisks, fromPeg, toPeg, pegBoard):
    sparePeg = getSparePeg(fromPeg, toPeg)

    if numDisks >= 1:
        solveHanoi(numDisks - 1, fromPeg, sparePeg, pegBoard)
        moveDisk(fromPeg, toPeg, pegBoard)
        solveHanoi(numDisks - 1, sparePeg, toPeg, pegBoard)


if __name__ == '__main__':
    solveHanoi(2, 0, 1, initialPegBoard(2, 0))

    print()
    moves = 0
    solveHanoi(3, 0, 1, initialPegBoard(3, 0))

    print()
    moves = 0
    solveHanoi(4, 0, 1, initialPegBoard(4, 0))

    print()
    moves = 0
    solveHanoi(5, 0, 1, initialPegBoard(5, 0))

    print()
    moves = 0
    solveHanoi(6, 0, 1, initialPegBoard(6, 0))

