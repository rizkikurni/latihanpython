try:
    with open("data.txt",'a',encoding='utf-8') as file:
        nama = input("masukan nama mahasiswa : ")
        data = file.write(nama)
        print(data)
except:
    print("file data.txt tidak ditemukan, membuat data baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("Daftar Mahasiswa")
