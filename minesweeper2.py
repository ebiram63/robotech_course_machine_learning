rows_columns = input()
num_bombs = input()
bombs_placed_position = []
#raw
n = int(rows_columns.split(" ")[0])
#column
m = int(rows_columns.split(" ")[1])
for i in range(int(num_bombs)):
    bombs_placed_position.append(input())
    
map = []
for x in range(n):
    map.append([])
    for y in range(m):
         map[x].append(0)

bombs_placed = 0
while bombs_placed < int(num_bombs):
    if map[n][m] != '*':
            map[n][m] = '*'
            bombs_placed += 1
for i in range(n - 1):
        for j in range(m - 1):
            if map[i][j] == '*':
                continue
            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    if map[x- 1][y] == '*':
                        map[i][j] += 1
         
print(map)