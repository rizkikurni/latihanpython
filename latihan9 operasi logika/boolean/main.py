# operasi logikan atau boolean
# not, or, and, xor(^)

print('======not======')
a = False
c= not a
print('data a =', a)
print('data c =', c)

print('======or=======')
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)
a = False
b = True
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)

print('======and=======')
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

print('======xor=======')
a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)
