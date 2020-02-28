# Chapter 5
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

for i in range(5,0,-1):
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year',friend)
print('Done!')

largest_to_far = -1
print('Before', largest_to_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_to_far:
        largest_to_far = the_num
    print(largest_to_far, the_num)
print('After', largest_to_far)

# counting loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# summing loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# finding tje average in loop
count = 0
sum = 0
print('Before', count, sum)
for i in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + i
    print(count, sum, i)
avg = sum / count
print('After',count, sum, avg)

# filtering in a loop
print('Before')
for i in [9, 41, 12, 3, 74, 15]:
    if i > 20:
        print('Large number', i)
print('After')

# search using a boolean variable
found = False
print('Before', found)
for i in [9, 41, 12, 3, 74, 15]:
    if i == 3:
        found = True
        print(found, i)
        break
    print(found, i)
print('After', found)

# how to find the smallest value
smallest_so_far = None
for i in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = i
    elif i < smallest_so_far:
        smallest_so_far = i
    print(smallest_so_far, i)
print('After', smallest_so_far)