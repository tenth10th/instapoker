"""
generate random hands
"""

import itertools
import random
from typing import List

ranks = list("23456789TJQKA")
suits = list("HDCS")

all_cards = ["".join(card) for card in itertools.product(ranks, suits)]


def get_random_hands(hand_count : int) -> None:
    """
    generate hand_count many hands of cards
    where each hand consists of 5 cards
    """
    i = 0
    hands : List[str] = []
    shuffled_cards = list(all_cards)
    random.shuffle(shuffled_cards)
    while i < len(shuffled_cards):
        hands.append(" ".join(shuffled_cards[i : i + 5]))
        i += 5
    print(repr(list(hands[:hand_count])))
