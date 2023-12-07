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

def intersection(winner, having):
    intersection = list(set(winner) & set(having))
    return intersection

def rewards_by_card(cards):
    rewards = []
    for i in range(len(cards)):
        card = cards[i]
        card_num = i + 1
        awarded_cards = len(intersection(card[0], card[1]))
        rewards.append((card_num, list(range(card_num + 1, card_num + 1 + awarded_cards))))
    return rewards

rewards = rewards_by_card(cards)

count_cards = {}
for i in range(len(cards)):
    card = cards[i]
    if rewards[i][0] not in count_cards:
        count_cards[rewards[i][0]] = 1
    else:
        count_cards[rewards[i][0]] += 1

    for j in range(len(rewards[i][1])):
        if rewards[i][1][j] not in count_cards:
            count_cards[rewards[i][1][j]] = count_cards[rewards[i][0]]
        else:
            count_cards[rewards[i][1][j]] += count_cards[rewards[i][0]]

print(sum(count_cards.values()))



