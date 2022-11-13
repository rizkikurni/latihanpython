# latihan membuat program menghitung keliling dan luas persegi

import os
import math

def header():
    #ini adalah header
    os.system("clear")
    print(f"{'PROGRAM MENGHITUNG LUAS DAN KELILING SEGITIGA':^50}")
    print(f"{'-'*50:^50}")

def input_user():
    # ini adalah input user
    alas = int(input("masukan nilai alas : "))
    tinggi = int(input("masukan nilai tinggi : "))
    return alas, tinggi

def hitung_luas(alas, tinggi):
    return alas * tinggi /2

def hitung_keliling(alas, tinggi):
    sisi_kuadrat = alas**2 + tinggi**2
    sisi = sisi_kuadrat**(.5)
    return alas + tinggi + sisi


#PROGRAM UTAMA
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = print(f"Nilai Luas segitiga : {hitung_luas(LEBAR, PANJANG)}")
    KELILING = print(f"Nilai Keliling segitiga : {hitung_keliling(LEBAR, PANJANG)}")

    iscontinue = input("apakah lanjut y/n ???")
    if iscontinue == "n":
        break
print(f"""

{'PROGRAM SELESAI':^50}

""")