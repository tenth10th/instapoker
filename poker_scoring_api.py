rank_values = {str(x):x for x in range(2, 11)}
rank_values['J'] = 11
rank_values['Q'] = 12
rank_values['K'] = 13
rank_values['A'] = 14

suit_values = "CDHS"


def score_poker_hands(first_hand: str, second_hand: str):
    if first_hand is None or second_hand is None:
        raise ValueError("Invalid None hands:", first_hand, second_hand)

    first_rank = first_hand[0:-1]
    second_rank = second_hand[0:-1]
    
    if first_rank not in rank_values or second_rank not in rank_values:
        raise ValueError("Invalid rank in hands:", first_hand, second_hand)

    first_suit = first_hand[-1]
    second_suit = second_hand[-1]
    
    if first_suit not in suit_values or second_suit not in suit_values:
        raise ValueError("Invalid suit in hands:", first_hand, second_hand)

    if (int(first_rank) > int(second_rank)):
        return 1
    else:
        return 2
