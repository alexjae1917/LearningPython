ex1 = [12, 3, 4, 10]
ex2 = [1]
ex3 = []
ex4 = [12, 3, 4, 10, 8]
ex = ex1.copy()

if len(ex) <= 1:
    print(ex1, ' =>', ex)
else:
    ex.insert(0, ex.pop())
    print(ex1, ' =>', ex)
