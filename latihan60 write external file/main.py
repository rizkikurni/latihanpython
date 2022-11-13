# mode write

with open("data.txt",'w',encoding="utf-8") as file:
    file.write("""rizki tampan sekali dan sangat ganteng
    aku adalah orang""")
# tidak bisa melanjutkan write dengan with baru, harus dalam satu with


# mode append(menambah)

with open("data1.txt",'w',encoding="utf-8") as file:
    file.write("""rizki tampan sekali dan sangat ganteng
    aku adalah orang\n""")

with open("data1.txt",'a',encoding="utf-8") as file:
    file.write("""rizki tampan sekali dan sangat ganteng
    aku adalah orang""")

# untuk mengatasi masalah diatas

# mode r+(akan menimpa sesuai dengan panjang data)

with open("data2.txt",'w',encoding="utf-8") as file:
    file.write("""rizki tampan sekali dan sangat ganteng
    aku adalah orang\n""")

with open("data2.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")
    file.write("baris-4\n")



