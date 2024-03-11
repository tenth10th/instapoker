def score_poker_hands(hand1, hand2):
    """
    Given two hands, return an integer indicating which hand won (1 or 2)

    Currently, each hand consists of a single card...

    Currently, the hand with the highest ranked card wins...
    """
    # Validate that both hands are strings!
    if (not isinstance(hand1, str)) or (not isinstance(hand2, str)):
        raise ValueError("hand is not a string")

    rank1 = get_rank(hand1)
    rank2 = get_rank(hand2)

    if rank1 is None:
        raise ValueError("hand1 invalid rank")
    if rank2 is None:
        raise ValueError("hand2 invalid rank")

    suit1 = get_suit(hand1)
    suit2 = get_suit(hand2)

    if suit1 is None:
        raise ValueError("hand1 invalid suit")
    if suit2 is None:
        raise ValueError("hand2 invalid suit")

    if get_rank(hand1) > get_rank(hand2):
        return 1
    else:
        return 2


def get_rank(card):
    """
    Return card's rank as an integer (or None if invalid)
    """
    str_rank = card[:-1]

    # Dictionary seems like the simplest way to
    # associate strings with int values (and look up
    # those associations easily)
    # fmt: off
    rank_dict = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10, 
        "J": 11, "Q": 12, "K": 13, "A": 14
    }
    # fmt: on

    # Remember: dictionary.get returns None if the key doesn't exist...
    int_rank = rank_dict.get(str_rank)

    return int_rank


def get_suit(card):
    """
    Return uppercase suit letter (or None if invalid)
    """
    str_suit = card[-1]

    # Remember: {} can be used for a Set literal...
    valid_suits = {"H", "S", "C", "D"}

    if str_suit in valid_suits:
        return str_suit
    else:
        return None
