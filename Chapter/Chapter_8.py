friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
carryon = ['socks', 'shirt', 'perfume']
a = [1, 24, 76]
b = ['red', 24, 98.6]
c = [1, [5, 6], 9]
d = []

for i in friends:
    print('Happy New Year:', i)
print('Done!')

lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto)
print(len(lotto))

print(range(5))
print(len(friends))
print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

print(dir(list))

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

print(friends)
print(friends[1])
friends.sort()
print(friends)
print(friends[1])

num = [3, 41, 12, 9, 74, 15]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))

# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average:', average)
#
# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' :
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print('Average:',average)

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for i in stuff:
    print(i)

line = 'first;second;third'
thing = line.split(';')
print(thing)
nline = 'a lot          of spaces'
etc = nline.split()
print(etc)

xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

words = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
nwords = words.split()
print(nwords)
email = nwords[1]
print(email)
print(email.split('@')[1])

