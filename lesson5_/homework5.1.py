import keyword
import string


def check(name: str):
    cntalpha = 0
    cntline = 0

    if name[0].isdigit():
        return False

    if name in keyword.kwlist:
        return False

    for i in name:
        if i == '_':
            cntline += 1

        if i in string.punctuation and i != '_' or i == ' ':
            return False

        if i.isalpha():
            cntalpha += 1
            if i.isupper():
                return False

    if cntalpha == 0 and cntline > 1:
        return False

    return True


m = 0
while m < 15:
    name = input('Enter new string: ')
    print(check(name))
    m += 1
