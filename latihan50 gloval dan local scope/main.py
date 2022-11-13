# global scope


nama_global = "rizki"
# akses variabel global dalam fungsi
    # bisa juga diakses dilooping 
def fungsi():
    print(f"nama anda adalah {nama_global}")

fungsi()

# local scope
angka = 0

def ubah_angka(nilai):
    nilai = angka
    

print(f"sebelum diubah {angka}")
ubah_angka(10)
print("setelah dirubah {angka}")


