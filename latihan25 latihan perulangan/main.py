# latihan perulangan 

# membuat segitiga
from itertools import count


print("membuat segitiga siku siku")
sisi = 10
count = 1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break

print("akhir program")

# ciptaan sendiri

tinggi = int(input("masukan tinggi ="))

perbandingan_lebar = int(input("masukan perbandingan_lebar setiga ="))

count = 1

while True:
    print("*"*count)
    count += perbandingan_lebar

    pembatas = int(count / perbandingan_lebar)
    if pembatas == tinggi:
        break
print("akhir program")

#  3. hanya ganjil saja

print("membuat segitiga siku siku ganjil saja")
sisi = 10
count = 1
while True:
    if (count%2):
        #print jika ganjil
        print("*"*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("akhir program")

# membuat segitiga sama sisi

sisi = 10
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi, "*"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("akhir program")

# membuat belah ketupat

sisi = 10
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi, "*"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("akhir program")

while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi, "*"*count)
        count -= 1
        spasi += 1
    else:
        count += 1
        continue

    if count == 1:
        break
