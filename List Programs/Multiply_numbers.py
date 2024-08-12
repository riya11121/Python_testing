#Multiply all numbers in the list using Traversal

def multiplyList(myList):
    result=1
    for x in myList:
        result=result*x
    return result
list1=[1,2,3]
list2=[1,2,3,2]
print(multiplyList(list1))
print(multiplyList(list2))

#using for loop

def multiplylist(list1):
    product=1

    for element in list1:
        product*=element

    return product
list1=[4,2,3,2]
result=multiplylist(list1)
print(result)