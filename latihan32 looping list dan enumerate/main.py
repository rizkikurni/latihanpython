# looping dari list

# for loop

angka = [4,5,2,3,2,42]

for kontol in angka:
    print(kontol)

# for loop dan range

panjang = len(angka)

for pjg in range(panjang):
    print(angka[pjg])

# while loop

panjang = len(angka)
i = 0

while i < panjang:
    print(angka[i])
    i += 1

# list comprehension

data = ["rizki", "otong", "asu", 24, 2,2 ,2]

[print(i) for i in data]


# eumerate

for index,data in enumerate(data):
    print(f"index = {index}, data = {data}")
