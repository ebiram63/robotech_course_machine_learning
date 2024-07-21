rows_columns = input()
num_bombs = input()
bombs_placed_position = []
#raw
n = int(rows_columns.split(" ")[0])
#column
m = int(rows_columns.split(" ")[1])
for i in range(int(num_bombs)):
    bombs_placed_position.append(input())

def generate_board(m, n, num_bombs):
    board = [[0 for _ in range(m)] for _ in range(n)]
    
    bombs_placed = 0
    k = 0
    while bombs_placed < int(num_bombs):
        if k <= int(num_bombs):
            #print(bombs_placed_position)
            row = int(bombs_placed_position[k].split(" ")[0]) - 1
            col = int(bombs_placed_position[k].split(" ")[1]) - 1
            #print("row" , row, "column", col)
            k += 1
        if board[row][col] != '*':
            board[row][col] = '*'
            bombs_placed += 1
    
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == '*':
                continue
            for x in range(max(0, i - 1), min(m, i + 2)):
                for y in range(max(0, j - 1), min(n, j + 2)):
                    if board[x- 1][y] == '*':
                        board[i][j] += 1
    
    return board

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

board = generate_board(m, n, num_bombs)
print_board(board)