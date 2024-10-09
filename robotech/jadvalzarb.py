#print("A", "B", "C", sep=" ", end=" ")
#print("D", "E", "F")
n = int(input("numbers of rows: "))
m = int(input("numbers of columns: "))
for i in range(1, n+1):
    print()
    for j in range(1, m+1):
        print(j*i, end=" ")
        
    