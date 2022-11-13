# contoh sederhana


from numbers import Number


while True:
    angka = int(input("masukan angka yang akan membagi angka 10 = "))
    hasil = 0

    try:
        hasil = 10/angka
        print(f"hasilnya adalah {hasil}")
        out = input("ulang? (Y/N)")
        if out == "n" and "N":
            break
        
    except:
        print("angka tidak boleh nol")


# contoh kedua
try:
    with open("data.txt",'r',encoding='utf-8') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

    
# exceptin eror message
angka = 0
try:
    hasil = 8/angka
except Exception as eror:
    print(eror)

# membuat exception sendiri

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(2,"v"))
    