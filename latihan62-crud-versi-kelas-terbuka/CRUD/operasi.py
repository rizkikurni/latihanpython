import string
import random
import time
from .util import random_string
from . import database
import os

def delete(no_buku):
    try:
        with open(database.DB_NAMA,'r') as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku -1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
         print("database eror")
    
    os.rename("data_temp.txt",database.DB_NAMA)
                
def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)    

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(database.DB_NAMA,'r+',encoding="utf-8")as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("salah di operasi")
    


def create_fist_data():
    penulis = input("Penulis: ")
    judul =  input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t:" ))
            if len(str(tahun)) == 4:
                break
            else:
                print("silahkan masukan tahun yang benar (yyyy)")
        except:
            print("tahun harus angka boss")

    data = database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(database.DB_NAMA,'w',encoding="utf-8")as file:
            file.write(data_str)
    except:
        print("udahlah gagal boss")



def create(tahun,judul,penulis):
    data = database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(database.DB_NAMA,'a',encoding="utf-8")as file:
            file.write(data_str)
    except:
        print("udahlah gagal boss")

def read(**kwargs):
    try:
        with open(database.DB_NAMA,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            print(jumlah_buku)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("membaca database eror")
        return False

