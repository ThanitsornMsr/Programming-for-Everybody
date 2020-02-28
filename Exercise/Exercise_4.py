def fred():
    print('Zap')
def jane():
    print('ABC')
jane()
fred()
jane()

def computepay(hours, rate):
    if hours > 40:
        total1 = hours * rate
        total2 = (hours - 40) * (rate * 0.5)
        pay = total1 + total2
        return pay
    else:
        pay = hours * rate
        return pay
try:
    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    print('Pay:',computepay(float(hours),float(rate)))
except:
    print('Error, please enter numeric input')

def computegrade(score):
    if score >= 0 and score <= 1:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return 'Bad score'
try:
    score = input('Enter score: ')
    print(computepay(float(score)))
except:
    print('Bad score')