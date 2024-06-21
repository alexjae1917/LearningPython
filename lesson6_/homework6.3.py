
number = '999' #input("Enter some number: ")
multi = 10
while multi > 9:
    multi = 1
    for i in number:
        multi *= int(i)

    number = str(multi)

print(multi)

