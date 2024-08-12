def swappositions(list,pos1,pos2):

    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

list=[45,346,34,2,543]
pos1,pos2=0,2

print(swappositions(list,pos1,pos2))