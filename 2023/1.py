import re

f = open('./1.txt', 'r')
lines = f.readlines()

numbers = []

for line in lines:
    first = re.search(r'[0-9]+', line).group()[0]
    last = re.search(r'[0-9]+', line[::-1]).group()[0]
    
    num = first + last
    numbers.append(int(num))

print(sum(numbers))