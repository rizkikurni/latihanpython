# ketika kita menjalankan program utama(bukan import) makan akan keluar __main__
print(__name__)

# ini ketika kita menggunakan import
import tambah

# fungsinya

if __name__ == "__main__":
    print("hello word")

# ketika kita mempunyai folder yang isinya ada __main__ maka otomatis akan menjalankan file __main__