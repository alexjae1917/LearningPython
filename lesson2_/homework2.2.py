number = int(input("Enter 5digit number ", ))
rev = number % 10
rev = rev * 10 + (number % 100) // 10
rev = rev * 10 + (number % 1000) // 100
rev = rev * 10 + (number % 10000) // 1000
rev = rev * 10 + (number % 100000) // 10000
print(rev)