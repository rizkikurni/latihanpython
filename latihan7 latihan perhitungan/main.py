# latihan konversi satuan temperature

print("\nProgram konversi temperature\n")

celcius = float(input('masukan suhu dalam celcius: '))
print("suhu adalah",celcius,  "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamus adalah ", reamur, "reamur")

# farenheit
farenheit = ((9/5) * celcius) + 32
print("suhu dalam farenheit adalah", farenheit, "farenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin", kelvin, "kelvin")