#! python3
# characterPictureGrid.py - Prints a grid passed as a 2D list.
# Adam Pellot


# Prints grid.
def characterPictureGrid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print('')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
characterPictureGrid(grid)
