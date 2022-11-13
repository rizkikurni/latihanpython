import os
import CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt":  os.system("cls")
    
    print(f"""
        selamat datang di program
        database mahasiswa
        {"="*30}
        """)
    
    # cek ada database atau tidak
    CRUD.init_console()

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
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            
        print("="*20)

        is_done = input("Lanjut (y/n)?: ")
        if is_done == "n" or is_done == "N":
            break
