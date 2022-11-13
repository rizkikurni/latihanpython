from datetime import datetime


siswa1 = {
    'nama':'rizki kurniawan',
    'nim':'12345',
    'sks':130,
    'ttl':datetime(2004,8,31)
}

siswa2 = {
    'nama':'rizki kurniawan',
    'nim':'12345',
    'sks':130,
    'ttl':datetime(2004,8,31)
}

siswa3 = {
    'nama':'rizki kurniawan',
    'nim':'12345',
    'sks':130,
    'ttl':datetime(2004,8,31)
}

data_siswa = {
    'SIS001':siswa1,
    'SIS002':siswa2,
    'SIS003':siswa3
}

print(f"{'KODE':<6} {'NAMA':<17} {'NIM':^5} {'SKS':3} {'TTL':^10}")
print('-'*50)

for siswa in data_siswa:
    KEY =  siswa
    NAMA = data_siswa[KEY]['nama']
    NIM = data_siswa[KEY]['nim']
    SKS = data_siswa[KEY]['sks']
    TTL = data_siswa[KEY]['ttl'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<5} {SKS:<3} {TTL:<10}")



