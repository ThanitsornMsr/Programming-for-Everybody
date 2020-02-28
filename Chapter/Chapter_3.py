# Chapter 3

#if...else
x = 5
if x < 10:
    print('Smaller')
else:
    print('Bigger')
print('Finish')

x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

x = 20
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

# try/except Sample
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a Number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
else:
    print('Not a Number')