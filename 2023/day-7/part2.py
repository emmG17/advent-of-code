card_map = { "T": "A", "J": "-", "Q": "C", "K": "D", "A": "E" }

def parse_cards(filename: str) -> list:
    cards = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            hand, bid = line.strip().split(' ');
            cards.append((hand, int(bid)));
    return cards

def most_frequent(hand: str) -> str:
    counts = dict.fromkeys(set(hand), 0)
    for card in hand:
        counts[card] += 1
    if "J" in counts.keys():
        del counts["J"]
    return max(counts, key = lambda x: counts[x])
    
def use_joker(hand: str) -> str:
    # Check if the hand is a Joker Five of a Kind
    if hand.count('J') == 5:
        return hand
    return hand.replace('J', most_frequent(hand)) 

def hand_rank(hand: str) -> tuple[int, str]:
    hand_values = "".join(card_map[card] if card in card_map.keys() else card for card in hand)
    if hand.find('J') != -1:
        hand = use_joker(hand)
    counts = [ hand.count(card) for card in hand ]
    if 5 in counts:
        return (7, hand_values)
    if 4 in counts:
        return (6, hand_values)
    if 3 in counts:
        if 2 in counts:
            return (5, hand_values)
        return (4, hand_values)
    if 2 in counts:
        if (counts.count(2) == 4):
            return (3, hand_values)
        return (2, hand_values)
    return (1, hand_values)
    

game = parse_cards('input.txt')
ranked_hands = sorted([ (hand_rank(hand), bid) for hand, bid in game ]) 

sum = 0
for i in range(len(ranked_hands)):
    sum += ranked_hands[i][1] * (i + 1)

print(sum)

