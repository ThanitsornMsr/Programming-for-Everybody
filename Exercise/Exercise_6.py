str = 'X-DSPAM-Confidence:0.8475'
a = str.find(':')
b = float(str[a + 1:])
print(b)
print(type(b))