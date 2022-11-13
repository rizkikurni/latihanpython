# copy

data = {
    "aku":"aku adalah orang yang hebat",
    "baby":"i love you baby"
}

datacopy = data.copy()

data["aku"] = "anger ngawor"

print(data)
print(datacopy)

# pop dictionary (berdassarkan keys)
pertama = datacopy.pop("aku")

print(pertama)


# popitem dictionary

kedua = datacopy.popitem()
print(kedua) #pop item menggambil data yang paling akhir
