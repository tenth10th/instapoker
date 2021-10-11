# DO NOT COMMIT start
ranks = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}
suits = ('H', 'D', 'C', 'S')
def score_rank(rank):
    score = ranks.get(rank)
    if score is None:
        raise ValueError(f"Invalid rank: {rank}")
    return int(score)


def validate_suit(suit):
    if suit not in suits:
        raise ValueError(f"Invalid suit: {suit}")
    return suit

def parse_hand(hand):
    if not hand or not isinstance(hand, str):
        raise ValueError("Hands must be strings containing at least one card")
    cards = hand.split(" ")
    values = [(score_rank(c[0:len(c)-1]), validate_suit(c[-1])) for c in cards]
    values.sort(key=lambda x: x[0], reverse=True)
    return values
# DO NOT COMMIT end

def score_poker_hands(h1, h2):
    """
    Given two poker hands, represented by strings, return an integer result:
        0: Draw (hands have equal value)
        1: Hand 1 Wins
        2: Hand 2 Wins
    """
    # Delete start
    h1_values = parse_hand(h1)
    #print("\nHand 1:", h1, "=>",  h1_values)
    h2_values = parse_hand(h2)
    #print("Hand 2:", h2, "=>", h2_values)
    return 1 if h1_values[0] > h2_values[0] else 2
    # Delete end

    # TODO: Figure out how Poker hands are scored?
    # FIXME: Implement Poker scoring here, I guess
    pass
