#default argument adalah ketika argumentnya kosong maka akan diisi otomatis oleh defaultnya

# def fungsi(argument = nilai defaultnya)

# contoh1

def say(nama = "kak"):
    print(f"hallo {nama}")

say("rizki")
say()


# contoh2
def pangkat(angka, pangkat=2):
    return angka ** pangkat

print(pangkat(10,3))
print(pangkat(8))