sum = 0
count = 0
listnumber = []

while True:
    try:
        number = input('Enter a number: ')
        sum = sum + float(number)
        count = count + 1
        listnumber.append(float(number))
    except:
        if number == 'done':
            break
        else:
            print('Invalid input')
            pass

print(sum, count, sum/count)

less = None
for i in listnumber:
    if less is None:
        less = i
    elif i < less:
        less = i
print('Minimum number:', less)

more = None
for i in listnumber:
    if more is None:
        more = i
    elif i > more:
        more = i
print('Maximum number:', more)


