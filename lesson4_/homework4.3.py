import random

lst =[]
for i in range(0,random.randint(3,10)):
    lst.append(random.randint(0,10))
new_lst=[lst[0],lst[2],lst[-2]]
print(lst,'->->',new_lst)