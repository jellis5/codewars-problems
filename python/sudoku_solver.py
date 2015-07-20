#From http://www.codewars.com/kata/5296bc77afba8baa690002d7

#Description:

#Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

#The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

def testIndexes(puzzle, iRow, indexAmnts, numsLeft):
    for index in indexAmnts:
        if indexAmnts[index] == 1:
            for num in numsLeft:
                for indexNum in numsLeft[num]:
                    if indexNum == index:
                        puzzle[iRow][index] = num
                        return True

def sudoku(puzzle):
    rounds = 0
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                rounds += 1
    while rounds > 0:
        for iRow in range(9):
            filledNums, emptyIndexes = [], []
            for iColumn in range(9):
                if puzzle[iRow][iColumn] != 0:
                    filledNums.append(puzzle[iRow][iColumn])
                else:
                    emptyIndexes.append(iColumn)
            numsLeft = {num: [] for num in set(range(1, 10)) ^ set(filledNums)}
            indexAmnts = {}
            for i in emptyIndexes:
                indexAmnts[i] = 0
                for num in numsLeft:
                    for r in range(9):
                        if r == iRow: continue
                        if puzzle[r][i] == num:
                            break
                    else:
                        # see if 3x3 boxes will allow placement
                        inBlock = False
                        rRangeStart, rRangeEnd = 0, 3
                        cRangeStart, cRangeEnd = 0, 3
                        if iRow > 2 and iRow < 6:
                            rRangeStart, rRangeEnd = 3, 6
                        elif iRow > 5:
                            rRangeStart, rRangeEnd = 6, 9
                        if i > 2 and i < 6:
                            cRangeStart, cRangeEnd = 3, 6
                        elif i > 5:
                            cRangeStart, cRangeEnd = 6, 9
                        for r in range(rRangeStart, rRangeEnd):
                            for c in range(cRangeStart, cRangeEnd):
                                if puzzle[r][c] == num:
                                    inBlock = True
                        if not inBlock:
                            numsLeft[num].append(i)
                            indexAmnts[i] += 1
            if testIndexes(puzzle, iRow, indexAmnts, numsLeft):
                break
                                
        rounds -= 1
    return puzzle
