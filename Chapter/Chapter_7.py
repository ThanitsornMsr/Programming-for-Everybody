# using open()
handle = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
print(handle)

# bewline character
stuff = 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
print(len(stuff))

# file handel as a sequence
count = 0
xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
for char in xfile:
    # print(char)
    count = count + 1
print('Line Count:',count)

# reading the whole file
xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
inp = xfile.read()
print(len(inp))
print(inp[:20])

# search throught a file
xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
for line in xfile:
    if line.startswith('From:'):
        # print(line)
        print(line.strip('\n'))
print('-'*20)

# skipping with continue
xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# using in to select lines
xfile = open(r'C:\Users\User\PycharmProjects\Python_for_EveryOne\mbox-short.txt', 'r')
for line in xfile:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/" + fname)
    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were',count,'subject line in',fname)
except:
    print('File cannot be opened:', fname)