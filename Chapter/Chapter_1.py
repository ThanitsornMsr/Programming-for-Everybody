# Chapter 1
name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

fh = open('romeo.txt','r')

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,'Lines')