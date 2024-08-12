#1. Length function

# list=[2,3,4,5,6]
# a=len(list)
# print(a)

# #2. using naive method

# list=[1,2,3,4]
# print("The list is:",str(list))

# counter=0
# for i in list:
#     counter=counter+1
# print("Length of list using naive method is:",str(counter))

#3. using length_hint() function

from operator import length_hint

list=[2,3,4,5,6]
print("The list is:",list)

list_len=len(list)
list_len_hint=length_hint(list)

print(list_len)
print(list_len_hint)