try:
    with open("data.txt",'r',encoding='utf-8') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat data baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("Daftar Mahasiswa")
