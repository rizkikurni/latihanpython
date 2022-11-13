# pass dia berfungsi sebagai dummy, tidak akan dieksekusi

angka= 5

print(angka)

while angka < 10:
    angka += 1
    if angka == 8:
        pass # dia tidak akan dieksekusi
    
    print(angka)

# continue

angka2 = 1

print(f"angka sekarang adalah {angka2}")

while angka2 < 6:
    angka2 += 1
    print(f"angka sekarang adalah {angka2}")

    if angka2 == 4:
        print("iki bedo dewe")
        continue #jadi fungsinya untuk meloncati funcion dibawahnya

    print("bagus")

print("selesai")