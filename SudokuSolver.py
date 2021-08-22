#Made by Piotr Łądkowski
def sudoku_empty(sudoku):
    for row in sudoku:
        for element in row:
            if type(element) is not int:
                return False
    return True

def solve_sudoku(sudoku):
    initPossibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sudoku = sudoku[:]
    solved = False

    while not solved:

        for row in range( len(sudoku) ):

            for element in range( len(sudoku[row]) ):

                if type(sudoku[row][element]) is not int:

                    possibles = initPossibles[:]

                    #check in grid
                    for rowCount in range(row - (row % 3), row - (row % 3) + 3):
                        for elemCount in range(element-(element%3), element-(element%3)+3):
                            if sudoku[rowCount][elemCount] in possibles:
                                possibles.remove(sudoku[rowCount][elemCount])

                    #check in row
                    for elem in sudoku[row]:
                        if elem in possibles:
                            possibles.remove(elem)

                    #check in column
                    for checkRow in sudoku:
                        if checkRow[element] in possibles:
                            possibles.remove(checkRow[element])


                    if len(possibles) is 1:
                        possibles = possibles[0]

                    sudoku[row][element] = possibles


        solved = sudoku_empty(sudoku)

    return sudoku

def print_sudoku(sudoku):
    for row in sudoku:
        printRow = ""
        for elem in row:
            printRow += str(elem)
            if elem is "" or '':
                printRow += "[]"
            printRow += " "
        print(printRow)
