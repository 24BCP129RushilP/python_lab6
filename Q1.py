name =[("alone","abc","het"),"visha",("denish",),"vanshika",("vikas",)]
boys_count=0
girls_count=0
for ele in name:
    if isinstance(ele,tuple):
        tpl=ele
        l=list(tpl) 
        for item in l:
            boys_count=boys_count+1
    else:
        girls_count = girls_count+1
print(boys_count,girls_count)
        
