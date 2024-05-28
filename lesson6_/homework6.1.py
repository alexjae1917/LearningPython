import string

letters = input('Enter range: ')


first = string.ascii_letters.index(letters[0])

second = string.ascii_letters.index(letters[2])+1
print(string.ascii_letters[first:second])
