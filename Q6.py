tpl = (1,2,3,4,5,6,7,8,9,10,4)

lst = list(tpl)

print(tpl)
ele = int(input("element to remove"))
nele = int(input("new element"))
for item in lst:
    if item == ele:
        new_lst = lst[:(lst.index(item))] #begin to changing ele - 1 postion 
        new_lst.append(nele) # updated ele
        new_lst = new_lst + lst[(lst.index(item)+1):] # after updated ele to end 

tpl=tuple(lst)
new_tpl = tuple(new_lst)

print(tpl)
print(new_tpl)
