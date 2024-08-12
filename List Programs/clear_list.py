#using clear() function

GEEK=[3,4,5,6]
print("GEEK before clear:",GEEK)

GEEK.clear()
print("GEEK after clear:",GEEK)

#clear a list by reinitializing the list

list=[1,2,3]
print("List before deleting is:",list)

list=[]
print("List after deleting is",list)

#clearing a List using del

list=[1,2,3]
print(list)
del list[:]
print(list)

#pop() method

list=[1,2,3,4,5]
print(list)
while len(list)!=0:
    list.pop()
print(list)

