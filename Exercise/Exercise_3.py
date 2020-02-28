hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

if float(hours) > 40:
    total1 = float(hours) * float(rate)
    total2 = (float(hours) - 40) * (float(rate) * 0.5)
    pay = total1 + total2
    print('Pay:', pay)
else:
    pay = float(hours) * float(rate)
    print('Pay:', pay)


try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if float(hours) > 40:
        total1 = float(hours) * float(rate)
        total2 = (float(hours) - 40) * (float(rate) * 0.5)
        pay = total1 + total2
        print('Pay:', pay)
    else:
        pay = float(hours) * float(rate)
        print('Pay:', pay)
except:
    print('Error, please enter numberic input')

try:
    score = float(input('Enter score: '))
    if score >= 0 and score <= 1:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('Bad score')
except:
    print('Bad score')