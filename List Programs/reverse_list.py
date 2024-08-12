#Reverse list using slicing technique

def reverse(lst):
    new_list=lst[::-1]
    return new_list
lst=[10,23,45,34,54]
print(reverse(lst))

#reverse list using the reversed() and reverse() built-in function

lst=[4,5,6,7,8]
lst.reverse()
print(lst)
print(list(reversed(lst)))