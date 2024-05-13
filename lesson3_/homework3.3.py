ex1 = [1, 2, 3, 4, 5, 6]
ex2 = [1, 2, 3]
ex3 = [1, 2, 3, 4, 5]
ex4 = [1]
ex5 = []

ex = ex3

res = []
j = len(ex) // 2

if len(ex) == 1:
    res.append(ex[0])
    res.append([])

elif len(ex) % 2 == 0:
    res.append(ex[:j])
    res.append(ex[j:])

elif len(ex) % 2 != 0:
    res.append(ex[:j + 1])
    res.append(ex[j + 1:])

else:
    res = [[], []]

print(res)
