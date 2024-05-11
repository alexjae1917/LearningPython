ex1 = [1, 2, 3, 4, 5, 6]
ex2 = [1, 2, 3]
ex3 = [1, 2, 3, 4, 5]
ex4 = [1]
ex5 = []
def division(lst):
    res =[]
    i = int(len(lst)/2+1)
    j = int(len(lst)/2)



    if len(lst) == 1:
        res.append(lst[0])
        res.append([])
    elif len(lst) % 2 == 0:
        res.append(lst[0:j])
        res.append(lst[j:])
    elif len(lst) % 2 != 0:
        res.append(lst[:i])
        res.append(lst[i:])
    else:
        res =[[],[]]
    return res

print( division(ex5) )