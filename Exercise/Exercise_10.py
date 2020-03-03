def max_count_email(xfile):
    d = dict()
    for line in xfile:
        line = line.strip()
        if line.startswith('From') and not line.startswith('From:'):
            word = line.split()
            d[word[1]] = d.get(word[1], 0) + 1
    lst = [(count, email) for email, count in d.items()]
    sortlst = sorted(lst, reverse=True)
    for v, k in sortlst[:1]:
        print(k, v)

name = input('Enter a file name: ')
try:
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    max_count_email(xfile)
except:
    name = 'mbox-short.txt'
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    max_count_email(xfile)

def count_hour(xfile):
    d = dict()
    for line in xfile:
        line = line.strip()
        if line.startswith('From') and not line.startswith('From:'):
            word = line.split()
            wordtime = word[5]
            d[wordtime[0:2]] = d.get(wordtime[0:2], 0) + 1
    lst = list()
    for k, v in d.items():
        lst.append((k, v))
    sortlst = sorted(lst)
    for k, v in sortlst:
        print(k, v)

name = input('Enter a file name: ')
try:
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    count_hour(xfile)
except:
    name = 'mbox-short.txt'
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    count_hour(xfile)

def count_char(xfile):
    d = dict()
    lst = list('abcdefghijklmnopqrstuvwxyz')
    for line in xfile:
        line = line.lower()
        for char in line:
            if char in lst:
                d[char] = d.get(char, 0) + 1
            else:
                continue
    print(sorted(d.items()))

name = input('Enter a file name: ')
try:
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    count_char(xfile)
except:
    name = 'mbox-short.txt'
    xfile = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + name)
    count_char(xfile)