# penggunaan type hints digunakan untuk menandai data int/str/dll

import string


def pangkatsepuluh(argument:int) -> int:
    output =  10**argument
    return output

HASIL = pangkatsepuluh(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("rizki")
