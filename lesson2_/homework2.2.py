number = int(input("Enter 5digit number ", ))
n5 = number % 10
n4 = (number % 100) // 10
n3 = (number % 1000) // 100
n2 = (number % 10000) // 1000
n1 = (number % 100000) // 10000
rev = (((n5*10 + n4) * 10 + n3) * 10 + n2) * 10 + n1
print(rev)
