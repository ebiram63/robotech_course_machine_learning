stack = ["first", "second", "third"]
print(stack)
stack.append('fourth')
stack.append('fifth')
print(stack)
stack.pop()
print(stack)

queue = ["ali", "mohammad"]
queue.append("reza")
queue.append("amir")
print(queue)
print(queue[0]) 
queue.pop(0)
print(queue)

myList = [0, 1, 2, 3]
for i, it in enumerate(myList):
    print("the {0}th object in myList is {1}!".format(i+1, it))
    

listA = [1, 2, 3, 4]
listB = ['a', 'b', 'c', 'd']
listC = ['I', 'II', 'III', 'IV']
for a, b, c in zip(listA, listB, listC):
    print("{0}th alphabet or {1} in greece is {2}".format(a, c, b))


ls = [2, 4, 3, 1]
print(ls)
print(sorted(ls))



ls = ['a', 'bcd', 'salam', 'hello']
print(reversed(ls))
for i in reversed(ls):
    print(i, end=' ')
print("=======")

def f(x):
    return True if x%2 == 0 else False
ls = [1, 2, 4, 3, 6, 4]
print(filter(f, ls))
for x in filter(f, ls):
    print(x, end=' ')
print("=======")


def f(x):
    return int(x)
ls = [2, '4', False, 3.14]
print(map(f, ls))
for x in map(f, ls):
    print(x, end=' ')
print("=======")


number = map(int, input().split())
print(sum(number))



ls = [1, 2, 3, 4]
sum(ls)