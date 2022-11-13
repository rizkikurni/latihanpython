barang1 = ["pensil", "limaribu", "faber castel"]
barang2 = ["tip ex", "sepuluh ribu", "kenk0"]
barang3 = ["pulpen", "dua ribu", "hitek"]

daftar_barang = [barang1, barang2, barang3]

# mengambil data list dalam list
print(daftar_barang[0][0])

# mengcopy sangat dalam 

from copy import deepcopy

daftar_barang_deepcopy = deepcopy(daftar_barang)

daftar_barang[2][1] = "rizki" #contoh percobaan
print(daftar_barang)
print(daftar_barang_deepcopy)
