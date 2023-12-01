import re

f = open('./1.txt', 'r')
lines = f.readlines()

def part1():
    total = 0
    for line in lines:
        first = re.search(r'[0-9]+', line).group()[0]
        last = re.search(r'[0-9]+', line[::-1]).group()[0]
        total += int(first + last)

    return total


def part2():
    regex_first = r'([0-9]|one|two|three|four|five|six|seven|eight|nine){1}'
    regex_last = r'([0-9]|one|two|three|four|five|six|seven|eight|nine)?$'

    total = 0
    numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in lines:
        first = re.search(regex_first, line).group()
        last = re.search(regex_last, line).group()
        while last == '' or last == None:
            line = line[:-1]
            last = re.search(regex_last, line).group()

        if first in numbers.keys():
            first = numbers[first]
        if last in numbers.keys():
            last = numbers[last]

        total += int(first + last)

    return total

print(part1())
print(part2())