tpl = (1,2,3,4,5,6,7,8,9,10,4)

lst = list(tpl)

print(tpl)
ele = int(input("enter an element to remove"))
for item in lst:
    if item == ele:
        lst.remove(item)
        #break => to remove only one element
tpl=tuple(lst)

print(tpl)
