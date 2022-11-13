a = 3
b = 5

# bitwise  or
c = a | b 
print("\n========or========")
print('nilai : ', a,', binary :', format(a, '08b'))
print('nilai : ', b,', binary :', format(b, '08b'))
print('-----------------------')
print('nilai : ', c,', binary :', format(c, '08b'))
# bitwise  and
c = a & b 
print("\n========and========")
print('nilai : ', a,', binary :', format(a, '08b'))
print('nilai : ', b,', binary :', format(b, '08b'))
print('-----------------------')
print('nilai : ', c,', binary :', format(c, '08b'))
# bitwise  xor
c = a ^ b 
print("\n========xor========")
print('nilai : ', a,', binary :', format(a, '08b'))
print('nilai : ', b,', binary :', format(b, '08b'))
print('-----------------------')
print('nilai : ', c,', binary :', format(c, '08b'))
# bitwise  not
c = ~a
print("\n========not========")
print('nilai : ', a,', binary :', format(a, '08b'))
print('-----------------------')
print('nilai : ', c,', binary :', format(c, '08b'))

#shift mengeser
# >> geser kanan
# << geser kiri

c = a << 2
print("\n========<<========")
print('nilai : ', a,', binary :', format(a, '08b'))
print('-----------------------')
print('nilai : ', c,', binary :', format(c, '08b'))
