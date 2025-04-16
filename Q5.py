lst = ["name",(),"rollno",("abc"),(),1]
tpl=()
for item in lst:
    if item == tpl:
        lst.remove(item)

print(lst)
