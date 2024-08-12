#1. Interchange 1st and last element

def swaplist(newList):
    size=len(newList)

    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp

    return newList

newList=[4,5,6,7,8]
print(swaplist(newList))

#2.

def swaplist(newList):
    newList[0],newList[-1]=newList[-1],newList[0]
    return newList
newList=[4,5,6,7,8]
print(swaplist(newList))
