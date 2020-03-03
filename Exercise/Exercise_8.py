f = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/romeo.txt")
lst = list()
for line in f:
    line = line.strip().split()
    for i in line:
        if i in lst:
            continue
        else:
            lst.append(i)
print(sorted(lst))

name = input('Enter a file name: ')
f = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+name)
count = 0
for line in f:
    line = line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        print(line.split()[1])
        count = count + 1
print('There were',count,'lines in the file with From as the first word')

lst = list()
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    lst.append(float(num))
print('Maximum:', max(lst))
print('Minimum:', min(lst))