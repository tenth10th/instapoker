from typing import Optional, Tuple
from enum import IntEnum


def score_poker_hands(hand1_str: str, hand2_str: str) -> int:
    if not isinstance(hand1_str, str) or not isinstance(hand1_str, str):
        raise ValueError("Please check hand types or be fired")
    hand1 = Hand(hand1_str)
    hand2 = Hand(hand2_str)
    return 1 if hand1.value() > hand2.value() else 2


class Card:
    def __init__(self, card_str: str):
        if len(card_str) < 2:
            raise ValueError("Cards must be at least two characters")
        self.suit = card_str[-1]
        if self.suit not in "HDCS":
            raise ValueError("That is not a valid suit")
        self.rank_str = card_str[0:-1]
        self.int_rank()
    # TODO: Add accessors? validators?

    rank_values = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def int_rank(self):
        self.rank = self.rank_values.get(
            self.rank_str,
        )
        if self.rank is None:
            try:
                self.rank = int(self.rank_str)
            except ValueError:
                raise ValueError("That is not a valid rank")
            if self.rank < 2 or self.rank > 9:
                raise ValueError("The card rank must be between 2 and 9")


class HandType(IntEnum):
    HIGHEST_CARD = 0
    PAIR = 1


class Hand:
    def __init__(self, hand_str: str):
        self.cards = list(map(Card, hand_str.split(" ")))

    def highest_card(self):
        print("self.cards", self.cards)
        # Eventually, this could get us the "kicker" (for ties)
        return max(map(lambda x: x.rank, self.cards))

    def has_pair(self) -> Optional[int]:
        rank_counts: dict[int, int] = dict()
        for card in self.cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        best_pair = None
        for rank, count in rank_counts.items():
            if count >= 2 and (best_pair is None or rank > best_pair):
                best_pair = rank
        return best_pair

    def value(self) -> Tuple[int, int]:
        pair_value = self.has_pair()
        high_card = self.highest_card()
        hand_type = HandType.PAIR if pair_value else HandType.HIGHEST_CARD
        hand_value = pair_value or high_card
        # Need to re-evaluate this as more Hands are added!
        return hand_type, hand_value
