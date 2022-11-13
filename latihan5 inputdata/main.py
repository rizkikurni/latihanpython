# data yang dimasukan pasti string
data = input("masukan nama: ")

print("data = ",data,",type =",type(data))

# jika ingin mengambil integer dan boolean maka
bilangan = int(input("masukan angka:"))
bilangan = float(input("masukan angka: "))

print("data = ",bilangan,",type =",type(bilangan))

biner = bool(int(input("masukan nilai boolean:")))

print("data = ",biner,",type =",type(biner))
