a="hello buddy"
print(a[:5])
print(a[6:11])
print(a[0:11:2]) # last number is to jump by char
print(a[6:] + a[:6])
print(a[-4:] + a[:-3])
print(a[2::2])
print(a[::2])

print("=========")

tim = '16:30:10'
hrs, min, sec = tim.split(':')
print(hrs) ; print(min) ; print(sec)
print(tim.split(':', 1))  # split() only once
print(tim.split(':'))
print(tim.rsplit(':', 1)) #reverse split
print(tim.partition(':')) # partition can only do one split. it will presrive the delimiter and also put the output in tuple
print(tim.rpartition(':')) # rpartition is same as partition but reverse order
print("=========")

mystr="lotto"
print(mystr.replace('lo', 'ho'))

t = "mytest with some somspace"
print(t.replace(" ",""))
print(max(t))
print(len(t))
print(t.count("som")) ; print(t.count("some"))
print(t.index("t"))

d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(list(d.values()))
print(list(d))
d["one"] = 42
print(d)
del d["two"]
print(d)
