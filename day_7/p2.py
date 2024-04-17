"""AoC Program 7 - 1b"""

import sys
from collections import Counter
import re

input_text = open(sys.argv[1]).read().strip()
lines = input_text.split("\n")

input = {}
for line in lines:
    res=line.strip().split()
    input.update({str(res[0]): int(res[1])})
    

def transulate_back(c):
    if c in [2,3,4,5,6,7,8,9]:
        return str(c)
    return {
        10: "T",
        1: "J",
        12: "Q",
        13: "K",
        14: "A"
    }[c]

def translate(c):
	if c.isnumeric():
		return int(c)
	return {
		"T":10,
		"J":1,
		"Q":12,
		"K":13,
		"A":14
	}[c]

rank = 1
results = {
    'high_cards': [], 
    'one_pair': [],
    'two_pair': [],
    'three_pair': [],
    'full_house': [],
    'four_kind': [],
    'five_kind':[]
}
def card_rank(cards):
    card_val = tuple(translate(c) for c in cards)
    cards = re.sub("J", "", cards)
    if len(set(cards)) == 5:
        results['high_cards'].append(card_val)
    elif len(set(cards))==4:
        results['one_pair'].append(card_val)
    elif len(set(cards))==3:
        # TTT98 -> 3 kind
        # 23432 -> 2 kind
        counter = [k for k, v in Counter(cards).items() if v==3]
        if counter:
            results['three_pair'].append(card_val)
        else:
            results['two_pair'].append(card_val)
    elif len(set(cards))==2:
        counter = [k for k, v in Counter(cards).items() if v==4]
        if counter:
            results['four_kind'].append(card_val)
        else:
            results['full_house'].append(card_val)
    elif len(set(cards))==1:
        results['five_kind'].append(card_val)
    
def cards_sort():
    """sort the cards."""
    results['high_cards'].sort()
    results['one_pair'].sort()
    results['two_pair'].sort()
    results['three_pair'].sort()
    results['full_house'].sort()
    results['four_kind'].sort()
    results['five_kind'].sort()
    
for cards, win in input.items():
    card_rank(cards)

cards_sort()
ans = 0
rank = 1
for i in ['high_cards', 'one_pair', 'two_pair', 'three_pair', 'full_house', 'four_kind', 'five_kind']:
    for card in results[i]:
        a = ["".join(transulate_back(c)) for c in card]
        ans += rank * input["".join(a)]
        rank += 1
print(ans)
