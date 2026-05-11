# All known rank representations, in ascending order of value:
VALID_RANKS: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# TODO: Is there a natural order for suits? (are suits ordered?)
VALID_SUITS: list[str] = ['H', 'D', 'C', 'S']

MAX_CARDS_PER_HAND = 5  # According to last email?

def score_poker_hands(hand1: str | None, hand2: str | None) -> int:
    """
    Compare two hands, represented as strings of space-separated cards
    (e.g. "2H KD" for Two of Hearts, King of Diamonds)
    Returning 1 if the first hand is greater, or 2 if the second is...
    """
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
    raises ValueError on invalid suits (not listed in valid_suits, above)
        e.g. "H" for Hearts becomes 0, "D" for Diamonds becomes 1...
    TODO: Suits are checked for equality, but do they have a natural order? 
    """
    suit_str = card[-1]
    return VALID_SUITS.index(suit_str)

def _parse_card(card: str) -> tuple[int, int]:
    """
    Parse a card into a tuple of (int rank, suit letter)
    raises a ValueError in the event of invalid ranks or suits (see above)
        e.g. hand "2H" becomes (0, "H"), because 2 is the lowest Rank
        e.g. hand "AC" becomes (12, "C"), because Ace is the highest Rank
    """
    if not card:
        raise ValueError(f"Can't parse card: {card}")
    rank = _rank(card)
    suit = _suit(card)
    return rank, suit

def _parse_hand(hand: str | None) -> list[tuple[int, int]]:
    """
    Parse a hand string into a list of Card Tuples
    Card Tuples are a tuple of (int rank, suit letter)
    e.g. hand "2H KD" becomes [(0, "H"), (11, "D")]
    """
    if not hand or not hand.strip():
        raise ValueError(f"Can't parse hand: \"{hand}\"")
    card_strs = hand.split(" ")
    cards = [_parse_card(c) for c in card_strs]
    return cards

def _score_cards(card_tuples: list[tuple[int, int]]) -> int:
    """
    For a given list of Card Tuples, return the highest rank integer (see parse_card)
    (intended for use in "highest card" scoring)
    """
    ranks = [rank for rank, _ in card_tuples]
    return max(ranks)

"""
TODO:
highest_card(hand) function?
"""