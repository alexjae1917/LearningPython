import keyword
import string



def check(name):
    cnt=0

    if not name[0].isalpha() and name[0] !="_":
        return False
    else:cnt=1

    if name in keyword.kwlist:
        return False

    for i in name[1:-1]:

        if i.isalpha():
            cnt += 1
            if i != i.upper():return False

        if i in string.punctuation and i != '_' or i ==' ':
            return False

    if cnt == 0: return False

    return True
m=0
while m<15:
    name = input('Enter new string: ')
    print(check(name))
    m+=1



#print('_' in string.punctuation)

