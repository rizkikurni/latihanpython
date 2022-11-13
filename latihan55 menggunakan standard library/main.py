import datetime as dt

print(dt.datetime.now())


from collections import Counter

data = ["a", "b", "a","b","d","d"]

print(f"jumlah data a adalah {Counter(data)['a']}")