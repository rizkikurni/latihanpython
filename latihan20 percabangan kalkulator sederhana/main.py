# kalkulator sederhana
import os

print("kalkulator sederhana")

angka1 = int(input("masukan angka 1 = "))
print("""
1. untuk penjumlahan
2. untuk pengurangan
3. untuk perkalian
4. untuk pembagian""")
operasi = input("masukan operasi yang di inginkan")
angka2 = int(input("masukan angka 2 = "))

if operasi == "1":
    print(f"hasinya adalah {angka1 + angka2}")
elif operasi == "2":
     print(f"hasinya adalah {angka1 - angka2}")
elif operasi == "3":
     print(f"hasinya adalah {angka1 * angka2}")
elif operasi == "4":
     print(f"hasinya adalah {angka1 / angka2}")
    