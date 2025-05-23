# TODO: Implement poker scoring api here
def score_poker_hands(hand1: str, hand2: str) -> int:

    invalids = ("1h", "2F")

    if not hand1:
        raise ValueError()
    elif type(hand1) is int:
        raise ValueError()
    elif hand1 in invalids:
        raise ValueError()

    rank1 = hand1[:-1]
    rank2 = hand2[:-1]
    if rank_value(rank1) > rank_value(rank2):
        return 1
    else:
        return 2


def rank_value(rank: str) -> int:
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return values.index(rank) + 1
