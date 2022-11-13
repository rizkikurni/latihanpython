# list

# number
data = [1,2,3]

print(data)

# string
data_str = ["rizki", "kurniawan", "najwa"]
print(data_str)

# boolean
data_bool = [True, False]

# campuran
data_campuran = ["rizki", 1, 2, "wawa"]
print(data_campuran)

# cara alternatif membuat list

data_range = range(0,20,3) #range(start, stop, step)
print(list(data_range))


# membuat list dengan for loop
list_for = [i**2 for i in range(0,11)] #i bisa melakukan operasi matematika
print(list_for)

# membuat list pake for dan if

list_forif = [i for i in range(0,11) if i != 3] #menghilangkan angka
print(list_forif)

list_forif = [i for i in range(0,11) if i %2 != 0] #angka ganjil
print(list_forif)

list_forif = [i for i in range(0,11) if i %2 == 0] #angka genap
print(list_forif)

