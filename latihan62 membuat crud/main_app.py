import os

if __name__ == "__main__":
    sistem_operasi = os.name

while True:
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt":  os.system("cls")

    print(f"""
    selamat datang di program
    database mahasiswa
    {"="*30}
    """)

    print("""
    1. Read Data
    2. Create Data
    3. Update Data
    4. Delete Data
    """)

    user_option = input("masukan opsi: ")

    print("="*20)
    
    match user_option:
        case "1":
            try:
                with open("data.txt",'r',encoding='utf-8') as file:
                    files = file.read()
                    print(files)
            except:
                print("file data.txt tidak ditemukan, membuat data baru")
                with open("data.txt",'w',encoding='utf-8') as file:
                    file.write("Daftar Mahasiswa")
        case "2":
            try:
                with open("data.txt",'a',encoding='utf-8') as file:
                    files = file.write()
                    print(files)
            except:
                print("file data.txt tidak ditemukan, membuat data baru")
                with open("data.txt",'w',encoding='utf-8') as file:
                    file.write("Daftar Mahasiswa")
        case "3": print("Read Data")
        case "4": print("Read Data")
        
    print("="*20)

    is_done = input("Lanjut (y/n)?: ")
    if is_done == "n" or is_done == "N":
        break
