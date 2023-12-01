import re

f = open('./1.txt', 'r')
lines = f.readlines()

total = 0

for line in lines:
    first = re.search(r'[0-9]+', line).group()[0]
    last = re.search(r'[0-9]+', line[::-1]).group()[0]
    total += int(first + last)

print(total)