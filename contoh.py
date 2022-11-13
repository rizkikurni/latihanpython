import os
all_list = os.listdir()
n = 0
while n<9999 :
    try :
        list = all_list[n]
        print("%s."%(n+1), list)
        n = n+1
    except IndexError :
        break
pilihan = input("masukkan pilihan-->> ")
f = open('bot/%s'%(pilihan), 'r+')
baca = f.read()
print('''

1. ganti reff
2. buat file joiner
3. hapus reff
4. exit


''')

bm = input('masukkan pilihan-->> ')
if bm == '1' :
    if '5203652831' in baca:
        baca2 =baca.replace('5203652831', isi_saya)
        open = open('bot/%s'%(pilihan), 'w')
        open.write(baca2)
        open.close()
    else :
        print("ini file apa ya bang ndak tau akuu...")
elif bm == "2" :
    if '' in baca:
        baca2 =baca.replace('5203652831', isi_saya)
        open = open('bot/%s'%(pilihan), 'w')
        open.write(baca2)
        open.close()
    else :
        print("ini file apa ya bang ndak tau akuu...")