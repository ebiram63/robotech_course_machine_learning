mylist = ['1','2','a','w']
print(mylist)

zeros = [0] * 100
print(zeros)

myList = [10, 20, 30 ,40 ,50 ,60]
print(myList)
print(myList[:])
print(myList[1])
print(myList[1:])
print(myList[:1])
print(myList[1:0])
print(myList[0:2])

print(list(range(10)))
print(list('salam'))

mylist = [10]
mylist.append(20)
print(mylist)

mylist.extend([30, 40, 50])
print(mylist)

#list.insert(i, x)
mylist = [1, 2 ]
mylist.insert(1, 4)
print(mylist)

#list.remove(x)
mylist = [1, 2, 3, 4]
mylist.remove(3)
print(mylist)

#list.pop(i)
mylist = [10, 20, 30]
mylist.pop(0)
print(mylist)

#list.clear()
mylist = [1, 2, 3]
mylist.clear()
print(mylist)

#list.index(x, start, end)
myList = ["amir", "ali", "amir", "ali"]
print(myList.index('ali'))
print(myList.index('ali', 2, 4))
#print(myList.index('ali', 0, 1))

#list.count(x)
myList = ["amir", "ali", "amir", "ali"]
print(myList.count('ali'))


#list.sort(key=None, reverse=False)
companies = ['apple', 'samsung', 'xiaomi', 'sony', 'nokia']
print(companies)
companies.sort()
print(companies)
def getLength(a):
    return len(a)
    
companies.sort(key=getLength)
print(companies)


#list.reverse()
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

#c.join(list)
names = ['ali', 'mohamadreza', 'mahdi']
print('-'.join(names))

#list.copy() list[:]
numbers = [1, 2, 3, 4, 5]
print(numbers.copy())
print(numbers[:])