#sum of elements in list

total=0
list=[11,21,31,4,1,432]
for ele in range(0,len(list)):
    total=total+list[ele]
print(total)

#using while() loop

total=0
ele=0

list=[32,3,4,2,34,12]
while(ele<len(list)):
    total=total+list[ele]
    ele+=1

print("Sum of all elements in list",total)

#recursive way

list=[1,2,3,4,5]

def sumOfList(list,size):
    if(size==0):
        return 0
    else:
        return list[size-1]+sumOfList(list,size-1)

total=sumOfList(list,len(list))
print("Sum of all elements in given list:",total)   