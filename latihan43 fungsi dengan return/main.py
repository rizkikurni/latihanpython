# fungsi dengan return

# def nama_fungsi(argument):
    #badan fungsi
    # return output


# fungsi kuadrat
def kuadrat(inputangka):
    ouput_kuadrat = inputangka**2
    return ouput_kuadrat

print(kuadrat(7))
    
# fungsi tambah
def tambah(angka1, angka2):
    return angka1 + angka2

print(tambah(3,4))

# fungsi dengan return banyak
def operasimatematika(angka1, angka2):
    tambahh = angka1 + angka2
    kurangg = angka1 - angka2
    bagi = angka1 / angka2
    return tambahh, kurangg, bagi

a,b,c = operasimatematika(4,2)

print(f"hasil tambah = {a}")
print(f"hasil bagi = {c}")