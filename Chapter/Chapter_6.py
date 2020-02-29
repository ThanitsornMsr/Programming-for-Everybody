str1 = 'Hello'
str2 = "there"
bob = str1 + str2
print(bob)

str3 = '123'
x = int(str3) + 1
print(x)

name = input('Enter: ')
print(name)
apple = input('Enter: ')
x = int(apple) - 10
print(x)

fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)
x = len(fruit)
print(x)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# slicing string
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

# sring concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

# using in as a logical operator
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print('Found it!')

# string comparison
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# string library
print('A' < 'z')
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

print(dir(str))

# searching string
fruit = 'banana'
pos = fruit.find('na')
print(pos)
print(fruit.find('an'))
aa = fruit.find('z')
print(aa)

# search and replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)

# stripping whitespace
greet = '             Hello Bob        '
print(greet.lstrip(),'!')
print(greet.rstrip())
print(greet.strip())

# prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('please'))

# parsing and extracting
data = 'From stephen.marsuard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)