purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

# comparing lists and dictionaries
lst = list()
lst.append (21)
lst.insert(0,183)
print(lst)
lst[1] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

# dictionary literal
jjj = {'chuck' : 1,
       'fred' : 42,
       'jan' : 100}
print(jjj)
ooo = {}
print(ooo)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

aaa = dict()
lst = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for i in lst:
    if i in aaa:
        aaa[i] = aaa[i] + 1
    else:
        aaa[i] = 1
print(aaa)

count = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    count[name] = count.get(name, 0) + 1
    print(count)
print(count)

count = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    count[word] = count.get(word, 0) + 1
print('Count', count)

count = {'chuck' : 1,
         'fred' : 42,
         'jan' : 100}
for key in count:
    print(key, count[key])

print(list(count))
print(count.keys())
print(count.values())
print(count.items())

for k, v in count.items():
    print(k, v)