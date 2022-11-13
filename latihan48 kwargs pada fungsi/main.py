# **kwargs sama seperti args tapi ini untuk data dictionary



from ctypes.wintypes import PLARGE_INTEGER
from optparse import Option


def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")


fungsi(nama="rizki", tinggi=170, berat=64)



# studi kasus

def math(*args,**kwargs):
    output = 0 
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka

    elif kwargs["option"] == "kurang":
        for angka in args:
            output -= angka
    
    else:
        print("TIDAK ADA OPERASI APAPUN")

    return output

hasil = math(9,1,2,5,option="kurang")

print(hasil)
