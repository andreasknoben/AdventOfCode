f = open('./2.txt')
lines = f.readlines()
f.close()

def part1():
    games = []
    possible = []

    for i in range(len(lines)):
        splitline = lines[i].split(':')
        games.append(int(splitline[0].split(' ')[1]))
        sets = splitline[1].split(';')

        line_possible = True
        for s in sets:
            s = s.split(',')
            counts = {'red': 0, 'green': 0, 'blue': 0}
            for item in s:
                item = item.strip()
                res = item.split(' ')
                counts[res[1]] += int(res[0])
            
            if (counts['red'] > 12) or (counts['green']) > 13 or (counts['blue'] > 14):
                line_possible = False
                break
            else:
                continue

        possible.append(line_possible)

    possible_id = [games[i] for i in range(len(games)) if possible[i]]
    return sum(possible_id)

print(part1())