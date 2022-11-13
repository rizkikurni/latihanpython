# manipulasi list
# index               0        1       2    (dari depan)
# index               -3       -2      -1   (dari belakang) 
data = ["rizki", "wawa", "tanto"]

print(data[0])

# mengambil info jumlah data
panjang_data = len(data[1])
print(panjang_data)

# menambahkan data
    # data.insert(posisi, item)
data.insert(2, "fafa")
print(data)

    #menambah data diakhir
data.append("deo")
print(data) 

    # mengabungkan kedua list
data.extend(["ini data baru 1", "data 2"])
print(data)

# merubah data
data[3] = "berubah menjadi 3"

    # menghapus data
data.remove("rizki")
print(data)
    # menghapus data paling belakang
data.pop()
print(data)


