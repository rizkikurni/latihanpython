# operasi dictionary


data = {
    "riz":"rizki ganteng sekali",
    "waw":"adiku yang paling cantik sedunia",
    "tan":"tanto adik keduaku"
}

# panjang dictionary
LENDICT = len(data)
print(f"panjang data dictionary == {LENDICT}")

# mengecek key exist atau tidak
key = input("masukan key yang dicek :")
cekkey = key in data

if cekkey == True:
    print(f"apakah {key} ada di data: ada")
else:
    print(f"apakah {key} ada di data: tidak ada")

# mengakses value (read) dengan get

print(data.get("riz"))
print(data.get("dakjf", "data tidak ditemukan"))#jika pakai get ketika data tidak ada maka tidak akan eror

# mengupdate data

data.update({"riz":"akan menjadi raja iblis yang sangat hebat"})
print(data)
data.update({"wanwa":"es wawan sangat enak sekali"}) #jika menggunakan update maka ketika data tidak ada, otomatis akan ditambahkan, dan tidak akan eror
print(data)


# menghapus data

del data["riz"]
print(data)

