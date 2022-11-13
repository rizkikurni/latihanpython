import datetime as dt

tanggal_lahir = dt.date(2004, 8, 31)

print(f"tanggal lahir {tanggal_lahir} hari {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"umur dalam hari {hari_ini - tanggal_lahir} hari")
print(f"umur dalam bulan {(hari_ini - tanggal_lahir).days // 30} bulan")
print(f"umur dalam tahun {(hari_ini - tanggal_lahir).days // 365} tahun")
print(f"umur dalam sisa bulan {((hari_ini - tanggal_lahir).days % 365)//30} ")

