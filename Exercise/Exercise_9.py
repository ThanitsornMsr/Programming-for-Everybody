xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/words.txt")
dct = dict()
for line in xfile:
    line = line.rstrip().split()
    for word in line:
        dct[word] = dct.get(word, 0) + 1
print(dct)

name = input('Enter a file name: ')
xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+name)
dct = dict()
for line in xfile:
    line = line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        x = line.split()
        dct[x[2]] = dct.get(x[2], 0) + 1
print(dct)

name = input('Enter a file name: ')
xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+name)
dct = dict()
for line in xfile:
    line = line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        x = line.split()
        dct[x[1]] = dct.get(x[1], 0) + 1
print(dct)

maxdctk = None
maxdctv = None
name = input('Enter a file name: ')
xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+name)
dct = dict()
for line in xfile:
    line = line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        x = line.split()
        dct[x[1]] = dct.get(x[1], 0) + 1
for k, v in dct.items():
    if maxdctv is None or v > maxdctv:
        maxdctv = v
        maxdctk = k
print(maxdctk, maxdctv)

name = input('Enter a file name: ')
xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
dct = dict()
for line in xfile:
    line = line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        x = line.split()
        dct[x[1][x[1].find('@')+1:]] = dct.get(x[1][x[1].find('@')+1:], 0) + 1
print(dct)