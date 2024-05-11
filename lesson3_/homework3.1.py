ex1 = [12, 3, 4, 10]
ex2 = [1]
ex3 = []
ex4 = [12, 3, 4, 10, 8]


# ex1.insert(0,ex1.pop())
# ex2.insert(0,ex1.pop())
# ex2.insert(0,ex1.pop())
# ex4.insert(0,ex1.pop())
# print(ex1 ,' => ',)

def change_last(lst):
    if len(lst) <= 1:
        return lst
    lst.insert(0, lst.pop())
    return lst


print(change_last(ex1))

print(change_last(ex2))
print(change_last(ex3))
print(change_last(ex4))
