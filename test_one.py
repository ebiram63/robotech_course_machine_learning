rows_columns = input()
num_bombs = input()
m = int(rows_columns.split(" ")[0])
n = int(rows_columns.split(" ")[1])
print([[0 for _ in range(n)] for _ in range(m)])