from typing import Optional, Tuple
from enum import IntEnum


def score_poker_hands(hand1_str: str, hand2_str: str) -> int:
    if not isinstance(hand1_str, str) or not isinstance(hand1_str, str):
        raise ValueError("Please check hand types or be fired")
    hand1 = Hand(hand1_str)
    hand2 = Hand(hand2_str)
    if hand1.value() == hand2.value():
        return 0
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
    TWO_PAIR = 2


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

    def has_two_pair(self) -> Optional[int]:
        rank_counts: dict[int, int] = dict()
        for card in self.cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        pairs = []
        for rank, count in rank_counts.items():
            if count == 2:
                pairs.append(rank)
        pairs = sorted(pairs, reverse=True)
        return pairs if len(pairs) == 2 else None

    def value(self) -> Tuple[int, int, Tuple[int]]:
        comparisons = [
            (HandType.TWO_PAIR, self.has_two_pair),
            (HandType.PAIR, self.has_pair),
        ]
        sorted_cards = tuple(sorted([card.rank for card in self.cards], reverse=True))
        for hand_type, check_func in comparisons:x
            hand_value = check_func()
            if hand_value:
                return hand_type, hand_value, sorted_cards
        return HandType.HIGHEST_CARD, sorted_cards[0], sorted_cards
