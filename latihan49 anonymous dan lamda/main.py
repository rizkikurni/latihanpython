# lamda fungsion adalah untuk mempersingkat def

# menggunakan cara def
def kuadratdef(angka):
    return angka**2

print(kuadratdef(8))


# menggunakan lamda
    # output = lambda argument: expression
kuadrat = lambda angka : angka**2
print(f"hasi lamda kuadrat = {kuadrat(3)}")

pangkat2 = lambda angka,pangkat : angka**pangkat
print(f"hasi lamda pangkat = {pangkat2(3,3)}")


# sorting untuk list biasa
data_list = ["rizki","abel","tanto","najwa"]
data_list.sort()
print(data_list)

# sorting pakai panjang huruf

def panjangnama(nama):
    return len(nama)

data_list.sort(key=panjangnama)
print(data_list) 

# sorting pakai lamda
data_list = ["rizki","abel","tanto","najwa","aziz"]
data_list.sort(key=lambda nama:len(nama))

print(data_list)


# filter
angka = [1,2,3,4,5,6,7,8,9,10]

data_angka = list(filter(lambda x:x<7,angka))
print(data_angka)

    # angka genap
data_angka = list(filter(lambda x:x%2==0,angka))
print(data_angka)




# anonymous fungsion

def pangkat(n):
    return lambda angka:angka**n

pangkat3 = pangkat(3)
print(pangkat3(2))