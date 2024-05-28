ex1 = [1, 2, 3, 4, 5, 6]
ex2 = [1, 2, 3]
ex3 = [1, 2, 3, 4, 5]
ex4 = [1]
ex5 = []

ex = ex4

res = []
j = len(ex) // 2

if len(ex) % 2 == 0:
    res.append(ex[:j])
    res.append(ex[j:])

else:
    res.append(ex[:j + 1])
    res.append(ex[j + 1:])

print(res)
