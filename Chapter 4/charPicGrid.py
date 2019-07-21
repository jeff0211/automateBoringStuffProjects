grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for x in range(len(grid)):
        if x < (len(grid)-1):
            print(grid[x][i], end='')
        else:
            print(grid[x][i])
            
#USING WHILE LOOP
# count = 0
# while count < len(grid[0]):
#     for i in range(len(grid)):
#         print(grid[i][count], end='')
#     print('\n')
#     count += 1
