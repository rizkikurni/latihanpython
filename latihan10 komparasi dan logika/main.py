# membuat gabungan area rentang dari angka

# ++++++++++3----------10+++++++++=

inputuser = float(input("masukan angka <3 atau >10: "))

kurangdari3 = (inputuser < 3)
lebihdari10 = (inputuser >10)
print(kurangdari3 or lebihdari10)

# ----------3++++++++++10------------
inputuser = float(input("masukan angka >3 atau <10: "))

kurangdari3 = (inputuser > 3)
lebihdari10 = (inputuser <10)
print(kurangdari3 and lebihdari10)

#------0+++++++++++5-------8+++++++11------
inputuser = float(input("masukan angka: "))

lebihdari0 = (inputuser > 0)
kurangdari5 = (inputuser < 5)
lebihdari8 = (inputuser > 8)
kurangdari11 = (inputuser < 11)

print((lebihdari0 and kurangdari5) or (lebihdari8 and kurangdari11))