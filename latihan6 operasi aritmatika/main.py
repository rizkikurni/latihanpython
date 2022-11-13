# operasi ada +, -, *, /, **(pangkat), %(modulus: sisa bagi), // (floor division: pembagian dibulatkan
a = 16
b = 3

hasil = a + b - a * b / a **b
print("hasil :" ,hasil)

hasilmodulus = a % b
hasilfloor = a // b

print("hasil modulus:" ,hasilmodulus)
print("hasil floor:" ,hasilfloor)