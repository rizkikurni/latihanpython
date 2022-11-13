membaca = open("data.txt",mode="r")

print(membaca.read())

# untuk mengecek bisa dibaca atau tidak
print(f"status read = {membaca.readable()}")
print(f"status write = {membaca.writable()}")

# membaca satu baris
membaca = open("data.txt",mode="r")
print(membaca.readline()) #membaca satu baris saja

# jadi list
membaca = open("data.txt",mode="r")
print(membaca.readlines()) #membaca satu baris saja
print(membaca.readlines()) #membaca satu baris saja

# apakah file sudah ditutup

print(f"apakah file sudah diclose = {membaca.closed}")

membaca.close()
print(f"apakah file sudah diclose = {membaca.closed}")


# salah satu teknik membuka file di python dengan with(mengclose otomatis)

with open("data.txt",mode="r") as files:
    content = files.readline()
    print(content,end="")



