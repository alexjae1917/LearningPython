import keyword
import string


def check(name):
    cnta = 0
    cnt_ = 0



    if name[0].isdigit():
        return False


    if name in keyword.kwlist:
        return False

    for i in name:
        if i =='_':cnt_+=1

        if i in string.punctuation and i != '_' or i == ' ':
            return False

        if i.isalpha():
            cnta += 1
            if i == i.upper(): return False

    if cnta == 0 and cnt_>1: return False

    return True


m = 0
while m < 15:
    name = input('Enter new string: ')
    print(check(name))
    m += 1


