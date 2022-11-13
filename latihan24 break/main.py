# break langsung program end(kalau langsung ketemu, trus end)

angka = 1

while angka < 20:
    angka += 2
    print(f"angka sekarang adalah {angka}")

    if angka == 9:
        print("akhirnya ketemu")
        break
    print("salah")

print("finish")

#latihan menggunakan break

data_int = int(input("hitung sampai"))
angka = 0

while True:
    angka += 1
    print(f"hitung angka = {angka}")

    if angka == data_int:
        print("akhirnya ketemu")
        break
    print("kurang")

print("finish")