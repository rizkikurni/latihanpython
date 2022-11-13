# template
# def nama_fungsi(argument):
    #badan fungsi

def say_hello(nama):
    print(f"selamat datang di program kami {nama}")

say_hello("rizki")


# program tambah

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(input("masukan angka 1 = "), input("masukan angka 2 = "))

# fungsi dengan looping

def peserta(listpeserta):
    datapeserta = listpeserta.copy()
    for pesertaa in datapeserta:
        print(f"yang terhormat {pesertaa}")

daftarpeserta1 = ["rizki", "kamal", "deo"]
peserta(daftarpeserta1)
