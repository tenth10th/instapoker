from typing import Tuple, Iterable


# TODO: Implement poker scoring api here
def score_poker_hands(hand1: str, hand2: str) -> int:
    """
    Accept two hands as strings, return an integer
    """
    if hand1 == None or hand2 == None:
        raise ValueError("Bad input!")

    split_hand1 = hand1.split(" ")
    split_hand_2 = hand2.split(" ")

    max_hand_1 = max([parse_card(hand)[0] for hand in split_hand1])
    max_hand_2 = max([parse_card(hand)[0] for hand in split_hand_2])

    return 1 if max_hand_1 > max_hand_2 else 2


def parse_card(card: str) -> Tuple[str, str]:
    if card == None or len(card) < 2:
        raise ValueError("Bad card!")

    rank = card[0:-1]
    suit = card[-1]

    # Mapping of Card ranks to comparable integers
    rank_map = {str(i): i for i in range(2, 11)}
    rank_map.update(
        {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
    )

    try:
        rank = rank_map[rank]  # KeyError if not found
    except KeyError:
        raise ValueError("Bad rank!")

    # rank_map.get(rank) # None if not found

    suit_set = {"H", "D", "C", "S"}
    if suit not in suit_set:
        raise ValueError("Bad suit!")

    return (rank, suit)


"""
Example of loose "duck" typing in Python:

def foo(bar: Iterable):
    for x in bar:
        print(x)

foo("hello")
foo([1, 2, 3])
"""
