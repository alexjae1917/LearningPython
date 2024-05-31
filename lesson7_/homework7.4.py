def common_elements() -> set:
    lst3 = []
    lst5 = []
    for i in range(0, 100, 3):
        lst3.append(i)
    for i in range(0, 100, 5):
        lst5.append(i)
    return set(lst3) & set(lst5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
