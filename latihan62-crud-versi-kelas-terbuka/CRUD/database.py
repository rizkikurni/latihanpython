from . import operasi

DB_NAMA = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}


def init_console():
    try:
        with open(DB_NAMA,"r") as file:
            print("database tersedia, init selesai")
    
    except:
        print("database tidak ditemukan, silakan membuat database baru")
        operasi.create_fist_data()