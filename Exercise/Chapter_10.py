x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(max(y))

for i in y:
    print(i)

print(dir(tuple))

(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

d = dict()
d['csev'] = 2
d['cwen'] = 4
for k, v in d.items():
    print(k, v)
tups = d.items()
print(tups)

print((0, 1,2) < (5, 1, 2))
print((0, 1, 200000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adam', 'Sam'))
print('J' > 'A')

d = {'a' : 10,
     'b' : 1,
     'c' : 22}
print(d.items())
print(sorted(d.items()))

d = {'a' : 10,
     'b' : 1,
     'c' : 22}
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)

d = {'a' : 10,
     'b' : 1,
     'c' : 22}
l = list()
for k, v in d.items():
    l.append((v, k))
print(l)
tmp = sorted(l, reverse=True)
print(tmp)

xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\romeo.txt', 'r')
count = dict()
for line in xfile:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
lst = list()
for k, v in count.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v, k in lst[:10]:
    print(k, v)

d = {'a' : 10,
     'b' : 1,
     'c' : 22}
print(sorted([(v, k) for k, v in d.items()]))