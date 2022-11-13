from . import operasi

def delete_console():
    read_console()
    while True:
        print("silahkan pilih nomor yang akan didelete")
        no_buku = int(input("masukan nomor buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4]

            # data yang ingin dihapus
            print("n"+"="*150)
            print("Silahkan pilih data apa yang ingin anda ubah")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. penulis\t: {penulis:.40}")
            print(f"3. tahun\t: {tahun:.40}")
            is_done = input("apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("nomor buku tidak valid, silahkan masukan lagi")
    print("data berhasil dihapus")       

def update_console():
    read_console()
    while True:
        no_buku = int(input("nomor buku: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("nomor yang anda masukan tidak valid, silahkan masukan lagi")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        # data yang ingin di update
        print("n"+"="*150)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:.40}")

        # memilih data update
        user_option = input("Pilih data 1,2,3: ")
        print("\n"+"="*150)
        match user_option:
            case "1": judul = input("judul\t")
            case "2": penulis = input("penulis\t")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t:" ))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("silahkan masukan tahun yang benar (yyyy)")
                    except:
                        print("tahun harus angka boss")
            case _: print("index tidak cocok")
        print("data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:4}")
        is_done = input("Lanjut update data(y/n)?: ")
        if is_done == "n" or is_done == "N":
            break
    # print(data_buku)


    operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

def create_console():
    print("\n\n"+"="*150)
    print("Silahkan masukan data buku \n")
    penulis = input("penulis\t: ")
    judul = input("judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t:" ))
            if len(str(tahun)) == 4:
                break
            else:
                print("silahkan masukan tahun yang benar (yyyy)")
        except:
            print("tahun harus angka boss")
    operasi.create(tahun,judul,penulis)
    print("\nberikut adalah data baru anda")
    read_console()


def read_console():
    data_file = operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # data
    for index,data in enumerate(data_file):  
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")



    # footer
    print("="*100+"\n")