#! python3
# tablePrinter.py - takes a list of lists of strings and displays it in
#                   a well-organized table with each column
#                   right-justified.
# Adam Pellot


# Prints table.
def printTable(lists):
    colWidths = [0] * len(tableData)
    for x in range(len(lists)):
        for y in range(len(lists[0])):
            if len(lists[x][y]) > colWidths[x]:
                colWidths[x] = len(lists[x][y])
    for y in range(len(lists[0])):
        for x in range(len(lists)):
            print(lists[x][y].rjust(colWidths[x]), end=' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
