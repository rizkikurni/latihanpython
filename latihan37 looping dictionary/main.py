# loping dictionary

data = {
    "aa":"aku",
    "bb":"baby",
    "cc":"cendol",
    "dd":"dudung",
    "ee":"europa"
}

# looping first try yang keluar adalah keynya saja

for dt in data:
    print(dt)

# operator untuk mengambil item

keys = data.keys()
print(keys)

for key in data.keys():
    print(data.get(key))

    # 2

value = data.values()
print(value)

for value in data.values():
    print(value)

    # 3

items = data.items()
print(items)

for item in data.items():
    print(item)

for key,valur in data.items():
    print(f"key ={key}, value = {valur}")