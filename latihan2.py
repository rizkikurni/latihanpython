print ('*******************************************************************')
print ('****************Program Suhu di Dalam Ruangan**********************')
print ('*******************************************************************')
print ('')
nama = input('Masukan Nama Ruangan :')
suhu = int(input('Masukan Suhu Ruangan :'))
print ('')
print ('Cetak :')
print ('Nama Perpustakaan:',nama)
if(suhu>=28):
    print ('Keterangan: Suhu di Dalam Ruangan',nama,'panas')
else:
    print ('Keterangan: Suhu di Dalam Ruangan',nama,'Dingin')
