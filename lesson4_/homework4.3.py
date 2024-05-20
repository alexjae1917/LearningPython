
ex1 = [0, 1, 0, 12, 3]
ex2 = [0]
ex3 = [1, 0, 13, 0, 0, 0, 5]
ex4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]

ex = ex4

for i in range(0,len(ex)):
    if ex[i] == 0:
         ex.append(ex.pop(i))

print(ex)
