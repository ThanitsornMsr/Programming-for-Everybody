fname = input('Enter a file name: ')
ofname = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+fname)
for line in ofname:
    line = line.rstrip().upper()
    print(line)

fname = input('Enter a file name: ')
ofname = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+fname)
count = 0
sum = 0
for line in ofname:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        a = float(line[20:])
        sum = sum + a
print('Average spam confidence:', sum/count)

fname = input('Enter a file name: ')
try:
    ofname = open(r"C:/Users/User/PycharmProjects/Python_for_EveryOne/"+fname)
    count = 0
    for line in ofname:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were', count, 'subject lines in',fname)
except:
    if '.' in fname:
        print('File cannot be opened:', fname)
    else:
        print(fname.upper(),"TO YOU - You have been punk'd")