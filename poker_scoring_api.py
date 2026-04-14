# TODO: Implement poker scoring api here

VALID_RANKS: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# FIXME: Is there an order for suits? (are suits ordered?)
VALID_SUITS: list[str] = ['H', 'D', 'C', 'S']

MAX_CARD_PER_HAND = 5  # Probably

def score_poker_hands(hand1: str | None, hand2: str | None) -> int:
    card_tuples1 = _parse_hand(hand1)
    score1 = _score_cards(card_tuples1)

    card_tuples2 = _parse_hand(hand2)
    score2 = _score_cards(card_tuples2)

    return 1 if score1 > score2 else 2

def _rank(card: str) -> int:
    """
    Return an integer representation of the rank of a valid card
    raises ValueError on invalid ranks (not listed in valid_ranks, above)
    """
    rank_str = card[0:-1]
    return VALID_RANKS.index(rank_str)

def _suit(card: str) -> int:
    """
    Return an integer representation of the suit of a valid card
    (FIXME: Are suits actually ordered or comparable?!)
    raises ValueError on invalid suits (not listed in valid_suits, above)
    """
    suit_str = card[-1]
    return VALID_SUITS.index(suit_str)

def _parse_card(card: str) -> tuple[int, int]:
    """
    Parse a card into a tuple of (rank, suit) integers
    raises a ValueError in the event of invalid ranks or suits (see above)
    """
    if not card:
        raise ValueError(f"Can't parse card: {card}")
    rank = _rank(card)
    suit = _suit(card)
    return rank, suit

def _parse_hand(hand: str | None) -> list[tuple[int, int]]:
    if not hand or not hand.strip():
        raise ValueError(f"Can't parse hand: \"{hand}\"")
    card_strs = hand.split(" ")
    cards = [_parse_card(c) for c in card_strs]
    return cards

def _score_cards(card_tuples: list[tuple[int, int]]) -> int:
    ranks = [rank for rank, _ in card_tuples]
    return max(ranks)

"""
TODO:
highest_card(hand) function?
"""