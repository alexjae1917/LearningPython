ex1 = [0, 1, 0, 12, 3]
ex2 = [0]
ex3 = [1, 0, 13, 0, 0, 0, 5]
ex4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]

ex = ex4


def zero(n):
    return n == 0


ex.sort(key=zero)
print(ex)

# ex.reverse()
# res = []
# for i in ex:
#     if i == 0:
#         res.append(i)
#     else:
#         res.insert(0,i)
#
#
#
# print(res)
