# menyambung string 

nama_pertama = "alicia"
nama_tengah = "najwa"
nama_akhir = "ramadahani"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir

print(nama_lengkap)

# menghitung string

print(len(nama_lengkap))

# mengecek ada komponen atau tidak

z = "Z"
ngecek = z in nama_lengkap #ada
print(ngecek)


z = "Z"
ngecek = z not in nama_lengkap #tidak ada
print(ngecek)

# mengulang string
print(nama_akhir*5)

# indexing
print("index ke-3: " + nama_lengkap[3])
print("index ke- 3-8: " + nama_lengkap[3:9]) #3=>x>9
print("index ke-0-20 selang 2: " + nama_lengkap[0:21:2])

#item paling kecil
print("paling kecil:" + min(nama_lengkap))

#item paling besar
print("paling besar:" + max(nama_lengkap))
ascii_code = ord(" ")
print("spasi adalah" + str(ascii_code))

#operator dalam bentuk method

data = "najwa sangat cantik"
jumlah = data.count("a")
print("jumlah data", data, "=", str(jumlah))

###part2

#cara merubah huruf menjadi besar semua

contoh = "ai shi teru".upper()
print(contoh)

#cara merubah huruf menjadi kecil semua

contoh = "ai shi teru".lower()
print(contoh)

# cara pengecekan data dengan isX method

apakah_lower = contoh.islower()
print(str(apakah_lower))

"""
1) .isupper untuk mengecek huruf besar
2) .isalpha untuk mengecek semuanya huruf
3) .isalnum untuk huruf dan angka
4) .isdecimal untuk angka saja
5) .isspace untuk spasi, tab, newline
6) .istitle untuk kata yang dimulai dengan huruf besar
""" 

# ngecek komponen starswicth endswicth

cek_start = "kimi ni na wa".startswith("kimi")
print(cek_start)

cek_end = "kimi ni na wa".endswith("kimi")
print(cek_end)

# pengabungan komponen join dan split
pisah = ['roti','ini','sangat','enak']
gabungan = '.'.join(pisah)
print(gabungan)

gabungan = "akuiisangatiicintaiikamu"
print(gabungan.split('ii'))

#alokasi karakter rjust, ljust, center

kanan = "kanan".rjust(20,"-")
print("'"+kanan+"'")

# kebalikannya strip

kanan = kanan.strip("-")
print(kanan)

