# latihan penggunaan list

daftar_barang = []
while True:
    print("masukan daftar barang")
    nama = input("nama barang:")
    harga = input("harga barang:")

    barang = [nama, harga]
    daftar_barang.append(barang)

    print("="*20, "daftar barang", "="*20)
    for index, brg in enumerate(daftar_barang):
        print(f"{index+1} | {brg[0]} | {brg[1]}")

    print("="*40)
    end = input("apakah lanjut?? y/n")
    if end == "n" or "N":
        break
print("program selesai")