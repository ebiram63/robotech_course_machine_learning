rows = 5

def fact(n):
    f = 1 
    while True:
        if n == 0:
            break
        f *= n 
        n = n - 1
        
    return f
#print(fact(5))

def combination(n, k):
    return int(fact(n)/(fact(k)*fact(n-k)))

print(combination(10, 2))

def khayam(rows):
    for i in range(0, rows):
        print()
        for j in range(0, i+1):
            print(combination(i,j) , end=" ")
            
khayam(7)