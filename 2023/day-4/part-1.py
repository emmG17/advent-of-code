def parse_lines(file):
    lines = []
    with open(file, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def parse_cards(lines):
    cards = []
    for line in lines:
        card = line.split(":")[1:][0]
        win_have = card.split(" | ")
        winner = win_have[0].strip().replace("  ", " ").split(" ")
        having = win_have[1].strip().replace("  ", " ").split(" ")
        cards.append((winner, having))
    return cards



lines = parse_lines('input.txt')
cards = parse_cards(lines)

def points(winner, having):
    intersection = list(set(winner) & set(having))
    matches = len(intersection)
    if matches == 0:
        return 0
    return 2 ** ( matches - 1 )

point_sum = 0
for card in cards:
    reward = points(card[0], card[1])
    point_sum += reward

print(point_sum)

