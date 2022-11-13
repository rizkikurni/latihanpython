# args untuk mempersingkat dengan cara tanpa menggunakan list pada program

# kenalan dengan args


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

fungsi("rizki", 123,50)

# studi kasus

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    
    return output

hasiltambah = tambah(2,4,2,6,2,2)
print(hasiltambah)

