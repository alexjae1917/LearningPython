from rectangle import Rectangle


a = Rectangle(8,4)
b = Rectangle(25,7)
print(f'First {a}')
print(f'Second {b}')
print(f'Sum {a+b}')
print(f'10x First {a*10}')
assert b > a, 'Test3'
assert a < b, 'Test4'
assert not a == b, 'Test5'
assert a != b, 'Test6'