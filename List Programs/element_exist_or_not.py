#using "in" statement

lst=[3,4,98,6,6,43,245.324]
i=687
if i in lst:
    print("exist")
else:
    print("Not exist")

#using loop

list=[4,5,6,7,8]
for i in list:
    if(i==5):
        print("exist")

#using count() function

list=[43,455,23424,4352,13412,3134]

list_test=list.count(4855)

if list_test>0:
    print("yes")
else:
    print("No") #test