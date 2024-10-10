from sys import argv

debug = 0
if len(argv) > 2:
    print("Too many arguments.")
    exit()
else:
    try:
        if argv[1] == '-db':
            debug = 1
    except:
        debug = 0

def printKu(sudoku):
    display = ''
    for line in sudoku:
        for item in list(line):
            display += (item + ' ')
        display += '\n'
    return display

def getGrid():
    grid = []
    for i in range(9):
        line = input("Please input line " + str(i + 1) + ": ")
        while line:
            if line.isdigit() and (len(line) == 9):
                grid.append(line)
                line = ''
            else:
                line = input("Please input a line of 9 digits: ")
    return grid

def valGrid(grid):
    if debug:
        print("Checking rows:\n", grid)
    if not valUnq(grid):
        print("Rows not unique")
        return False
    print("Rows unique!")

#get columns
    columns = []
    for i in range(len(grid)):
        temp = ''
        col = ''
        
        for row in grid:
            col += row[i]
        
        if debug:
            print(col)
        columns.append(col)
    
    if debug:
        print("Checking columns:\n", columns)
    if not valUnq(columns):
        print("Columns not unique")
        return False
    print("Columns unique!")

#get subsquares
    subsquares = []
    for i in range(0, 9, 3):
        sqr = ''
        counter = 0
        for row in grid:
            sqr += row[i:i+3]
            counter += 1
            if counter == 3:
                subsquares.append(sqr)
                sqr = ''
                counter = 0
    if debug:
        print("checking subsquares:\n", subsquares)
    if not valUnq(subsquares):
        print("Subsquares not unique")
        return False
    print("Subsquares unique!")

    return True

def valUnq(digList):
    for entry in digList:
        myList = sorted(list(entry))
        for i in range(len(entry)):
            if i > 0:
                if myList[i] == myList[i-1]:
                    return False
    return True


myGrid = getGrid()

print("Your sudoku: \n")
print(printKu(myGrid))

if valGrid(myGrid):
    print("Yes")
else:
    print("No")
