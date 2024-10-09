import time 


n = int(input("add ra vared konid: "))
answer_1  = 0
answer_2  = 0
answer_3  = 0

"""
#solution1
for a in range(1, n+1):
    for b in range(a, n+1):
        for c in range(b, n+1):
            if a+b> c and a+c > b and b+c > a and a+b+c == n:
                #print(a,b,c)
                answer_1 += 1
print(answer_1)
"""

start = time.time()
#solution2 
for a in range(1, n+1):
    for b in range(a, n+1):
        for c in range(b, n+1):
            if a+b > c and a+b+c == n:
                #print(a,b,c)
                answer_2 += 1
#print(answer_2)
end = time.time()
print("solution2: ",end - start)

start = time.time()
#solution3 
for a in range(1, n+1):
    for b in range(a, n+1):
        c = n -(a+b)
        if a+b > c and c >= b:
            #print(a,b,c)
            answer_3 += 1
#print(answer_3)
end = time.time()
print("solution3: ",end - start)