exm1 = [1,3,5]
exm2 = [0]
exm3= [6]
exm4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]

exm = exm1
sum = 0

for i in exm[::2]:
     sum += i

print(sum * exm[-1])

