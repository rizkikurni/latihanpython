#1.cara membuat string

'''
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = 'menggunakan double quote'
print(data)

print('"Halo, apa kabar?"')

#2.menggunakan tanda \

#membuat tanda ' menjadi string
print('mari sholat jum\'at')

# backlash
print("C:\\user\\ucup")

# tab
print("ucup \t\t\t main jauh")

# backspace
print("ucup \bpintar, menghapus")

# newline
print("baris pertama \nbaris kedua") # LF
print("baris pertama \rbaris kedua") # CR
print("baris pertama \r\nbaris kedua") # CRLF untuk windows


# 3. string literasi atau raw

# mengunakan raw string
print(r'c:\new folder')

# multiline literal string
print("""
nama: rizki
kelas: 2a
""")