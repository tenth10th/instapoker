import itertools
import random

ranks = list("23456789TJQKA")
suits = list("HDCS")

all_cards = [
    ''.join(card) for card in itertools.product(ranks, suits)
]

def get_random_hands(hand_count):
    i = 0
    hands = list()
    shuffled_cards = list(all_cards)
    random.shuffle(shuffled_cards)
    while i < len(shuffled_cards):
        hands.append(" ".join(shuffled_cards[i:i+5]))
        i += 5
    print(repr(list(hands[:hand_count])))

